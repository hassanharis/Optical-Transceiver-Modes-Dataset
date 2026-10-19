# Optical Transceiver Modes Dataset and OTSE

This repository brings together a structured optical transceiver dataset and OTSE, the
Optical Transceiver Spec Extractor used to build and inspect it. The goal is to turn
heterogeneous vendor datasheets into comparable module specifications and operating
modes for optical-network research, catalog analysis and planning-tool development.

OTSE uses a local LLM through llama-server to recover parameters such as wavelength,
baud rate, power, FEC, modulation and reach into a Pydantic schema. Streamlit interfaces
support reviewing parsed text, extracting specifications, inspecting corpus composition
and maintaining canonical terminology. Dataset artifacts are separate from the software
package and from new local extraction outputs.

## Dataset Overview

The dataset distinguishes a **module envelope**, which describes the transceiver as a
whole, from **operating modes**, which associate selectable configurations with their
interfaces, standards identifiers and performance parameters. A module may support
several modes with different bit rates, modulation formats, FEC schemes, OSNR requirements
and dispersion tolerances; those values should not be combined arbitrarily.

The repository provides three complementary resources:

- **Schema:** typed fields, descriptions, units and module-versus-mode boundaries in
  [software/otse/transceiver_models.py](software/otse/transceiver_models.py).
- **Terminology:** field-specific canonical values and synonym mappings in the
  [harmonization lexicon](dataset/harmonization_lexicon.json).
- **Artifacts and tooling:** extraction runs, HTML reports, corpus loaders, analytics,
  mode exports and inventory generation. See the [dataset guide](dataset/README.md).

Corpus size, vendor coverage and field completeness depend on the selected run folders
and deduplication policy. Generate a composition report for the snapshot being studied
rather than treating counts from an individual transceiver example as corpus totals.

## How It Works

```
PDF → Parse → Review Markdown → Extract Atoms → Link Modes → Harmonize → Export/Review
```

1. **Parse** — Converts PDF to markdown using PyMuPDF4LLM (text + tables)
2. **Review** — Editable text area to fix OCR errors or trim irrelevant sections
3. **Extract** — Recover independent atomic values into `TransceiverSpecs`, with schema validation
4. **Link** — Separate module-level and mode-varying fields, then synthesize operating modes
5. **Harmonize** — Apply versioned, field-specific replacement rules to align vendor terminology
6. **Inspect and export** — Review corpus coverage, generate reports and export modes or inventories

These stages are available through separate tools, not a single automatic publish command.
The extraction CLI performs parsing, atomic extraction and storage; the extraction UI
also exposes mode synthesis. Harmonization and corpus/export tools run separately.
Run storage retains metadata, reviewed markdown and model responses for inspection.

## Design Notes

Why the pipeline is shaped this way:

**Two-stage extraction: atoms first, then modes.** Rather than asking the model to produce a
structured, mode-aware object in one pass, extraction is split into two stages. Stage one pulls every
parameter as an independent atomic value with no cross-field inference. Stage two links those atoms
into coherent operating modes. For coherent optics datasheets, recovering which values *co-occur* in a
selectable configuration is the genuinely hard part — a single module may expose a dozen application
codes, each with its own baud rate, modulation, OSNR requirement and reach. Separating "what values
exist" from "which values belong together" makes errors easier to isolate and lets
deterministic processing constrain the mode-linking task. Quantitative accuracy claims
require a versioned evaluation set, annotation protocol and reported metrics; schema
validation alone does not establish extraction correctness.

**Module envelope vs. per-mode specification.** `MODE_FIELDS` in the
[schema](software/otse/transceiver_models.py) marks which
parameters vary per configuration and which describe the module as a whole. A worst-case receiver
sensitivity is a hardware envelope; a required OSNR is a per-mode figure. Encoding that distinction in
the schema means mode synthesis only has to reason about the fields that can actually differ.

**Field descriptions do double duty.** Each Pydantic `Field(description=...)` is both the validation
contract and the schema text sent to the model, generated from `model_json_schema()`. There is one
definition of what a field means, so the prompt and the validator cannot drift apart as the schema
evolves.

**Human review sits before extraction, not after.** PDF-to-text on vendor datasheets is unreliable —
merged table cells, footnote markers glued to values, multi-column layouts. The editable markdown step
acknowledges that rather than pretending parsing is solved, and lets the operator trim irrelevant
sections or repair a mangled table before spending inference time on it.

**Runs record exactly what was sent.** `content.md` stores the post-edit markdown that actually reached
the model, alongside the raw LLM response and the validated specs. A run can be understood after the
fact without re-parsing the source PDF.

**Harmonization is a first-class stage.** Vendors may describe the same concept using
different FEC names, form-factor spellings, fiber labels, modulation names, connector
terms or standards strings. Literal recovery and terminology alignment are different
tasks: a value can be recovered faithfully yet remain difficult to compare across
vendors. The lexicon makes those mappings explicit, field-specific and reviewable.
Record its version with derived exports, and preserve an original artifact snapshot
before applying replacement rules to run files.

## Research and Use Cases

| Use case | How the dataset can help |
| --- | --- |
| Mode comparison | Filter by bit rate, FEC or dispersion tolerance and compare documented TX/RX power and OSNR requirements under compatible conditions. |
| Link budgets and performance modeling | Supply documented sensitivity, power, OSNR and impairment limits to external engineering models. Fiber loss, dispersion and other link assumptions must be supplied separately. |
| Digital twins and network planning | Populate comparable transceiver catalogs for mode selection and what-if analysis against fiber-plant constraints. |
| Host-interface coverage | Relate host electrical interface codes to media modes and form factors for migration planning, procurement and interoperability screening. |
| Power-efficiency analysis | Compare reported consumption with capacity and operating conditions, distinguishing module-level ratings from genuinely mode-specific measurements. |
| Standards and metadata research | Examine vendor terminology, standards identifiers, missing values and differences in reported specifications. |
| Human-in-the-loop QA | Audit replacement-rule changes and inspect newly encountered vendor terms before accepting a derived export. |
| AI and extraction benchmarks | Study literal recovery, canonicalization and mode association, or use human-verified examples to develop training and evaluation datasets. |

These are supported research directions and downstream applications, not bundled
simulators or validated deployment recommendations. Matching a few datasheet values to
a standard is not sufficient to demonstrate standards compliance or interoperability.

### Benchmarking and Future Work

A useful evaluation should distinguish **literal extraction**, **canonical vocabulary
alignment** and **mode association**. Report slot-level precision, recall or F1 before
and after harmonization, vocabulary adherence, out-of-vocabulary vendor terms, missing
field coverage and whether values were assigned to the correct mode. Publish the
snapshot, deduplication policy, reference annotations and scoring rules with results.

The rule-based lexicon provides a baseline for comparing normalization during extraction
with a dedicated post-extraction stage. Potential extensions include retrieval-augmented
normalization using synonym clusters and standards definitions, instruction tuning on
human-verified literal/canonical pairs, domain-language adaptation, and constrained
decoding. These learning-based methods are research proposals, not implemented training
workflows in this repository. Mode-selection models would additionally need labeled or
carefully simulated link conditions; such labels do not follow from datasheet modes alone.

## Requirements

- Python 3.11+
- [llama-server](https://github.com/ggml-org/llama.cpp) with locally downloaded GGUF models

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Linux/macOS: source .venv/bin/activate
python -m pip install -e .
```

Core extraction dependencies are pinned in `requirements.txt`. For linting and tests, use
`python -m pip install -e ".[dev]"`. Record the complete environment with each reproducibility
study, including the pandas version, external llama-server build, model and inference settings.

Start the model server:

```bash
llama-server --models-dir /path/to/models --models-max 1
```

## Usage

```bash
python -m otse.launch extract
python -m otse.launch composition
python -m otse.launch harmonize
```

On Windows, use [run_extraction_app.bat](run_extraction_app.bat),
[run_composition_app.bat](run_composition_app.bat) or
[run_harmonization_app.bat](run_harmonization_app.bat) after installation.

Or via CLI:

```bash
python -m otse.pipeline.run path/to/datasheet.pdf --model Qwen3.6-27B-Q4_K_M
```

## Project Structure

```
dataset/
  README.md                    Dataset structure, provenance and release notes
  harmonization_lexicon.json    Canonical value replacement rules
  runs/                        Existing extraction corpus (preserved)
  reports/                     Existing HTML reports (preserved)
  releases/                    Curated release exports and release requirements
  example_use_cases/
software/otse/
  paths.py                     Shared data and output path configuration
  launch.py                    Streamlit app launcher
  transceiver_models.py        Pydantic schema (TransceiverSpecs)
  pipeline/                    PDF parsing, atomic extraction, mode synthesis, storage
  composition/                 Corpus loading, harmonization and analytics
  scripts/                     Streamlit apps and CLI utilities
docs/                          Architecture and reproduction instructions
tests/                         Import, path and entry-point regression checks
workspace/                     Local outputs, ignored by Git
```

## Run Storage

New extraction runs are saved under `workspace/runs/<YYYYMMDD_HHMMSS>/`.
Reports, exports and inventory also default to `workspace/`, not the published dataset.
Existing `dataset/runs/` and `dataset/reports/` are preserved, not silently rewritten.
Select `dataset/runs/` explicitly when analyzing the existing corpus:

```bash
python -m otse.scripts.composition_report --runs-dir dataset/runs
python -m otse.scripts.export_all_modes --runs-dir dataset/runs
python -m otse.scripts.build_inventory --runs-dir dataset/runs --dry-run
```

### Load the Corpus in Python

After installing OTSE, run this from the repository root:

```python
from otse.composition.loader import load_corpus

records = load_corpus("dataset/runs", dedupe_by_source=True)
for record in records:
  print(record.module_id, len(record.modes))
```

The loader selects the latest run per stored source identifier by default. Inspect
those identifiers before interpreting this as unique physical module or datasheet
coverage: temporary upload paths are not guaranteed to be stable source identities.
Use `dedupe_by_source=False` to inspect every run. The Python package does not bundle
the corpus; when working elsewhere, pass an absolute dataset path.

The composition and harmonization apps have a Runs directory field. Alternatively set
`TRANSCEIVER_RUNS_DIR` to an absolute corpus directory before launching an app.
Set `OTSE_MODEL_DIR` if your GGUF files are not in `~/models`.
See [reproduction instructions](docs/reproduction.md) for all path settings and commands,
and [architecture](docs/architecture.md) for the component boundaries.

| File | Contents |
|------|----------|
| `meta.json` | Timestamp, source file, model used, validation status |
| `content.md` | The markdown actually sent to the LLM |
| `raw_llm.json` | Raw JSON returned by the model |
| `specs.json` | Validated `TransceiverSpecs` (only if validation passed) |
| `parsed.json` | Parse metadata (page count, tables, char count) |
| `mode_atoms.json` | Separation of multi-valued mode fields and general module fields |
| `raw_llm_modes_response.json` | Mode-linking completion and finish metadata |
| `raw_llm_modes.json` | Parsed raw mode-linking output |
| `modes.json` | Synthesized operating modes |

Artifacts are stage-dependent; incomplete or historical runs may omit some files.
The lexicon's `run_artifacts` list specifies which JSON files replacement rules can
modify. Archive originals before applying harmonization when literal-versus-canonical
evaluation or reconstruction of the original model response matters.

## Extracted Parameters

The schema covers: vendor/model identification, wavelength/frequency, baud rate, modulation formats, TX/RX power, OSNR, chromatic dispersion, PMD/PDL, FEC types and thresholds, reach, host/media interface codes, form factor, and direct-detect specific fields.

## Provenance and Responsible Use

Source material consists of vendor datasheets. The pipeline supports human review of
parsed content and retains run-level source/model metadata, reviewed markdown and raw
responses. Those artifacts aid auditing but do not demonstrate that every record has
been independently human-verified. Document verification status for any released snapshot.

- Treat missing values as unknown, not zero or evidence that a capability is unsupported.
- Compare values only under compatible conditions, including BER, FEC, wavelength,
  temperature, mode and OSNR reference bandwidth where specified.
- Preserve the distinction between module envelopes, mode-specific values and inferred
  relationships. Do not turn independent extrema into an undocumented operating mode.
- Use the dataset as evidence for research and screening, not a substitute for current
  vendor documentation, standards testing or engineering validation.
- Review source attribution, private/local paths, vendor text and redistribution rights
  before publishing artifacts or deriving model-training datasets.

## Release Status

Software is provided under the [MIT license](LICENSE). Dataset licensing and third-party
redistribution rights require separate review; see [dataset notes](dataset/README.md).
The existing run folders and reports are research artifacts, not an audited public release.
Dataset licensing terms, a curated snapshot and a publication DOI are not established
by this README. The Word-document draft proposes CC BY 4.0 for the dataset, but that
proposal is not a license grant and does not replace third-party rights review.
See the [release checklist](dataset/releases/README.md) before publishing a snapshot.

## Citation

Software citation metadata is provided in [CITATION.cff](CITATION.cff). Until a formal
dataset citation and DOI are available, identify the repository, software revision,
dataset snapshot, schema revision and harmonization-lexicon version used in your work.
Do not use the software version as a substitute for a dataset or schema release identifier.

## Development

```bash
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
```
