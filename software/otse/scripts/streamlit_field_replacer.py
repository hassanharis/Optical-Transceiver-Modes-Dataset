"""
Streamlit UI for OTSE run field value replacements.

Run after installing OTSE:
    python -m otse.launch harmonize
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

import pandas as pd
import streamlit as st

from otse.composition.field_replacer import (
    DEFAULT_CONFIG_PATH,
    ReplacementConfig,
    apply_to_runs,
    load_config_document,
    preview_run_changes,
    reload_config,
    save_config_document,
)
from otse.composition.fields import FieldKind, discover_fields, field_literals
from otse.composition.loader import default_runs_dir, iter_run_dirs, load_corpus, runs_corpus_version

st.set_page_config(
    page_title="OTSE field value replacer",
    layout="wide",
    initial_sidebar_state="expanded",
)

ARTIFACT_HELP = (
    "Files updated per run folder: "
    "specs.json, raw_llm.json, mode_atoms.json, modes.json, "
    "raw_llm_modes.json, raw_llm_modes_response.json"
)


def parse_from_values(text: str) -> list[str]:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if len(lines) <= 1 and "," in text:
        return [p.strip() for p in text.split(",") if p.strip()]
    return lines


def rules_to_document(base: dict, rules_ui: list[dict]) -> dict:
    doc = deepcopy(base)
    doc["rules"] = []
    for row in rules_ui:
        field = (row.get("field") or "").strip()
        to_val = (row.get("to") or "").strip()
        if not field or not to_val:
            continue
        doc["rules"].append(
            {
                "field": field,
                "to": to_val,
                "from": parse_from_values(str(row.get("from_text") or "")),
                "case_insensitive": bool(row.get("case_insensitive", True)),
                "dedupe_lists": bool(row.get("dedupe_lists", True)),
            }
        )
    return doc


@st.cache_data(show_spinner="Discovering fields and values…")
def cached_field_catalog(
    runs_dir: str,
    corpus_version: int,
    run_ids: tuple[str, ...],
) -> tuple[list[str], dict[str, list[str]], int]:
    """Return categorical field names, literals per field, and module count."""
    root = Path(runs_dir)
    if not root.is_dir():
        return [], {}, 0

    records = load_corpus(root)
    if run_ids:
        allowed = set(run_ids)
        records = [r for r in records if r.run_id in allowed]

    literal_sets: dict[str, set[str]] = {}
    for info in discover_fields(records):
        if info.kind not in (FieldKind.CATEGORICAL, FieldKind.BOOLEAN):
            continue
        literal_sets.setdefault(info.name, set()).update(
            field_literals(records, info.name, info.level)
        )

    names = sorted(literal_sets.keys(), key=str.lower)
    literals = {
        name: sorted(vals, key=lambda s: s.casefold())
        for name, vals in literal_sets.items()
    }
    return names, literals, len(records)


def field_select_options(field_names: list[str], current: str) -> list[str]:
    options = list(field_names)
    if current and current not in options:
        options.append(current)
        options.sort(key=str.lower)
    return options


RAW_RULES_JSON_KEY = "raw_rules_json"
RAW_RULES_JSON_PENDING_KEY = "_raw_rules_json_pending"


def format_rules_document(doc: dict) -> str:
    return json.dumps(doc, indent=2, ensure_ascii=False)


def schedule_raw_rules_json(doc: dict) -> None:
    """Queue JSON text for the editor; applied before the text_area on the next run."""
    st.session_state[RAW_RULES_JSON_PENDING_KEY] = format_rules_document(doc)


def flush_pending_raw_rules_json() -> None:
    pending = st.session_state.pop(RAW_RULES_JSON_PENDING_KEY, None)
    if pending is not None:
        st.session_state[RAW_RULES_JSON_KEY] = pending


def init_raw_rules_json_if_missing(config_doc: dict, rules_ui: list[dict]) -> None:
    if RAW_RULES_JSON_KEY in st.session_state:
        return
    st.session_state[RAW_RULES_JSON_KEY] = format_rules_document(
        rules_to_document(config_doc, rules_ui)
    )


def document_to_rules_ui(doc: dict) -> list[dict]:
    rows: list[dict] = []
    for rule in doc.get("rules", []):
        from_list = rule.get("from") or []
        rows.append(
            {
                "field": rule.get("field", ""),
                "to": rule.get("to", ""),
                "from_text": "\n".join(str(x) for x in from_list),
                "case_insensitive": bool(rule.get("case_insensitive", True)),
                "dedupe_lists": bool(rule.get("dedupe_lists", True)),
            }
        )
    return rows


def main() -> None:
    st.title("OTSE field value replacer")
    st.caption(
        "Edit replacement rules and apply them to run JSON under `runs/`. "
        "Regenerate HTML reports from OTSE after applying."
    )

    if "config_doc" not in st.session_state:
        st.session_state.config_doc = load_config_document(DEFAULT_CONFIG_PATH)
    if "rules_ui" not in st.session_state:
        st.session_state.rules_ui = document_to_rules_ui(st.session_state.config_doc)
    init_raw_rules_json_if_missing(
        st.session_state.config_doc,
        st.session_state.rules_ui,
    )

    with st.sidebar:
        st.header("Paths")
        runs_dir = st.text_input("Runs directory", value=str(default_runs_dir()))
        config_path = st.text_input("Rules file", value=str(DEFAULT_CONFIG_PATH))

        if st.button("Reload rules from disk"):
            path = Path(config_path)
            if path.is_file():
                st.session_state.config_doc = load_config_document(path)
                st.session_state.rules_ui = document_to_rules_ui(st.session_state.config_doc)
                schedule_raw_rules_json(st.session_state.config_doc)
                reload_config(path)
                st.success(f"Loaded {path.name}")
            else:
                st.error("Rules file not found")

        run_dirs = sorted(p.name for p in iter_run_dirs(Path(runs_dir))) if Path(runs_dir).is_dir() else []
        st.caption(f"{len(run_dirs)} run folders with meta.json")
        limit_runs = st.checkbox("Limit to selected runs", value=False)
        selected_runs: list[str] = []
        if limit_runs and run_dirs:
            selected_runs = st.multiselect("Run IDs", options=run_dirs, default=[])

        if st.button("Refresh field catalog"):
            st.cache_data.clear()

    runs_path = Path(runs_dir)
    corpus_version = runs_corpus_version(runs_path) if runs_path.is_dir() else 0
    run_key = tuple(sorted(selected_runs)) if limit_runs and selected_runs else ()
    field_names, literals_by_field, n_modules = cached_field_catalog(
        runs_dir,
        corpus_version,
        run_key,
    )

    cfg_path = Path(config_path)
    doc = st.session_state.config_doc

    def active_config() -> ReplacementConfig:
        return ReplacementConfig.from_dict(
            rules_to_document(doc, st.session_state.rules_ui)
        )

    tab_rules, tab_json, tab_preview, tab_apply = st.tabs(
        ["Rules", "JSON", "Preview", "Apply"]
    )

    with tab_rules:
        st.subheader("Replacement rules")
        st.markdown(ARTIFACT_HELP)
        if runs_path.is_dir():
            st.caption(
                f"Corpus: **{n_modules}** modules · **{len(field_names)}** categorical fields "
                f"(snapshot `v{corpus_version}`)"
            )
        else:
            st.warning("Runs directory not found — field dropdown will be empty.")

        if st.button("Add rule"):
            st.session_state.rules_ui.append(
                {
                    "field": "",
                    "to": "",
                    "from_text": "",
                    "case_insensitive": True,
                    "dedupe_lists": True,
                }
            )
            st.rerun()

        to_remove: list[int] = []
        for idx, row in enumerate(st.session_state.rules_ui):
            title = row.get("field") or "(new)"
            with st.expander(f"Rule {idx + 1}: {title}", expanded=not row.get("field")):
                col_values, col_rule = st.columns([1.15, 1], gap="large")

                options = field_select_options(field_names, str(row.get("field") or ""))
                current_field = str(row.get("field") or "")

                with col_rule:
                    if options:
                        field_index = options.index(current_field) if current_field in options else 0
                        picked_field = st.selectbox(
                            "Field",
                            options=options,
                            index=field_index,
                            format_func=lambda x: x or "— select field —",
                            key=f"field_{idx}",
                        )
                    else:
                        picked_field = st.text_input(
                            "Field name",
                            value=current_field,
                            key=f"field_manual_{idx}",
                            help="No categorical fields found in runs; enter a schema field name.",
                        )
                    row["field"] = (picked_field or "").strip()
                    row["to"] = st.text_input(
                        "Replace with (to)",
                        value=row.get("to", ""),
                        key=f"to_{idx}",
                    )
                    c1, c2 = st.columns(2)
                    with c1:
                        row["case_insensitive"] = st.checkbox(
                            "Case insensitive",
                            value=bool(row.get("case_insensitive", True)),
                            key=f"ci_{idx}",
                        )
                    with c2:
                        row["dedupe_lists"] = st.checkbox(
                            "Dedupe lists after replace",
                            value=bool(row.get("dedupe_lists", True)),
                            key=f"dd_{idx}",
                        )
                    if st.button("Remove rule", key=f"rm_{idx}"):
                        to_remove.append(idx)

                parsed_from = parse_from_values(str(row.get("from_text") or ""))
                active_field = (picked_field or "").strip()

                with col_values:
                    st.markdown("**Unique values in corpus**")
                    if not active_field:
                        st.info("Choose a field to load values from runs.")
                        row["from_text"] = "\n".join(parsed_from)
                    else:
                        all_literals = literals_by_field.get(active_field, [])
                        corpus_set = set(all_literals)
                        st.caption(f"{len(all_literals)} distinct values for `{active_field}`")
                        filter_text = st.text_input(
                            "Filter values",
                            value="",
                            key=f"lit_filter_{idx}",
                            placeholder="Type to narrow the list…",
                        )
                        if filter_text:
                            needle = filter_text.casefold()
                            shown = [v for v in all_literals if needle in v.casefold()]
                        else:
                            shown = list(all_literals)
                        shown.sort(key=str.casefold)

                        default_pick = [v for v in parsed_from if v in shown]
                        picked_literals = st.multiselect(
                            "Map these values (from)",
                            options=shown,
                            default=default_pick,
                            key=f"from_pick_{idx}",
                        )
                        orphans = [v for v in parsed_from if v not in corpus_set]
                        extra_key = f"from_extra_{idx}"
                        prev_field_key = f"prev_field_{idx}"
                        if st.session_state.get(prev_field_key) != active_field:
                            st.session_state[extra_key] = "\n".join(orphans)
                            st.session_state[prev_field_key] = active_field
                        elif extra_key not in st.session_state:
                            st.session_state[extra_key] = "\n".join(orphans)
                        extra_raw = st.text_area(
                            "Other from values (not listed above)",
                            height=88,
                            key=extra_key,
                            help="Values absent from the corpus scan; still included in the rule.",
                        )
                        merged = list(
                            dict.fromkeys(picked_literals + parse_from_values(extra_raw))
                        )
                        row["from_text"] = "\n".join(merged)
                        if merged:
                            st.markdown("**Active from list**")
                            st.code("\n".join(merged), language=None)

        if to_remove:
            st.session_state.rules_ui = [
                r for i, r in enumerate(st.session_state.rules_ui) if i not in to_remove
            ]
            st.rerun()

        st.divider()
        if st.button("Save rules to disk", type="primary"):
            new_doc = rules_to_document(doc, st.session_state.rules_ui)
            new_doc.setdefault("description", doc.get("description", ""))
            new_doc["version"] = int(doc.get("version", 1))
            new_doc["run_artifacts"] = doc.get("run_artifacts", [])
            if not cfg_path.parent.is_dir():
                st.error("Rules directory does not exist")
            else:
                save_config_document(new_doc, cfg_path)
                st.session_state.config_doc = new_doc
                schedule_raw_rules_json(new_doc)
                st.success(f"Saved {cfg_path}")

    with tab_json:
        flush_pending_raw_rules_json()

        st.subheader("Raw rules JSON")
        st.caption(
            "Edits here are kept in this tab until you save or sync. "
            "Use **Sync from Rules tab** after changing rules in the visual editor."
        )
        sync_col, _ = st.columns([1, 3])
        with sync_col:
            if st.button("Sync from Rules tab"):
                schedule_raw_rules_json(
                    rules_to_document(doc, st.session_state.rules_ui)
                )
                st.rerun()

        st.text_area(
            "harmonization_lexicon.json",
            height=420,
            key=RAW_RULES_JSON_KEY,
        )
        json_text = st.session_state[RAW_RULES_JSON_KEY]
        if st.button("Apply JSON to editor"):
            try:
                parsed = json.loads(json_text)
                st.session_state.config_doc = parsed
                st.session_state.rules_ui = document_to_rules_ui(parsed)
                schedule_raw_rules_json(parsed)
                st.session_state["_json_flash"] = "JSON loaded into Rules tab"
                st.rerun()
            except json.JSONDecodeError as exc:
                st.error(f"Invalid JSON: {exc}")
        if st.button("Save JSON to disk"):
            try:
                parsed = json.loads(json_text)
                save_config_document(parsed, cfg_path)
                st.session_state.config_doc = parsed
                st.session_state.rules_ui = document_to_rules_ui(parsed)
                schedule_raw_rules_json(parsed)
                st.session_state["_json_flash"] = f"Saved {cfg_path}"
                st.rerun()
            except json.JSONDecodeError as exc:
                st.error(f"Invalid JSON: {exc}")

        flash = st.session_state.pop("_json_flash", None)
        if flash:
            st.success(flash)

    run_filter = selected_runs if limit_runs and selected_runs else None

    with tab_preview:
        st.subheader("Dry run (no writes)")
        if not runs_path.is_dir():
            st.warning("Runs directory not found")
        elif not active_config().rules:
            st.info("Add at least one rule to preview changes")
        elif st.button("Scan runs", type="primary"):
            with st.spinner("Scanning…"):
                previews = preview_run_changes(
                    runs_path, active_config(), run_ids=run_filter
                )
            st.session_state.preview_rows = [
                {
                    "run_id": p.run_id,
                    "file": p.artifact,
                    "fields_updated": p.fields_updated,
                    "values_replaced": p.values_replaced,
                    "path": str(p.path),
                }
                for p in previews
            ]

        rows = st.session_state.get("preview_rows", [])
        if rows:
            df = pd.DataFrame(rows)
            st.metric("Files that would change", len(df))
            st.dataframe(
                df.drop(columns=["path"]),
                use_container_width=True,
                hide_index=True,
            )
            st.download_button(
                "Download preview CSV",
                df.to_csv(index=False).encode("utf-8"),
                file_name="field_replacement_preview.csv",
                mime="text/csv",
            )
        else:
            st.caption("Click **Scan runs** to list affected artifacts.")

    with tab_apply:
        st.subheader("Write changes to runs/")
        st.warning(
            "This overwrites JSON artifacts in place. "
            "Regenerate reports from OTSE (`refresh_reports.py`) afterward."
        )
        if not runs_path.is_dir():
            st.warning("Runs directory not found")
        elif not active_config().rules:
            st.info("Add at least one rule before applying")
        else:
            if st.button("Apply replacements", type="primary"):
                with st.spinner("Writing files…"):
                    stats = apply_to_runs(
                        runs_path,
                        active_config(),
                        dry_run=False,
                        run_ids=run_filter,
                    )
                reload_config(cfg_path if cfg_path.is_file() else None)
                st.success(
                    f"Updated **{stats.files_touched}** files · "
                    f"**{stats.fields_updated}** field nodes · "
                    f"**{stats.values_replaced}** replacement events"
                )


if __name__ == "__main__":
    main()
