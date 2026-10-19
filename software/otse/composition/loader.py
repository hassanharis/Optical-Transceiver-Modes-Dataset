"""Load deduplicated corpus records from extraction run folders."""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterator

from otse.paths import RUNS_DIR


@dataclass
class CorpusRecord:
    """One datasheet (latest run per unique source PDF)."""

    run_id: str
    source_file: str
    source_basename: str
    meta: dict[str, Any]
    specs: dict[str, Any]
    modes: list[dict[str, Any]] = field(default_factory=list)

    @property
    def module_id(self) -> str:
        return self.source_basename or self.run_id


def _read_json(path: Path) -> dict[str, Any] | list[Any] | None:
    if not path.is_file():
        return None
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def iter_run_dirs(runs_dir: Path) -> Iterator[Path]:
    if not runs_dir.is_dir():
        return
    for child in sorted(runs_dir.iterdir()):
        if child.is_dir() and (child / "meta.json").is_file():
            yield child


def load_corpus(
    runs_dir: str | Path,
    *,
    dedupe_by_source: bool = True,
) -> list[CorpusRecord]:
    """
    Load specs/modes/meta from ``runs/<run_id>/``.

    When ``dedupe_by_source`` is True, keeps only the lexicographically latest
    run folder per ``meta.source_file`` (matches timestamped run ids).
    """
    root = Path(runs_dir)
    candidates: list[tuple[str, Path, dict[str, Any]]] = []

    for run_path in iter_run_dirs(root):
        meta = _read_json(run_path / "meta.json")
        if not isinstance(meta, dict):
            continue
        run_id = run_path.name
        source = str(meta.get("source_file") or "")
        candidates.append((source, run_path, meta))

    if dedupe_by_source:
        best: dict[str, tuple[str, Path, dict[str, Any]]] = {}
        for source, run_path, meta in candidates:
            key = source or run_path.name
            prev = best.get(key)
            if prev is None or run_path.name > prev[0]:
                best[key] = (run_path.name, run_path, meta)
        selected = [t[1:] for t in best.values()]
    else:
        selected = [(p, m) for _, p, m in candidates]

    records: list[CorpusRecord] = []
    for run_path, meta in selected:
        specs_raw = _read_json(run_path / "specs.json")
        specs = specs_raw if isinstance(specs_raw, dict) else {}

        modes_raw = _read_json(run_path / "modes.json")
        modes: list[dict[str, Any]] = []
        if isinstance(modes_raw, dict):
            raw_modes = modes_raw.get("modes")
            if isinstance(raw_modes, list):
                modes = [m for m in raw_modes if isinstance(m, dict)]

        source_file = str(meta.get("source_file") or "")
        records.append(
            CorpusRecord(
                run_id=run_path.name,
                source_file=source_file,
                source_basename=os.path.basename(source_file) if source_file else run_path.name,
                meta=meta,
                specs=specs,
                modes=modes,
            )
        )

    records.sort(key=lambda r: r.module_id.lower())
    return records


def default_runs_dir() -> Path:
    env = os.environ.get("TRANSCEIVER_RUNS_DIR")
    if env:
        return Path(env)
    return RUNS_DIR


def runs_corpus_version(runs_dir: str | Path) -> int:
    """Change when any run's specs.json changes (for Streamlit cache busting)."""
    root = Path(runs_dir)
    latest_ns = 0
    for run_path in iter_run_dirs(root):
        specs = run_path / "specs.json"
        if specs.is_file():
            latest_ns = max(latest_ns, specs.stat().st_mtime_ns)
    return latest_ns
