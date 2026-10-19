# Setup and Reproduction

Use Python 3.11 or newer. From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
```

On Linux/macOS, activate with `source .venv/bin/activate`. Editable installation makes
`otse` importable from any working directory. Relative CLI input/output paths are
relative to the caller's directory; use absolute paths when launching elsewhere.

## Applications and Extraction

```text
python -m otse.launch extract       # port 8501
python -m otse.launch composition   # port 8502
python -m otse.launch harmonize     # port 8503
python -m otse.launch extract --port 8510
python -m otse.pipeline.run /path/to/datasheet.pdf --model MODEL_ID
```

Installed console commands are `otse-app`, `otse-extract`, `otse-export` and
`otse-composition`. Windows batch launchers activate `.venv` when present and do not
install or upgrade dependencies on startup. `start - app_2.bat` delegates to
`run_extraction_app.bat` for compatibility.

Start the external model service separately:

```text
llama-server --models-dir /path/to/models --models-max 1
```

The default endpoint is `http://127.0.0.1:8080`. Record the server build, model name,
quantization, inference settings, Python environment and lexicon alongside results.
Extraction and mode synthesis depend on model behavior and are not guaranteed bitwise
reproducible. Do not assume historical runs can be recreated without their model setup.

## Path Configuration

CLI options and UI path selections override defaults. Environment settings are read
when modules are imported; set them before starting a command or app.

| Variable | Checkout default |
| --- | --- |
| `OTSE_DATASET_DIR` | `<repository>/dataset` |
| `OTSE_WORKSPACE_DIR` | `<repository>/workspace` |
| `TRANSCEIVER_RUNS_DIR` | `<workspace>/runs` |
| `OTSE_REPORTS_DIR` | `<workspace>/reports` |
| `OTSE_INVENTORY_DIR` | `<workspace>/inventory` |
| `OTSE_ARCHIVE_DIR` | `<workspace>/runs_archive` |
| `OTSE_LEXICON_PATH` | `<dataset>/harmonization_lexicon.json` |
| `OTSE_MODEL_DIR` | `~/models` |

Outside a source checkout, the base directory is `~/.otse`. Dataset artifacts are not
bundled in the Python distribution: set `OTSE_DATASET_DIR` to a downloaded dataset or
set `OTSE_LEXICON_PATH` explicitly before using harmonization/composition tools.

To inspect the existing corpus in this checkout, from the repository root:

```powershell
$env:TRANSCEIVER_RUNS_DIR = (Resolve-Path dataset/runs).Path
python -m otse.launch composition
```

This override also affects extraction and maintenance tools in the same environment.
Remove it before creating new local runs: `Remove-Item Env:TRANSCEIVER_RUNS_DIR`.

## Corpus Utilities

```text
python -m otse.scripts.composition_report --runs-dir dataset/runs
python -m otse.scripts.export_all_modes --runs-dir dataset/runs -o workspace/all_modes.csv
python -m otse.scripts.build_inventory --runs-dir dataset/runs --dry-run
python -m otse.scripts.refresh_reports --runs-dir dataset/runs --dry-run
python -m otse.scripts.apply_field_replacements --list-rules
python -m otse.scripts.apply_field_replacements --runs-dir dataset/runs --dry-run
python -m otse.scripts.generate_report dataset/runs/RUN_ID -o workspace/report.html
python -m otse.scripts.generate_modes_report dataset/runs/RUN_ID -o workspace/modes.html
```

`cleanup_runs` and `repair_runs` retain historical, run-specific maintenance policies.
Both accept `--runs-dir` and `--dry-run`; inspect their policies before using them on a
different corpus. Never run mutating commands on a release snapshot without a backup.

## Migration

- `pipeline.*`, `composition.*` and `transceiver_models` now live under `otse.*`.
- Old standalone script commands become `python -m otse.scripts.SCRIPT_NAME`.
- `dataset/harmonization lexicon.json` is now `dataset/harmonization_lexicon.json`.
- Existing dataset runs/reports were preserved; new outputs default to `workspace/`.
- Development dependencies moved from the recursive requirements include to `[dev]`.