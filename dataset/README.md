# Optical Transceiver Modes Dataset

## Contents

- `runs/<run_id>/`: historical extraction artifacts and provenance.
- `reports/`: existing HTML views generated from those artifacts.
- `harmonization_lexicon.json`: versioned canonical replacements for schema field values.
- `example_use_cases/`: dataset usage examples.
- `releases/`: location for curated, versioned JSON/CSV exports after review.

Run files can include `meta.json` (source/model/status/timings), `specs.json` (validated
module fields), `mode_atoms.json` (mode-varying atoms and general fields), `modes.json`
(linked operating modes), raw model responses, parse metadata and `content.md`.
Not every historical run contains every artifact. Field definitions and units are in
`software/otse/transceiver_models.py`; replacement semantics are in
`software/otse/composition/field_replacer.py`.

## Provenance and Limitations

The source material is vendor transceiver datasheets. Extraction combines PDF parsing,
human review, local LLM inference and deterministic validation/harmonization. A validated
record satisfies the schema, not necessarily the source document's intended meaning.
Preserve run IDs, source attribution, model identity and processing configuration when
building release exports. Missing values and cross-field mode associations require
review. Source paths in metadata can be temporary/local paths rather than public URLs.

## Release and Licensing Review

The root MIT license covers the software. Separate dataset licensing terms have not
been selected by this reorganization; do not treat this note as a grant of rights to
third-party source content. Choose appropriate dataset terms before publishing a release.

Audit vendor rights, `content.md`, raw responses and HTML reports for redistributed
source text. Review metadata for local/private paths and replace those in release
exports with stable source identifiers while preserving original research artifacts
privately. Do not publish source PDFs without redistribution permission.

Existing `runs/` and `reports/` remain unchanged and are not automatically cleared for
redistribution. See `releases/README.md` for the release checklist and
`../docs/reproduction.md` for commands that read these artifacts explicitly.