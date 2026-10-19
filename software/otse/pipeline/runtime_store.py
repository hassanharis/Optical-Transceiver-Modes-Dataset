"""Per-runtime storage for extraction results.

Each run gets a timestamped directory containing:
- parsed.json   — serialized ParsedDatasheet metadata
- raw_llm.json  — raw dict returned by LLM (before validation)
- raw_llm_modes_response.json — raw mode-linking completion and finish reason
- specs.json    — validated TransceiverSpecs (if validation passed)
- meta.json     — run metadata (timestamp, source file, provider, status)
"""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from otse.transceiver_models import TransceiverSpecs
from otse.pipeline.pdf_parser import ParsedDatasheet
from otse.paths import RUNS_DIR

logger = logging.getLogger(__name__)

DEFAULT_RUNS_DIR = RUNS_DIR


def _run_id() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")


def store_run(
    parsed: ParsedDatasheet,
    raw_dict: dict[str, Any],
    specs: TransceiverSpecs | None,
    *,
    model_id: str | None = None,
    runs_dir: Path | None = None,
    timings_seconds: dict[str, float] | None = None,
) -> Path:
    """Persist a single extraction run and return the run directory."""
    runs_dir = runs_dir or DEFAULT_RUNS_DIR
    run_dir = runs_dir / _run_id()
    run_dir.mkdir(parents=True, exist_ok=True)

    # Meta
    meta = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source_file": str(parsed.source_path),
        "page_count": parsed.page_count,
        "table_count": len(parsed.tables),
        "model_id": model_id,
        "validation_passed": specs is not None,
        "timings_seconds": timings_seconds or {},
    }
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

    # Parsed metadata (not full text — that can be large)
    parsed_meta = {
        "source_path": str(parsed.source_path),
        "page_count": parsed.page_count,
        "table_count": len(parsed.tables),
        "markdown_chars": len(parsed.markdown),
        "tables": [
            {"page": t.page_index, "label": t.label, "rows": len(t.rows)}
            for t in parsed.tables
        ],
    }
    (run_dir / "parsed.json").write_text(json.dumps(parsed_meta, indent=2), encoding="utf-8")

    # The markdown that was actually sent to the LLM (may be user-edited)
    (run_dir / "content.md").write_text(parsed.markdown, encoding="utf-8")

    # Raw LLM output
    if raw_dict:
        (run_dir / "raw_llm.json").write_text(json.dumps(raw_dict, indent=2), encoding="utf-8")

    # Validated specs
    if specs is not None:
        (run_dir / "specs.json").write_text(
            specs.model_dump_json(indent=2, exclude_none=True), encoding="utf-8"
        )

    logger.info("Run stored: %s", run_dir)
    return run_dir


def update_run_timings(run_dir: Path, timings_seconds: dict[str, float]) -> None:
    """Merge stage durations into an existing run's metadata."""
    meta_path = run_dir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    timings = meta.setdefault("timings_seconds", {})
    timings.update({name: round(seconds, 3) for name, seconds in timings_seconds.items()})
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")


def store_specs(run_dir: Path, specs: TransceiverSpecs) -> dict[str, Any]:
    """Overwrite the run's specifications with validated parameter edits."""
    data = specs.model_dump(mode="json")
    (run_dir / "specs.json").write_text(json.dumps(data, indent=2), encoding="utf-8")

    meta_path = run_dir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    meta["validation_passed"] = True
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return data


def load_run(run_dir: Path) -> dict[str, Any]:
    """Load a previously stored run."""
    result: dict[str, Any] = {}
    for name in (
        "meta.json",
        "parsed.json",
        "raw_llm.json",
        "raw_llm_modes_response.json",
        "raw_llm_modes.json",
        "specs.json",
    ):
        p = run_dir / name
        if p.exists():
            result[name.replace(".json", "")] = json.loads(p.read_text(encoding="utf-8"))
    return result


def list_runs(runs_dir: Path | None = None) -> list[Path]:
    """Return all run directories sorted by name (newest last)."""
    runs_dir = runs_dir or DEFAULT_RUNS_DIR
    if not runs_dir.exists():
        return []
    return sorted(d for d in runs_dir.iterdir() if d.is_dir())
