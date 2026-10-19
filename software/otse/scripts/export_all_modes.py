"""Export all synthesized operating modes from runs/ to one flat CSV file.

Each row represents one mode. Run-level module/general parameters are repeated
on every row for that run, while mode-specific values take precedence when a
field appears in both sources.

Usage:
    python -m otse.scripts.export_all_modes
    python -m otse.scripts.export_all_modes --runs-dir runs --output all_modes.csv
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from otse.paths import RUNS_DIR, WORKSPACE_DIR

DEFAULT_RUNS_DIR = RUNS_DIR
DEFAULT_OUTPUT = WORKSPACE_DIR / "all_modes.csv"


def _load_json(path: Path) -> Any | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"warning: could not read {path}: {exc}")
        return None


def _mode_list(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        value = value.get("modes", [])
    if not isinstance(value, list):
        return []
    return [mode for mode in value if isinstance(mode, dict)]


def collect_mode_rows(runs_dir: Path) -> tuple[list[dict[str, Any]], list[str]]:
    """Return flattened mode rows and warnings for skipped runs."""
    rows: list[dict[str, Any]] = []
    warnings: list[str] = []

    if not runs_dir.is_dir():
        return rows, [f"runs directory does not exist: {runs_dir}"]

    for run_dir in sorted(path for path in runs_dir.iterdir() if path.is_dir()):
        modes_data = _load_json(run_dir / "modes.json")
        modes = _mode_list(modes_data)
        if not modes:
            warnings.append(f"{run_dir.name}: no modes found - skipped")
            continue

        atoms = _load_json(run_dir / "mode_atoms.json")
        general = atoms.get("general", {}) if isinstance(atoms, dict) else {}
        if not isinstance(general, dict):
            general = {}
            warnings.append(f"{run_dir.name}: invalid general parameters - modes only")
        elif not general:
            warnings.append(f"{run_dir.name}: no general parameters - modes only")

        for mode in modes:
            rows.append({"run_id": run_dir.name, **general, **mode})

    return rows, warnings


def _fieldnames(rows: list[dict[str, Any]]) -> list[str]:
    fields = ["run_id"]
    seen = set(fields)
    for row in rows:
        for field in row:
            if field not in seen:
                seen.add(field)
                fields.append(field)
    return fields


def _csv_value(value: Any) -> Any:
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    if value is None:
        return ""
    return value


def write_csv(rows: list[dict[str, Any]], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = _fieldnames(rows)
    with output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(
            {field: _csv_value(row.get(field)) for field in fields} for row in rows
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export all run modes with repeated module/general parameters."
    )
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    rows, warnings = collect_mode_rows(args.runs_dir)
    if not rows:
        for warning in warnings:
            print(f"warning: {warning}")
        raise SystemExit("No modes found; no CSV was written.")

    write_csv(rows, args.output)
    for warning in warnings:
        print(f"warning: {warning}")
    print(f"Wrote {len(rows)} modes to {args.output}")


if __name__ == "__main__":
    main()