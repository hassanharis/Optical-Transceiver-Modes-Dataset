#!/usr/bin/env python3
"""Apply the harmonization lexicon to OTSE run artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from otse.composition.field_replacer import (
    ReplacementConfig,
    apply_to_runs,
    default_config,
)
from otse.composition.loader import default_runs_dir


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Replace canonical field values in OTSE run JSON artifacts.",
    )
    parser.add_argument(
        "--runs-dir",
        type=Path,
        default=default_runs_dir(),
        help="OTSE runs directory (default: workspace/runs or TRANSCEIVER_RUNS_DIR)",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Rules file (default: dataset/harmonization_lexicon.json or OTSE_LEXICON_PATH)",
    )
    parser.add_argument(
        "--run-id",
        action="append",
        default=[],
        help="Limit to specific run folder name(s); repeatable",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files",
    )
    parser.add_argument(
        "--list-rules",
        action="store_true",
        help="Print loaded rules and exit",
    )
    args = parser.parse_args()

    config = (
        ReplacementConfig.load(args.config)
        if args.config
        else default_config()
    )

    if args.list_rules:
        print(f"Config version: {config.version}")
        print("Artifacts:", ", ".join(config.run_artifacts))
        for rule in config.rules:
            print(f"\n{rule.field} -> {rule.to!r}")
            print(f"  from: {', '.join(rule.from_values)}")
            print(f"  case_insensitive={rule.case_insensitive} dedupe_lists={rule.dedupe_lists}")
        return

    if not args.runs_dir.is_dir():
        print(f"Runs directory not found: {args.runs_dir}", file=sys.stderr)
        sys.exit(1)

    run_ids = args.run_id or None
    stats = apply_to_runs(
        args.runs_dir,
        config,
        dry_run=args.dry_run,
        run_ids=run_ids,
    )
    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(f"[{mode}] files updated: {stats.files_touched}")
    print(f"  field nodes changed: {stats.fields_updated}")
    print(f"  replacement events: {stats.values_replaced}")


if __name__ == "__main__":
    main()
