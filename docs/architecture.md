# Architecture

OTSE separates reusable extraction and composition logic from its command-line and
Streamlit interfaces. The importable package lives at `software/otse/` and is installed
with `python -m pip install -e .` from the repository root.

```text
PDF -> pipeline.pdf_parser -> reviewed markdown -> pipeline.atom_extractor
    -> validated TransceiverSpecs -> pipeline.mode_linker -> operating modes
    -> pipeline.runtime_store -> workspace/runs/<run_id>/

Run artifacts -> composition.loader -> composition.fields / analytics
             -> composition.field_replacer -> harmonized run artifacts
             -> scripts -> inventory, flat exports, HTML reports and corpus UIs
```

## Ownership

- `transceiver_models.py`: schema definitions and module-versus-mode field boundaries.
- `pipeline/`: parsing, LLM extraction, deterministic processing and run persistence.
- `composition/`: corpus loading, field discovery, analytics and replacement rules.
- `scripts/`: user interfaces, maintenance commands and export/report generation.
- `paths.py`: working-directory-independent configuration; no import-path mutation.
- `launch.py`: finds installed app scripts and starts Streamlit using the same interpreter.

Internal imports are package-qualified (`otse.pipeline`, `otse.composition`). Run utilities
as modules rather than invoking their source files directly. The CLI pipeline extracts
atoms; the extraction UI also exposes review, mode synthesis and report generation.

## Data Boundaries

`dataset/` contains the existing corpus, lexicon, reports, examples and a location for
reviewed release exports. Existing artifacts remain in place so historical evidence is
not altered by this reorganization. New outputs go to ignored `workspace/` by default.
Published data is never selected as a write target implicitly. Explicit path overrides
can select the corpus, so back it up before running harmonization or maintenance tools.

Extraction needs an external llama-server and model files; neither is bundled. The
package does not download model weights or start the server automatically.