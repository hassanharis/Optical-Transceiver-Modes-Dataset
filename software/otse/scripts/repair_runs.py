"""Recover runs whose specs.json was never written.

Three runs finished extraction and mode synthesis but failed Pydantic validation,
so `store_run` skipped specs.json and everything downstream (M1, M2, Eval) treats
them as empty. The raw LLM output is still on disk, so the records are recoverable:
coerce, validate against the current schema, and store.

A fourth run (Nokia) has valid specs but no mode artifacts, because mode synthesis
returned no content. `separate_atoms` is pure code, so mode_atoms.json can be
rebuilt here; modes.json needs the model and is left for a re-run.

Usage:
    python -m otse.scripts.repair_runs --dry-run
    python -m otse.scripts.repair_runs
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from otse.pipeline.atom_extractor import _coerce_types
from otse.pipeline.mode_linker import separate_atoms
from otse.pipeline.runtime_store import store_specs
from otse.transceiver_models import TransceiverSpecs
from otse.paths import RUNS_DIR

RUNS = RUNS_DIR

# Runs that have raw_llm.json but no specs.json.
NEEDS_SPECS = ["20260819_171811", "20260821_095641", "20260821_104901"]

# Runs that have specs.json but no mode_atoms.json / modes.json.
NEEDS_MODE_ATOMS = ["20260821_121218"]

# Fields whose declared type changed from scalar to list; existing specs.json
# files written before the change may still hold a bare number.
RETYPED = ("extinction_ratio_db", "los_assert_dbm", "los_deassert_dbm")


def repair_specs(run_id: str, dry_run: bool) -> bool:
    run_dir = RUNS / run_id
    raw_path = run_dir / "raw_llm.json"
    if not raw_path.exists():
        print(f"  {run_id}: no raw_llm.json — cannot repair")
        return False
    if (run_dir / "specs.json").exists():
        print(f"  {run_id}: specs.json already present — skipping")
        return False

    raw = json.loads(raw_path.read_text(encoding="utf-8"))
    coerced = _coerce_types(dict(raw))
    try:
        specs = TransceiverSpecs.model_validate(coerced)
    except Exception as exc:
        errors = getattr(exc, "errors", None)
        print(f"  {run_id}: STILL INVALID")
        if callable(errors):
            for err in errors():
                loc = ".".join(str(x) for x in err.get("loc", ()))
                print(f"      {loc}: {err.get('msg')}  input={err.get('input')!r}")
        return False

    populated = sum(1 for v in specs.model_dump(exclude_none=True).values() if v not in (None, [], ""))
    print(f"  {run_id}: validates -> {populated} populated fields", end="")
    if dry_run:
        print("  [dry-run, not written]")
        return True
    store_specs(run_dir, specs)
    print("  -> specs.json written, validation_passed=True")
    return True


def repair_mode_atoms(run_id: str, dry_run: bool) -> bool:
    run_dir = RUNS / run_id
    specs_path = run_dir / "specs.json"
    if not specs_path.exists():
        print(f"  {run_id}: no specs.json — cannot derive atoms")
        return False
    if (run_dir / "mode_atoms.json").exists():
        print(f"  {run_id}: mode_atoms.json already present — skipping")
        return False

    specs_dict = json.loads(specs_path.read_text(encoding="utf-8"))
    multi, general = separate_atoms(specs_dict)
    print(f"  {run_id}: {len(multi)} multi-valued mode fields, {len(general)} general", end="")
    if dry_run:
        print("  [dry-run, not written]")
        return True
    (run_dir / "mode_atoms.json").write_text(
        json.dumps({"multi_valued": multi, "general": general}, indent=2), encoding="utf-8"
    )
    print("  -> mode_atoms.json written (modes.json still needs a model run)")
    return True


def report_retyped() -> None:
    """List specs.json files holding a bare number in a now-list field."""
    hits = []
    for run_dir in sorted(p for p in RUNS.iterdir() if p.is_dir()):
        path = run_dir / "specs.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        scalars = {f: data[f] for f in RETYPED
                   if f in data and data[f] is not None and not isinstance(data[f], list)}
        if scalars:
            hits.append((run_dir.name, scalars))
    if not hits:
        print("  none — no stored record holds a bare number in a retyped field")
        return
    for name, scalars in hits:
        print(f"  {name}: {scalars}")
    print("  (left as-is: readers coerce on load, and rewriting would edit stored evidence)")


def main() -> None:
    global RUNS
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs-dir", type=Path, default=RUNS_DIR)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    RUNS = args.runs_dir

    print("=" * 78)
    print("REPAIR: specs.json from raw LLM output" + ("  [DRY RUN]" if args.dry_run else ""))
    print("=" * 78)
    recovered = sum(repair_specs(r, args.dry_run) for r in NEEDS_SPECS)

    print()
    print("=" * 78)
    print("REPAIR: mode_atoms.json from stored specs")
    print("=" * 78)
    atoms = sum(repair_mode_atoms(r, args.dry_run) for r in NEEDS_MODE_ATOMS)

    print()
    print("=" * 78)
    print("AUDIT: records predating the scalar-to-list field change")
    print("=" * 78)
    report_retyped()

    print()
    print(f"specs.json recovered: {recovered}/{len(NEEDS_SPECS)}")
    print(f"mode_atoms.json rebuilt: {atoms}/{len(NEEDS_MODE_ATOMS)}")


if __name__ == "__main__":
    main()
