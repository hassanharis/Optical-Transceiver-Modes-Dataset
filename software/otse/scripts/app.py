"""Streamlit UI for the transceiver datasheet extraction pipeline.

Uses a local OpenAI-compatible llama-server endpoint.
"""

import json
import os
import tempfile
import time
from pathlib import Path

import requests
import streamlit as st
from openai import OpenAI
from pydantic import ValidationError

from otse.scripts.export_all_modes import collect_mode_rows, write_csv
from otse.pipeline.pdf_parser import parse_pdf
from otse.pipeline.atom_extractor import extract_atoms, BASE_URL
import re
from otse.pipeline.mode_linker import synthesize_modes, store_modes, separate_atoms, _filter_sections_by_provenance
from otse.pipeline.runtime_store import (
    list_runs,
    load_run,
    store_specs,
    store_run,
    update_run_timings,
)
from otse.scripts.generate_report import generate_html
from otse.scripts.generate_modes_report import generate_modes_html
from otse.transceiver_models import TransceiverSpecs

from otse.paths import MODEL_DIR, REPORTS_DIR, RUNS_DIR, WORKSPACE_DIR

ALL_MODES_CSV = WORKSPACE_DIR / "all_modes.csv"
ALL_MODES_JSON = WORKSPACE_DIR / "all_modes.json"

st.set_page_config(page_title="Transceiver Spec Extractor", layout="wide")
st.title("Transceiver Datasheet Extractor")


# --------------------------------------------------------------------------- #
# Server / model helpers (from Chatbot/llm.py pattern)
# --------------------------------------------------------------------------- #

def _server_up() -> bool:
    try:
        return requests.get(f"{BASE_URL}/health", timeout=5).ok
    except requests.RequestException:
        return False


def _list_models() -> list[str]:
    resp = requests.get(f"{BASE_URL}/v1/models", timeout=15)
    resp.raise_for_status()
    return [m["id"] for m in resp.json().get("data", [])]


def _disk_sizes() -> dict[str, float]:
    sizes: dict[str, float] = {}
    if not os.path.isdir(MODEL_DIR):
        return sizes
    for entry in os.scandir(MODEL_DIR):
        if entry.is_file() and entry.name.lower().endswith(".gguf"):
            sizes[os.path.splitext(entry.name)[0]] = entry.stat().st_size / 1024**3
    return sizes

def markdown_sections(markdown: str) -> list[tuple[str, int, int]]:
    matches = list(re.finditer(r"(?m)^#{1,6}\s+(.+)$", markdown))
    if not matches:
        return [("Document", 0, len(markdown))]

    sections = []
    if matches[0].start() > 0:
        sections.append(("Document introduction", 0, matches[0].start()))

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        sections.append((match.group(1).strip(), match.start(), end))

    return sections


def clean_markdown(markdown: str) -> str:

    markdown = re.sub(
        r"(?m)^[^\r\n]*==> picture[^\r\n]*(?:\r?\n|$)",
        "",
        markdown,
    )
    return markdown

def replace_editor_text() -> None:
    old = st.session_state.get("replace_text", "")
    new = st.session_state.get("replacement_text", "")

    if old:
        current = st.session_state.get("md_editor", "")
        st.session_state["md_editor"] = current.replace(old, new)
# --------------------------------------------------------------------------- #
# Sidebar: server status + model picker
# --------------------------------------------------------------------------- #

with st.sidebar:
    st.header("LLM Server")

    model_id = None
    if not _server_up():
        st.error(
            "llama-server router is not reachable on port 8080.\n\n"
            f'Start it with:\n```\nllama-server --models-dir "{MODEL_DIR}" --models-max 1\n```'
        )
    else:
        st.success("Server online")
        models = _list_models()
        if not models:
            st.error(f"No models found. Place GGUF files in {MODEL_DIR}")
        else:
            sizes = _disk_sizes()
            labels = [f"{m}  ({sizes[m]:.1f} GB)" if m in sizes else m for m in models]
            choice = st.selectbox("Model", labels)
            model_id = models[labels.index(choice)]

    st.divider()
    st.header("Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.1, 0.05)
    max_tokens = st.slider("Max tokens", 2048, 32768, 16384, 1024)
    st.caption("Thinking models need high token budgets")

# --------------------------------------------------------------------------- #
# Main area
# --------------------------------------------------------------------------- #

tab_extract, tab_history, tab_all_modes = st.tabs(["Extract", "History", "All Modes"])

with tab_extract:
    uploaded = st.file_uploader("Upload a PDF datasheet", type=["pdf"])

    # --- Step 1: Parse PDF ---
    if uploaded:
        file_key = uploaded.name + str(uploaded.size)
        if st.session_state.get("_parse_key") != file_key:
            st.session_state.pop("parsed", None)
            st.session_state.pop("edited_md", None)
            st.session_state.pop("extraction_result", None)
            st.session_state.pop("timings_seconds", None)
            st.session_state.pop("current_specs", None)
            st.session_state.pop("modes_result", None)

        if st.button("Parse PDF", type="secondary"):
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                tmp.write(uploaded.read())
                tmp_path = Path(tmp.name)
            with st.spinner("Parsing..."):
                stage_started = time.perf_counter()
                parsed = parse_pdf(tmp_path)
                parse_seconds = time.perf_counter() - stage_started
            st.session_state["parsed"] = parsed
            st.session_state["edited_md"] = parsed.markdown
            st.session_state["timings_seconds"] = {"parse_pdf": parse_seconds}
            st.session_state["_parse_key"] = file_key
            st.session_state.pop("extraction_result", None)
            st.success(f"PDF parsed in {parse_seconds:.3f} seconds")

    # --- Step 2: Review / edit parsed markdown ---
    if "parsed" in st.session_state:
        parsed = st.session_state["parsed"]
        st.subheader("Step 1 — Parsed Content")

        full_md = st.session_state.get("edited_md", parsed.markdown)
        full_md = clean_markdown(full_md)



        sections = markdown_sections(full_md)
        st.caption(f"{parsed.page_count} pages | {len(parsed.tables)} tables | {len(sections)} sections | {len(parsed.markdown):,} chars")

        nav_col, editor_col, preview_col = st.columns([1, 2, 2])
        headings = [re.sub(r"^#{1,6}\s+", "", line.strip()) for line in full_md.splitlines() if re.match(r"^#{1,6}\s+", line)]

        with nav_col:
            with st.expander(f"Identified Headings ({len(headings)})"):
                if headings:
                    for h in headings:
                        st.write(f"- {h}")
                else:
                    st.caption("No headings found")


        with editor_col:
            edited_md = st.text_area(
                "Edit the markdown before extraction",
                value=full_md,
                height=500,
                key="md_editor",
            )

        with preview_col:
            st.markdown("**Markdown Preview**")
            with st.container(height=500, border=True):
                st.markdown(edited_md)

        st.session_state["edited_md"] = edited_md


        replace_col, with_col, button_col = st.columns([2, 2, 1])

        with replace_col:
            st.text_input("Replace", key="replace_text")

        with with_col:
            st.text_input("With", key="replacement_text")

        with button_col:
            st.button(
                "Replace all",
                on_click=replace_editor_text,
                use_container_width=True,
            )


        # Show provenance-filtered content after extraction
        if "extraction_result" in st.session_state:
            ex_specs, ex_raw = st.session_state["extraction_result"]
            ex_data = st.session_state.get("current_specs") or (
                json.loads(ex_specs.model_dump_json()) if ex_specs else ex_raw
            )
            provenance = ex_data.get("provenance_datasheet_sections")
            if provenance and isinstance(provenance, (str, list)):
                filtered_md = _filter_sections_by_provenance(edited_md, provenance)
                prov_headings = len([line for line in filtered_md.splitlines() if re.match(r"^#{1,6}\s+", line)])
                with st.expander(f"Provenance Sections ({len(filtered_md):,} chars · {prov_headings} sections)", expanded=False):
                    st.text_area(
                        "Filtered content (read-only)",
                        value=filtered_md,
                        height=400,
                        disabled=True,
                        key="provenance_viewer",
                        label_visibility="collapsed",
                    )

        # --- Step 3: Extract ---
        if st.button("Extract Parameters", type="primary", disabled=model_id is None):
            # Patch the parsed object with edited markdown
            parsed.markdown = st.session_state["edited_md"]

            with st.status("Extracting...", expanded=True) as status:
                st.write(f"Sending to `{model_id}` ({len(parsed.markdown):,} chars)...")
                stage_started = time.perf_counter()
                specs, raw_dict = extract_atoms(
                    parsed,
                    model_id=model_id,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                extract_seconds = time.perf_counter() - stage_started
                timings = dict(st.session_state.get("timings_seconds", {}))
                timings["extract_atoms"] = extract_seconds
                st.write(f"Extraction completed in {extract_seconds:.3f} seconds")

                st.write("Storing run...")
                stage_started = time.perf_counter()
                run_dir = store_run(
                    parsed,
                    raw_dict,
                    specs,
                    model_id=model_id,
                    timings_seconds=timings,
                )
                timings["store_run"] = time.perf_counter() - stage_started
                timings["total"] = sum(
                    seconds for name, seconds in timings.items() if name != "total"
                )
                update_run_timings(run_dir, timings)

                # Persist content & provenance stats into meta
                result_data = json.loads(specs.model_dump_json()) if specs else raw_dict
                md_text = st.session_state["edited_md"]
                all_headings = [l for l in md_text.splitlines() if re.match(r"^#{1,6}\s+", l)]
                prov = result_data.get("provenance_datasheet_sections")
                if prov and isinstance(prov, (str, list)):
                    filt = _filter_sections_by_provenance(md_text, prov)
                    prov_headings = [l for l in filt.splitlines() if re.match(r"^#{1,6}\s+", l)]
                else:
                    filt = md_text
                    prov_headings = all_headings
                content_stats = {
                    "content_chars": len(md_text),
                    "content_headings": len(all_headings),
                    "provenance_chars": len(filt),
                    "provenance_headings": len(prov_headings),
                }
                meta_path = run_dir / "meta.json"
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
                meta["content_stats"] = content_stats
                meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")

                st.session_state["timings_seconds"] = timings
                st.session_state["_last_run_dir"] = str(run_dir)
                st.write(f"Saved to `{run_dir}` in {timings['store_run']:.3f} seconds")
                st.write(f"Total processing time: {timings['total']:.3f} seconds")

                if specs:
                    status.update(label="Extraction complete", state="complete")
                else:
                    status.update(label="Extraction complete (validation failed)", state="error")

            st.session_state["extraction_result"] = (specs, raw_dict)
            st.session_state.pop("modes_result", None)
            st.session_state.pop("current_specs", None)

    # --- Display results ---
    if "extraction_result" in st.session_state:
        specs, raw_dict = st.session_state["extraction_result"]
        run_dir = Path(st.session_state["_last_run_dir"])

        # Use saved edits if available, otherwise the extraction output
        display_data = st.session_state.get("current_specs") or (
            json.loads(specs.model_dump_json()) if specs else raw_dict
        )

        st.subheader("Extracted Parameters")
        col1, col2, col3 = st.columns(3)
        scalar_fields = {}
        list_fields = {}
        null_fields = []
        for k, v in display_data.items():
            if v is None:
                null_fields.append(k)
            elif isinstance(v, list) and len(v) > 1:
                list_fields[k] = v
            else:
                scalar_fields[k] = v

        with col1:
            st.markdown("**Scalar Values**")
            for k, v in scalar_fields.items():
                st.write(f"- **{k}:** {v}")
        with col2:
            st.markdown("**List Values**")
            for k, v in list_fields.items():
                if k == "penalties":
                    st.write(f"- **{k}:** ({len(v)} entries)")
                    with st.expander("View Penalties"):
                        st.json(v)
                else:
                    st.write(f"- **{k}:** {v}")
        with col3:
            st.markdown("**Not Found (null)**")
            for k in null_fields:
                st.write(f"- {k}")

        with st.expander("Edit Parameters (JSON)"):
            editor_key = f"review_editor_{run_dir.name}"
            edited_specs_json = st.text_area(
                "Parameters (JSON)",
                value=json.dumps(display_data, indent=2),
                height=600,
                key=editor_key,
                label_visibility="collapsed",
            )
            if st.button("Save Changes"):
                try:
                    edited_data = json.loads(edited_specs_json)
                    if not isinstance(edited_data, dict):
                        raise ValueError("Parameters must be a JSON object.")
                    validated = TransceiverSpecs.model_validate(edited_data)
                    saved = store_specs(run_dir, validated)
                    st.session_state["current_specs"] = saved
                    st.success("Changes saved to specs.json.")
                    st.rerun()
                except (json.JSONDecodeError, ValidationError, ValueError) as exc:
                    st.error(f"Could not save: {exc}")

        # --- Step 4: Mode Synthesis ---
        st.divider()
        st.subheader("Step 2 — Mode Synthesis")
        if st.button("Synthesize Modes", type="primary", disabled=model_id is None):
            source = display_data
            multi, general = separate_atoms(source)
            st.session_state.pop("modes_result", None)

            if multi:
                st.caption(f"{len(multi)} multi-valued fields to link into modes")
                with st.expander("Multi-valued atoms"):
                    st.json(multi)

            with st.status("Linking atoms into modes...", expanded=True) as status:
                stage_started = time.perf_counter()
                modes_result, _, _ = synthesize_modes(
                    source,
                    st.session_state["parsed"],
                    run_dir=run_dir,
                    model_id=model_id,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                mode_seconds = time.perf_counter() - stage_started
                timings = dict(st.session_state.get("timings_seconds", {}))
                timings["synthesize_modes"] = mode_seconds
                st.write(f"Mode synthesis completed in {mode_seconds:.3f} seconds")
                if modes_result:
                    stage_started = time.perf_counter()
                    store_modes(run_dir, modes_result, multi, general)
                    timings["store_modes"] = time.perf_counter() - stage_started
                    st.write(f"Modes saved in {timings['store_modes']:.3f} seconds")
                    status.update(label=f"{len(modes_result.get('modes', []))} modes identified", state="complete")
                else:
                    status.update(label="Mode synthesis failed", state="error")

                timings["total"] = sum(
                    seconds for name, seconds in timings.items() if name != "total"
                )
                update_run_timings(run_dir, timings)
                st.session_state["timings_seconds"] = timings

            st.session_state["modes_result"] = modes_result

        # --- Generate Report button (after mode synthesis) ---
        if st.session_state.get("modes_result"):
            run_dir = Path(st.session_state["_last_run_dir"])
            if st.button("Generate Report", type="secondary"):
                REPORTS_DIR.mkdir(parents=True, exist_ok=True)
                pipeline_path = REPORTS_DIR / f"{run_dir.name}_pipeline.html"
                html = generate_html(run_dir)
                pipeline_path.write_text(html, encoding="utf-8")
                modes_path = REPORTS_DIR / f"{run_dir.name}_modes.html"
                modes_html = generate_modes_html(run_dir)
                modes_path.write_text(modes_html, encoding="utf-8")
                st.success(f"Reports saved: `{pipeline_path}` and `{modes_path}`")

            modes_result = st.session_state["modes_result"]
            with st.expander("Raw LLM Mode Output"):
                st.json(modes_result)
            st.subheader("Configuration Modes")
            for i, mode in enumerate(modes_result.get("modes", [])):
                label = mode.get("label", f"Mode {i+1}")
                with st.expander(f"**{label}**", expanded=i == 0):
                    st.json(mode)

with tab_history:
    runs = list_runs()
    if not runs:
        st.info("No runs yet.")
    else:
        selected = st.selectbox("Select a run", [r.name for r in reversed(runs)])
        if selected:
            run_data = load_run(RUNS_DIR / selected)
            if "meta" in run_data:
                st.json(run_data["meta"])
            if "specs" in run_data:
                st.subheader("Validated Specs")
                st.json(run_data["specs"])
            elif "raw_llm" in run_data:
                st.subheader("Raw LLM Output (no validated specs)")
                st.json(run_data["raw_llm"])
            if "raw_llm_modes_response" in run_data:
                with st.expander("Raw Mode LLM Response"):
                    st.json(run_data["raw_llm_modes_response"])
            if "raw_llm_modes" in run_data:
                with st.expander("Raw LLM Mode Output"):
                    st.json(run_data["raw_llm_modes"])

            if st.button("Generate Report", key="hist_report"):
                REPORTS_DIR.mkdir(parents=True, exist_ok=True)
                sel_run_dir = RUNS_DIR / selected
                pipeline_path = REPORTS_DIR / f"{selected}_pipeline.html"
                html = generate_html(sel_run_dir)
                pipeline_path.write_text(html, encoding="utf-8")
                modes_path = REPORTS_DIR / f"{selected}_modes.html"
                modes_html = generate_modes_html(sel_run_dir)
                modes_path.write_text(modes_html, encoding="utf-8")
                st.success(f"Reports saved: `{pipeline_path}` and `{modes_path}`")

with tab_all_modes:
    st.subheader("All Operating Modes")
    st.caption(
        "One row per mode, with its run ID and the module parameters repeated "
        "for every mode in that run."
    )

    if "all_modes_rows" not in st.session_state:
        rows, warnings = collect_mode_rows(RUNS_DIR)
        st.session_state["all_modes_rows"] = rows
        st.session_state["all_modes_warnings"] = warnings

    if st.button("Refresh modes", type="primary", key="refresh_all_modes"):
        rows, warnings = collect_mode_rows(RUNS_DIR)
        st.session_state["all_modes_rows"] = rows
        st.session_state["all_modes_warnings"] = warnings
        if rows:
            write_csv(rows, ALL_MODES_CSV)
            ALL_MODES_JSON.write_text(
                json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            st.success(f"Refreshed {len(rows)} modes from {len(set(row['run_id'] for row in rows))} runs.")
        else:
            st.warning("No synthesized modes were found in the runs folder.")

    all_modes_rows = st.session_state["all_modes_rows"]
    all_modes_warnings = st.session_state["all_modes_warnings"]

    if all_modes_rows:
        metric_modes, metric_runs, metric_fields = st.columns(3)
        metric_modes.metric("Modes", len(all_modes_rows))
        metric_runs.metric("Runs", len({row["run_id"] for row in all_modes_rows}))
        metric_fields.metric("Fields", len({key for row in all_modes_rows for key in row}))

        display_rows = [
            {
                key: json.dumps(value, ensure_ascii=False)
                if isinstance(value, (list, dict))
                else value
                for key, value in row.items()
            }
            for row in all_modes_rows
        ]
        st.dataframe(display_rows, use_container_width=True, hide_index=True)

        csv_ready = ALL_MODES_CSV.exists()
        json_ready = ALL_MODES_JSON.exists()
        download_csv, download_json = st.columns(2)
        with download_csv:
            st.download_button(
                "Download CSV",
                data=ALL_MODES_CSV.read_bytes() if csv_ready else b"",
                file_name=ALL_MODES_CSV.name,
                mime="text/csv",
                disabled=not csv_ready,
                use_container_width=True,
            )
        with download_json:
            st.download_button(
                "Download JSON",
                data=ALL_MODES_JSON.read_bytes() if json_ready else b"",
                file_name=ALL_MODES_JSON.name,
                mime="application/json",
                disabled=not json_ready,
                use_container_width=True,
            )

    for warning in all_modes_warnings:
        st.warning(warning)
