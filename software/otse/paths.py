"""Shared, working-directory-independent locations for data and local outputs."""

from __future__ import annotations

import os
from pathlib import Path


SOURCE_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = (
    SOURCE_ROOT
    if (SOURCE_ROOT / "pyproject.toml").is_file() and (SOURCE_ROOT / "dataset").is_dir()
    else Path.home() / ".otse"
)


def configured_path(variable: str, default: Path) -> Path:
    value = os.environ.get(variable)
    return Path(value).expanduser().resolve() if value else default


DATASET_DIR = configured_path("OTSE_DATASET_DIR", PROJECT_ROOT / "dataset")
WORKSPACE_DIR = configured_path("OTSE_WORKSPACE_DIR", PROJECT_ROOT / "workspace")
RUNS_DIR = configured_path("TRANSCEIVER_RUNS_DIR", WORKSPACE_DIR / "runs")
REPORTS_DIR = configured_path("OTSE_REPORTS_DIR", WORKSPACE_DIR / "reports")
INVENTORY_DIR = configured_path("OTSE_INVENTORY_DIR", WORKSPACE_DIR / "inventory")
ARCHIVE_DIR = configured_path("OTSE_ARCHIVE_DIR", WORKSPACE_DIR / "runs_archive")
LEXICON_PATH = configured_path(
    "OTSE_LEXICON_PATH", DATASET_DIR / "harmonization_lexicon.json"
)
MODEL_DIR = configured_path("OTSE_MODEL_DIR", Path.home() / "models")