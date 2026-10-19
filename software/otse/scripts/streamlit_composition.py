"""
Streamlit explorer for transceiver datasheet corpus composition.

Run after installing OTSE:
    python -m otse.launch composition
"""

from __future__ import annotations

import io
from pathlib import Path

import pandas as pd
import streamlit as st

from otse.composition.analytics import (
    composition_overview,
    cross_tab,
    coverage_table,
    filter_records,
    literal_counts,
    numeric_summary,
)
from otse.composition.fields import (
    FieldKind,
    RecordLevel,
    discover_fields,
    field_literals,
    iter_field_values,
)
from otse.composition.loader import (
    default_runs_dir,
    iter_run_dirs,
    load_corpus,
    runs_corpus_version,
)

st.set_page_config(
    page_title="Transceiver corpus composition",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data(show_spinner="Loading corpus…")
def cached_load(runs_dir: str, corpus_version: int) -> tuple[list, int]:
    """``corpus_version`` must change when JSON on disk changes (see runs_corpus_version)."""
    path = Path(runs_dir)
    total = len(list(iter_run_dirs(path)))
    records = load_corpus(path)
    return records, total


def field_label(name: str, level: RecordLevel) -> str:
    return f"{level.value} · {name}"


def parse_field_label(label: str) -> tuple[str, RecordLevel]:
    level_s, name = label.split(" · ", 1)
    return name, RecordLevel(level_s)


def main() -> None:
    st.title("Transceiver datasheet corpus composition")
    st.caption("Dynamic field discovery and literal filters from extracted JSON runs.")

    with st.sidebar:
        st.header("Data")
        default = str(default_runs_dir())
        runs_dir = st.text_input("Runs directory", value=default)
        reload = st.button("Reload corpus")

    if reload:
        st.cache_data.clear()

    runs_path = Path(runs_dir)
    if not runs_path.is_dir():
        st.error(f"Runs directory not found: `{runs_dir}`")
        st.stop()

    corpus_version = runs_corpus_version(runs_path)
    with st.sidebar:
        st.caption(f"Corpus snapshot: v{corpus_version}")

    records, total_runs = cached_load(runs_dir, corpus_version)
    if not records:
        st.warning("No records found under runs/.")
        st.stop()

    all_fields = discover_fields(records)
    categorical = [
        f
        for f in all_fields
        if f.kind in (FieldKind.CATEGORICAL, FieldKind.BOOLEAN)
    ]
    numeric_fields = [f for f in all_fields if f.kind == FieldKind.NUMERIC]

    overview = composition_overview(records, total_run_folders=total_runs)

    with st.sidebar:
        st.header("Filters")
        st.caption("Multiselect literals per field (AND across fields). Options are discovered from data.")
        filter_field_labels = st.multiselect(
            "Fields to filter on",
            options=[field_label(f.name, f.level) for f in categorical],
            default=[],
        )
        count_mode = st.radio(
            "Count mode",
            options=["module", "mention"],
            format_func=lambda x: "Per datasheet (module)" if x == "module" else "Per mention (list elements)",
            horizontal=True,
        )

    filters: dict[tuple[str, RecordLevel], set[str]] = {}
    with st.sidebar:
        for label in filter_field_labels:
            name, level = parse_field_label(label)
            options = field_literals(records, name, level)
            if not options:
                continue
            selected = st.multiselect(label, options=options, default=[])
            if selected:
                filters[(name, level)] = set(selected)

    filtered = filter_records(records, filters)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Datasheets", f"{len(filtered)} / {overview.n_modules}")
    m2.metric("Mode records", sum(len(r.modes) for r in filtered))
    m3.metric("Run folders", total_runs)
    m4.metric("Validation OK", f"{overview.validation_passed} / {overview.n_modules}")

    tab_overview, tab_explorer, tab_coverage, tab_crosstab, tab_export = st.tabs(
        ["Overview", "Field explorer", "Coverage", "Cross-tab", "Export"]
    )

    with tab_overview:
        st.subheader("Document shape")
        st.write(
                        {
                            "page_count_median": overview.page_count_median,
                            "page_count_mean": overview.page_count_mean,
                            "table_count_median": overview.table_count_median,
                            "table_count_mean": overview.table_count_mean,
                            "modes_per_module_median": overview.modes_per_module_median,
                        }
                    )
        quick_fields = [
                        (f.name, f.level)
                        for f in categorical
                        if f.name in (
                            "vendor",
                            "form_factor",
                            "fiber_type",
                            "wavelength_band",
                            "modulation_format",
                            "standards_code",
                        )
                    ]

        charts = []

        for name, level in quick_fields:
            counts = literal_counts(filtered, name, level, count_mode="module")
            if counts:
                charts.append((name, level, counts))

        columns = st.columns(2)
        midpoint = (len(charts) + 1) // 2

        for i, (name, level, counts) in enumerate(charts):
            column = columns[0] if i < midpoint else columns[1]

            with column:
                df = pd.DataFrame(
                    [
                        {
                            "literal": k,
                            "modules": v,
                            "pct": 100 * v / len(filtered),
                        }
                        for k, v in counts.most_common(12)
                    ]
                )

                with st.expander(
                    field_label(name, level),
                    
                    expanded=True,
                ):
                    st.bar_chart(df.set_index("literal")["modules"])
        
        
       

    with tab_explorer:
        st.subheader("Explore any field")
        col_a, col_b = st.columns([2, 1])
        with col_a:
            explorer_label = st.selectbox(
                "Field",
                options=[field_label(f.name, f.level) for f in all_fields if f.kind != FieldKind.COMPLEX],
                index=0,
            )
        name, level = parse_field_label(explorer_label)
        info = next((f for f in all_fields if f.name == name and f.level == level), None)

        with col_b:
            if info:
                st.write(f"Kind: **{info.kind.value}** · literals: **{info.literal_count}**")

        if info and info.kind == FieldKind.NUMERIC:
            stats = numeric_summary(filtered, name, level)
            st.json(stats)
            values: list[float] = []
            for rec in filtered:
                for raw in iter_field_values(rec, name, level):
                    if isinstance(raw, (int, float)) and not isinstance(raw, bool):
                        values.append(float(raw))
                    elif isinstance(raw, list):
                        for item in raw:
                            if isinstance(item, (int, float)) and not isinstance(item, bool):
                                values.append(float(item))
            if values:
                st.line_chart(pd.Series(values).value_counts(bins=min(30, len(set(values)))).sort_index())
        else:
            literal_filter = st.multiselect(
                "Show only these literals (optional)",
                options=field_literals(filtered, name, level),
                default=[],
            )
            counts = literal_counts(filtered, name, level, count_mode=count_mode)
            rows = []
            for lit, n in counts.most_common():
                if literal_filter and lit not in literal_filter:
                    continue
                denom = len(filtered) if count_mode == "module" else sum(counts.values())
                rows.append(
                    {
                        "literal": lit,
                        "count": n,
                        "pct": round(100.0 * n / denom, 2) if denom else 0.0,
                    }
                )
            df = pd.DataFrame(rows)
            if df.empty:
                st.info("No values for this field in the filtered corpus.")
            else:
                st.dataframe(df, use_container_width=True, hide_index=True)
                st.bar_chart(df.set_index("literal")["count"].head(25))

    with tab_coverage:
        st.subheader("Field completeness (% datasheets with a non-empty value)")
        cov_fields = [(f.name, f.level) for f in all_fields if f.kind != FieldKind.COMPLEX]
        cov = coverage_table(filtered, cov_fields)
        cov_df = pd.DataFrame(cov).sort_values("coverage_pct", ascending=False)
        st.dataframe(cov_df, use_container_width=True, hide_index=True)
        st.bar_chart(cov_df.set_index("field")["coverage_pct"].head(30))

    with tab_crosstab:
        st.subheader("Two-field pivot (top literals)")
        cat_labels = [field_label(f.name, f.level) for f in categorical]
        if len(cat_labels) < 2:
            st.info("Need at least two categorical fields.")
        else:
            a_label = st.selectbox("Row field", cat_labels, index=cat_labels.index("module · form_factor") if "module · form_factor" in cat_labels else 0)
            b_label = st.selectbox("Column field", cat_labels, index=cat_labels.index("module · vendor") if "module · vendor" in cat_labels else 1)
            fa, la = parse_field_label(a_label)
            fb, lb = parse_field_label(b_label)
            rows, cols, matrix = cross_tab(
                filtered,
                fa,
                la,
                fb,
                lb,
                count_mode=count_mode,
            )
            pivot = pd.DataFrame(matrix, index=rows, columns=cols)
            st.dataframe(pivot, use_container_width=True)

    with tab_export:
        st.subheader("Tables for the paper")
        export_field = st.selectbox(
            "Composition table field",
            options=[field_label(f.name, f.level) for f in categorical],
            index=next(
                (i for i, f in enumerate(categorical) if f.name == "fiber_type"),
                0,
            ),
        )
        en, el = parse_field_label(export_field)
        top_n = st.slider("Top N literals", 5, 40, 15)
        counts = literal_counts(filtered, en, el, count_mode="module")
        export_df = pd.DataFrame(
            [
                {"literal": k, "modules": v, "pct": round(100.0 * v / len(filtered), 2)}
                for k, v in counts.most_common(top_n)
            ]
        )
        st.dataframe(export_df, use_container_width=True, hide_index=True)

        csv = export_df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, file_name=f"composition_{en}.csv", mime="text/csv")

        latex = export_df.to_latex(index=False, caption=f"Corpus composition by {en}.", label=f"tab:{en}")
        st.code(latex, language="latex")

        md_lines = [
            f"| {en} | modules | % |",
            "|---|---:|---:|",
        ]
        for _, row in export_df.iterrows():
            md_lines.append(f"| {row['literal']} | {int(row['modules'])} | {row['pct']:.1f} |")
        st.download_button(
            "Download Markdown",
            "\n".join(md_lines).encode("utf-8"),
            file_name=f"composition_{en}.md",
            mime="text/markdown",
        )

        if st.button("Build multi-field coverage CSV"):
            cov = pd.DataFrame(coverage_table(filtered, [(f.name, f.level) for f in all_fields if f.kind != FieldKind.COMPLEX]))
            buf = io.BytesIO()
            cov.to_csv(buf, index=False)
            st.download_button(
                "Download coverage table",
                buf.getvalue(),
                file_name="field_coverage.csv",
                mime="text/csv",
            )


if __name__ == "__main__":
    main()
