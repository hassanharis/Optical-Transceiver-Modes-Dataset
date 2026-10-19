"""Remove duplicate runs from the run store.

Duplicates were found by SHA-256 of content.md: identical parsed text means the
same PDF was processed twice. `source_file` in meta.json is a Streamlit temp path
and cannot be used for this.

Two dispositions:

DELETE  — the run carries nothing the surviving run does not. Incomplete pipelines
          and strictly worse extractions of the same PDF.
ARCHIVE — the run is a duplicate for corpus-counting purposes, so it must leave
          runs/, but it records a measurement that cannot be reconstructed from
          what remains. Moved to runs_archive/.

Run IDs referenced by Eval/gold/gold_routing.csv are refused outright: deleting
one silently drops rows from the gold set.

Usage:
    python -m otse.scripts.cleanup_runs --dry-run
    python -m otse.scripts.cleanup_runs
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from otse.paths import ARCHIVE_DIR, RUNS_DIR

RUNS = RUNS_DIR
ARCHIVE = ARCHIVE_DIR

# Keyed to the run that supersedes each one.
DELETE = {
    "20260817_094709": "duplicate of 20260807_123953 (SO-TQSFPDD4CCZRP); "
                       "extraction only, no mode_atoms/modes/raw_llm",
    "20260817_171841": "duplicate of 20260807_141342 (TQD017-TUNC-SO); "
                       "synthesis ran 423s but modes.json never written",
    "20260821_112237": "duplicate of 20260821_121218 (Nokia); the survivor also "
                       "kept raw_llm_modes_response.json",
    "20260821_133324": "duplicate of 20260821_133838 (Avago); abandoned before "
                       "mode synthesis",
    "20260813_085001": "duplicate of 20260810_163700 (TD8005-TUNC-SO); same five "
                       "code points, coarser labels, 65 vs 70 cells, 2.4x slower",
}

ARCHIVE_ONLY = {
    "20260817_095458": "only non-Qwen run (Nemotron-14B) — 9 degenerate modes vs "
                       "14 identified by Qwen3.6 on identical text; evidences the "
                       "model choice",
    "20260821_083817": "same PDF text and model as 20260821_090655 but an "
                       "incompatible decomposition (6 modes vs 12); the only "
                       "measured mode-synthesis non-determinism instance",
}

# From Eval/gold/gold_routing.csv — the 62 gold modes are keyed to these.
GOLD_RUNS = {
    "20260807_123953", "20260807_141342", "20260810_153827", "20260810_163700",
    "20260810_165202", "20260810_171058", "20260810_183943",
}


def main() -> None:
    global RUNS, ARCHIVE
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-dir", type=Path, default=RUNS_DIR)
    parser.add_argument("--archive-dir", type=Path, default=ARCHIVE_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    RUNS = args.runs_dir
    ARCHIVE = args.archive_dir
    tag = "  [DRY RUN]" if args.dry_run else ""

    protected = (set(DELETE) | set(ARCHIVE_ONLY)) & GOLD_RUNS
    if protected:
        raise SystemExit(f"refusing to touch gold-set runs: {sorted(protected)}")

    print("=" * 78)
    print("DELETE" + tag)
    print("=" * 78)
    deleted = 0
    for run_id, reason in DELETE.items():
        path = RUNS / run_id
        if not path.exists():
            print(f"  {run_id}: already gone")
            continue
        size = sum(f.stat().st_size for f in path.rglob("*") if f.is_file())
        print(f"  {run_id}  ({size // 1024} KB)\n      {reason}")
        if not args.dry_run:
            shutil.rmtree(path)
            deleted += 1

    print()
    print("=" * 78)
    print("ARCHIVE -> runs_archive/" + tag)
    print("=" * 78)
    archived = 0
    for run_id, reason in ARCHIVE_ONLY.items():
        path = RUNS / run_id
        if not path.exists():
            print(f"  {run_id}: already moved")
            continue
        print(f"  {run_id}\n      {reason}")
        if not args.dry_run:
            ARCHIVE.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(ARCHIVE / run_id))
            archived += 1

    print()
    remaining = sorted(p.name for p in RUNS.iterdir() if p.is_dir())
    print(f"deleted {deleted}, archived {archived}, {len(remaining)} runs remain")


if __name__ == "__main__":
    main()
