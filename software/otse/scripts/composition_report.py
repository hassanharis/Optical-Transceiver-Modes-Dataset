#!/usr/bin/env python3
"""CLI: print corpus composition summary (JSON or markdown)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from otse.composition.analytics import composition_overview, coverage_table, literal_counts
from otse.composition.fields import FieldKind, RecordLevel, discover_fields
from otse.composition.loader import default_runs_dir, iter_run_dirs, load_corpus


def main() -> None:
    parser = argparse.ArgumentParser(description="Transceiver corpus composition report")
    parser.add_argument(
        "--runs-dir",
        type=Path,
        default=default_runs_dir(),
        help="Path to runs/ directory",
    )
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--top", type=int, default=15, help="Top literals per categorical field")
    args = parser.parse_args()

    runs_dir = args.runs_dir
    total_runs = len(list(iter_run_dirs(runs_dir)))
    records = load_corpus(runs_dir)
    overview = composition_overview(records, total_run_folders=total_runs)
    fields = discover_fields(records)

    if args.format == "json":
        payload = {
            "overview": overview.__dict__,
            "top_literals": {},
            "coverage": coverage_table(
                records,
                [(f.name, f.level) for f in fields if f.kind != FieldKind.COMPLEX],
            ),
        }
        for f in fields:
            if f.kind not in (FieldKind.CATEGORICAL, FieldKind.BOOLEAN):
                continue
            counts = literal_counts(records, f.name, f.level, count_mode="module")
            payload["top_literals"][f"{f.level.value}.{f.name}"] = counts.most_common(args.top)
        print(json.dumps(payload, indent=2))
        return

    print("# Corpus composition\n")
    print(f"- Modules (deduped by source PDF): **{overview.n_modules}**")
    print(f"- Run folders on disk: **{overview.n_runs_total}**")
    print(f"- Mode records: **{overview.n_modes}**")
    print(f"- Validation passed: **{overview.validation_passed}** / {overview.n_modules}")
    if overview.page_count_median is not None:
        print(
            f"- Pages per datasheet: median **{overview.page_count_median}**, "
            f"mean **{overview.page_count_mean:.2f}**"
        )
    if overview.table_count_median is not None:
        print(
            f"- Tables per datasheet: median **{overview.table_count_median}**, "
            f"mean **{overview.table_count_mean:.2f}**"
        )
    print()

    print("## Top literals (per module)\n")
    for f in fields:
        if f.kind not in (FieldKind.CATEGORICAL, FieldKind.BOOLEAN):
            continue
        counts = literal_counts(records, f.name, f.level, count_mode="module")
        if not counts:
            continue
        print(f"### {f.level.value}: `{f.name}`\n")
        for lit, n in counts.most_common(args.top):
            pct = 100.0 * n / overview.n_modules
            print(f"- {lit}: {n} ({pct:.1f}%)")
        print()


if __name__ == "__main__":
    main()
