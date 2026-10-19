"""Rebuild reports/ so it matches runs/ exactly.

Reports are derived artifacts, so any run whose JSON changed needs its HTML
rebuilt, and any report whose run is gone is stale and misleading. Both
generators read whatever files are present and skip the rest, so a run without
modes.json still produces a usable pipeline report.

Usage:
    python -m otse.scripts.refresh_reports --dry-run
    python -m otse.scripts.refresh_reports
"""

from __future__ import annotations

import argparse
from pathlib import Path

from otse.scripts.generate_modes_report import generate_modes_html
from otse.scripts.generate_report import generate_html

from otse.paths import REPORTS_DIR, RUNS_DIR


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-dir", type=Path, default=RUNS_DIR)
    parser.add_argument("--reports-dir", type=Path, default=REPORTS_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    runs = args.runs_dir
    reports = args.reports_dir
    tag = "  [DRY RUN]" if args.dry_run else ""

    if not runs.is_dir():
        parser.error(f"Runs directory not found: {runs}")
    run_ids = sorted(p.name for p in runs.iterdir() if p.is_dir())
    if not args.dry_run:
        reports.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("STALE REPORTS (run no longer present)" + tag)
    print("=" * 74)
    stale = 0
    for report in sorted(reports.glob("*.html")):
        run_id = report.stem.replace("_modes", "").replace("_pipeline", "")
        if run_id not in run_ids:
            print(f"  remove {report.name}")
            stale += 1
            if not args.dry_run:
                report.unlink()
    if not stale:
        print("  none")

    print()
    print("=" * 74)
    print("REBUILD" + tag)
    print("=" * 74)
    built = 0
    for run_id in run_ids:
        run_dir = runs / run_id
        has_modes = (run_dir / "modes.json").exists()
        note = "" if has_modes else "   (no modes.json — pipeline report only)"
        print(f"  {run_id}{note}")
        if args.dry_run:
            continue
        (reports / f"{run_id}_pipeline.html").write_text(
            generate_html(run_dir), encoding="utf-8")
        (reports / f"{run_id}_modes.html").write_text(
            generate_modes_html(run_dir), encoding="utf-8")
        built += 1

    print()
    print(f"removed {stale} stale, rebuilt {built} runs x 2 reports")


if __name__ == "__main__":
    main()
