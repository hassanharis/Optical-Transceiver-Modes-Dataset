"""Build a per-module inventory from pipeline runs.

A run is one datasheet. A datasheet may describe one orderable SKU or several.
Inventory is one JSON file per SKU: that module's general envelope plus its own
operating modes. Record shapes and split rules are defined by split_run below.

Usage:
    python -m otse.scripts.build_inventory
    python -m otse.scripts.build_inventory --dry-run
    python -m otse.scripts.build_inventory --run 20260821_081405 --run 20260821_093751
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from otse.pipeline.mode_linker import separate_atoms
from otse.paths import INVENTORY_DIR, RUNS_DIR

RUNS = RUNS_DIR
INVENTORY = INVENTORY_DIR

# Hardware identity that belongs on the module when it is constant across that
# SKU's modes. Operating parameters (baud, OSNR, host/media codes, …) stay on
# the mode even if they happen to be constant.
MODULE_IDENTITY_FIELDS = (
    "form_factor",
    "wavelength_band",
    "wavelength_min_nm",
    "wavelength_max_nm",
    "wavelength_center_nm",
    "frequency_min_thz",
    "frequency_max_thz",
    "channel_total",
)

_TOKEN_SPLIT = re.compile(r"[^A-Za-z0-9.+-]+")
_UNSAFE_FILE = re.compile(r'[<>:"/\\|?*]+')


def _load(path: Path) -> Any | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _as_list(value: Any) -> list[Any]:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [item for item in value if item not in (None, "")]
    return [value]


def _unwrap(value: Any) -> Any:
    if isinstance(value, list) and len(value) == 1:
        return value[0]
    return value


def _norm_text(value: Any) -> str:
    return str(value).strip()


def _slug(text: str) -> str:
    text = _UNSAFE_FILE.sub("_", text.strip())
    text = re.sub(r"\s+", "_", text)
    text = text.rstrip(" .=")
    text = re.sub(r"_+", "_", text).strip("._")
    return text or "unknown"


def _sku_names(value: Any) -> list[str]:
    names: list[str] = []
    seen: set[str] = set()
    for item in _as_list(value):
        name = _norm_text(item)
        if not name:
            continue
        key = name.lower()
        if key in seen:
            continue
        seen.add(key)
        names.append(name)
    return names


def _canonical_sku(name: str, skus: list[str]) -> str:
    lookup = {sku.lower(): sku for sku in skus}
    return lookup.get(name.lower(), name)


def discover_skus(
    specs: dict[str, Any],
    general: dict[str, Any],
    modes: list[dict[str, Any]],
) -> list[str]:
    """SKU list is discovered from the run, never hardcoded."""
    for source in (specs.get("model"), general.get("model")):
        names = _sku_names(source)
        if names:
            return names
    names: list[str] = []
    seen: set[str] = set()
    for mode in modes:
        for name in _sku_names(mode.get("model")):
            key = name.lower()
            if key not in seen:
                seen.add(key)
                names.append(name)
    return names


def mode_list(modes_data: Any) -> list[dict[str, Any]]:
    if not modes_data:
        return []
    if isinstance(modes_data, list):
        return [m for m in modes_data if isinstance(m, dict)]
    if isinstance(modes_data, dict):
        raw = modes_data.get("modes", [])
        if isinstance(raw, list):
            return [m for m in raw if isinstance(m, dict)]
    return []


def resolve_mode_skus(mode: dict[str, Any], skus: list[str]) -> list[str]:
    """Return the SKUs this mode belongs to.

    Multi-SKU datasheets require an explicit model on the mode (canonical:
    20260821_081405, 20260821_093751). A missing model is only valid when the
    run has a single SKU already sitting in general.
    """
    declared = _sku_names(mode.get("model"))
    if declared:
        return [_canonical_sku(name, skus) for name in declared]

    if len(skus) == 1:
        return list(skus)

    tokens = {tok.lower() for tok in _TOKEN_SPLIT.split(str(mode.get("label") or "")) if tok}
    return [sku for sku in skus if sku.lower() in tokens]


def _values_equal(left: Any, right: Any) -> bool:
    return json.dumps(left, sort_keys=True, default=str) == json.dumps(
        right, sort_keys=True, default=str
    )


def constant_identity(modes: list[dict[str, Any]], field: str) -> Any | None:
    present = [mode[field] for mode in modes if field in mode and mode[field] not in (None, "")]
    if not present:
        return None
    first = present[0]
    if all(_values_equal(item, first) for item in present[1:]):
        return first
    return None


def build_general(
    run_general: dict[str, Any],
    sku: str,
    vendor: str,
    sku_modes: list[dict[str, Any]],
) -> dict[str, Any]:
    general = dict(run_general)
    for field in MODULE_IDENTITY_FIELDS:
        lifted = constant_identity(sku_modes, field)
        if lifted is not None:
            general[field] = lifted
    ordered: dict[str, Any] = {"vendor": vendor, "model": sku}
    for key, value in general.items():
        if key in ordered or value in (None, ""):
            continue
        ordered[key] = _unwrap(value) if key in MODULE_IDENTITY_FIELDS else value
    return ordered


def strip_mode(mode: dict[str, Any]) -> dict[str, Any]:
    skip = {"model"} | set(MODULE_IDENTITY_FIELDS)
    cleaned: dict[str, Any] = {}
    for key, value in mode.items():
        if key in skip or value in (None, ""):
            continue
        cleaned[key] = value
    return cleaned


def inventory_filename(vendor: str, model: str) -> str:
    return f"{_slug(vendor)}__{_slug(model)}.json"


def split_run(
    run_id: str,
    run_dir: Path,
) -> tuple[list[dict[str, Any]], list[str]]:
    """Return (module records, run-level warnings)."""
    warnings: list[str] = []
    specs = _load(run_dir / "specs.json")
    if not isinstance(specs, dict):
        return [], [f"{run_id}: no specs.json — skipped"]

    meta = _load(run_dir / "meta.json") or {}
    modes_data = _load(run_dir / "modes.json")
    atoms = _load(run_dir / "mode_atoms.json")
    if isinstance(atoms, dict) and "general" in atoms:
        general = dict(atoms.get("general") or {})
    else:
        _, general = separate_atoms(specs)
        warnings.append(f"{run_id}: no mode_atoms.json — general derived from specs")

    modes = mode_list(modes_data)
    if modes_data is None:
        warnings.append(f"{run_id}: no modes.json")

    skus = discover_skus(specs, general, modes)
    if not skus:
        return [], warnings + [f"{run_id}: no model name in specs, general, or modes — skipped"]

    vendor = _norm_text(general.get("vendor") or specs.get("vendor") or "Unknown") or "Unknown"
    split = "single_model" if len(skus) == 1 else "by_mode_model"
    source_file = meta.get("source_file") if isinstance(meta, dict) else None

    assigned: dict[str, list[dict[str, Any]]] = {sku: [] for sku in skus}
    extra_skus: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for index, mode in enumerate(modes):
        targets = resolve_mode_skus(mode, skus)
        if not targets:
            warnings.append(
                f"{run_id}: mode[{index}] {mode.get('label')!r} has no model — "
                "multi-SKU runs must tag every mode"
            )
            continue
        for sku in targets:
            if sku in assigned:
                assigned[sku].append(mode)
            else:
                extra_skus[sku].append(mode)
                warnings.append(
                    f"{run_id}: mode[{index}] refers to undeclared model {sku!r}"
                )

    for sku, sku_modes in extra_skus.items():
        assigned[sku] = sku_modes

    records: list[dict[str, Any]] = []
    for sku, sku_modes in assigned.items():
        record_warnings: list[str] = []
        if not sku_modes and modes:
            record_warnings.append("no modes assigned to this model")
        elif not sku_modes and modes_data is None:
            record_warnings.append("modes.json missing")

        records.append(
            {
                "vendor": vendor,
                "model": sku,
                "source_run": run_id,
                "source_file": source_file,
                "split": split,
                "warnings": record_warnings,
                "general": build_general(general, sku, vendor, sku_modes),
                "modes": [strip_mode(mode) for mode in sku_modes],
            }
        )
    return records, warnings


def collect_runs(run_ids: list[str] | None) -> list[Path]:
    if not RUNS.exists():
        return []
    if run_ids:
        return [RUNS / run_id for run_id in run_ids]
    return sorted(path for path in RUNS.iterdir() if path.is_dir())


def write_inventory(
    records: list[dict[str, Any]],
    run_warnings: list[str],
    n_runs: int,
    out_dir: Path,
    dry_run: bool,
) -> Path:
    by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for record in records:
        key = (record["vendor"].lower(), record["model"].lower())
        existing = by_key.get(key)
        if existing is None:
            by_key[key] = record
            continue
        if record["source_run"] >= existing["source_run"]:
            superseded = existing["source_run"]
            record["warnings"] = list(record["warnings"]) + [
                f"supersedes run {superseded}"
            ]
            by_key[key] = record
        else:
            existing["warnings"] = list(existing["warnings"]) + [
                f"supersedes run {record['source_run']}"
            ]

    modules = sorted(by_key.values(), key=lambda r: (r["vendor"].lower(), r["model"].lower()))
    index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "n_runs": n_runs,
        "n_modules": len(modules),
        "run_warnings": run_warnings,
        "modules": [
            {
                "vendor": rec["vendor"],
                "model": rec["model"],
                "file": inventory_filename(rec["vendor"], rec["model"]),
                "source_run": rec["source_run"],
                "n_modes": len(rec["modes"]),
                "split": rec["split"],
                "warnings": rec["warnings"],
            }
            for rec in modules
        ],
    }

    if dry_run:
        return out_dir / "index.json"

    if out_dir.exists():
        for stale in out_dir.glob("*.json"):
            stale.unlink()
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "index.json").write_text(json.dumps(index, indent=2), encoding="utf-8")
    for rec in modules:
        path = out_dir / inventory_filename(rec["vendor"], rec["model"])
        path.write_text(json.dumps(rec, indent=2), encoding="utf-8")
    return out_dir / "index.json"


def main() -> None:
    global RUNS
    parser = argparse.ArgumentParser(description="Build per-model inventory from runs/")
    parser.add_argument("--runs-dir", type=Path, default=RUNS_DIR)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--run",
        action="append",
        dest="run_ids",
        help="Limit to one run id (repeatable). Default: every directory in runs/",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=INVENTORY,
        help="Output directory (default: workspace/inventory or OTSE_INVENTORY_DIR)",
    )
    args = parser.parse_args()
    RUNS = args.runs_dir
    tag = "  [DRY RUN]" if args.dry_run else ""

    run_dirs = collect_runs(args.run_ids)
    records: list[dict[str, Any]] = []
    run_warnings: list[str] = []
    used_runs = 0

    print("=" * 78)
    print("SPLIT" + tag)
    print("=" * 78)

    for run_dir in run_dirs:
        run_id = run_dir.name
        if not run_dir.is_dir():
            run_warnings.append(f"{run_id}: not a directory")
            print(f"  {run_id}: missing")
            continue
        used_runs += 1
        recs, warns = split_run(run_id, run_dir)
        run_warnings.extend(warns)
        records.extend(recs)
        if recs:
            split = recs[0]["split"]
            names = ", ".join(r["model"] for r in recs)
            print(f"  {run_id}: {split} -> {len(recs)} module(s): {names}")
        else:
            print(f"  {run_id}: skipped")
        for warn in warns:
            print(f"    ! {warn}")

    print()
    print("=" * 78)
    print("WRITE" + tag)
    print("=" * 78)
    index_path = write_inventory(records, run_warnings, used_runs, args.out, args.dry_run)
    unique = {(r["vendor"].lower(), r["model"].lower()) for r in records}
    print(f"  {len(unique)} module file(s) + index.json -> {args.out}")
    print(f"  {len(run_warnings)} run-level warning(s)")
    if not args.dry_run:
        print(f"  index: {index_path}")


if __name__ == "__main__":
    main()
