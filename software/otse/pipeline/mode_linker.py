"""Step 3: Mode synthesis — link multi-valued atoms into configuration modes.

Takes the flat extracted specs and identifies which atomic values belong to
the same logical operating mode (e.g. same table row, same application code).

Module and variant context is passed separately from the multi-valued atoms.
Variants stay in that context; they are not turned into modes.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any

from openai import OpenAI

from otse.pipeline.atom_extractor import BASE_URL, _parse_json_from_response
from otse.pipeline.pdf_parser import ParsedDatasheet
from otse.pipeline.prompts import LINKING_SYSTEM_PROMPT, LINKING_USER_PROMPT_TEMPLATE
from otse.transceiver_models import MODE_FIELDS

logger = logging.getLogger(__name__)

USER_PROMPT_TEMPLATE = LINKING_USER_PROMPT_TEMPLATE


def _chunk_by_sections(md_text: str) -> list[tuple[str, str]]:
    """Split markdown into (heading, body) chunks by top-level headings."""
    lines = md_text.splitlines(keepends=True)
    chunks: list[tuple[str, str]] = []
    current_heading = ""
    current_body: list[str] = []

    for line in lines:
        if re.match(r"^#{1,6}\s+", line):
            if current_heading or current_body:
                chunks.append((current_heading, "".join(current_body)))
            current_heading = line.strip().lstrip("#").strip()
            current_body = []
        else:
            current_body.append(line)

    if current_heading or current_body:
        chunks.append((current_heading, "".join(current_body)))
    return chunks


def _normalize(text: str) -> str:
    """Lowercase, collapse whitespace, strip punctuation for fuzzy matching."""
    return re.sub(r"[^a-z0-9 ]", "", text.lower()).strip()


def _filter_sections_by_provenance(
    md_text: str, provenance: str | list[str]
) -> str:
    """Return only the sections referenced in provenance_datasheet_sections.

    Falls back to full text if provenance lists as many or more sections than exist.
    """
    chunks = _chunk_by_sections(md_text)
    if not chunks:
        return md_text

    # Parse provenance into normalized target names.
    provenance_items = (
        provenance if isinstance(provenance, list) else re.split(r"[,;\n]", provenance)
    )
    targets = [_normalize(item) for item in provenance_items if item.strip()]
    if not targets:
        return md_text

    total_sections = len([h for h, _ in chunks if h])
    if len(targets) >= total_sections:
        return md_text

    # Match each chunk heading against targets using substring containment
    selected: list[str] = []
    for heading, body in chunks:
        norm_heading = _normalize(heading)
        if not norm_heading:
            continue
        for target in targets:
            if target in norm_heading or norm_heading in target:
                selected.append(f"## {heading}\n{body}")
                break

    if not selected:
        logger.warning("Provenance filtering matched 0 sections; using full text")
        return md_text

    logger.info("Provenance filter: %d/%d sections selected", len(selected), total_sections)
    return "\n\n".join(selected)


def separate_atoms(specs_dict: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Split specs into (multi_valued_mode_atoms, general_params).

    Mode fields with >1 value (or list of objects like penalties) go to multi_valued.
    Mode fields with exactly 1 scalar value or general fields go to general.
    """
    multi = {}
    general = {}

    for key, value in specs_dict.items():
        if key in MODE_FIELDS:
            if isinstance(value, list) and len(value) > 1:
                multi[key] = value
            elif key == "penalties" and isinstance(value, list) and len(value) > 0:
                # Penalties can have 1 or more entries that may belong to specific modes
                multi[key] = value
            elif value is not None:
                general[key] = value
        else:
            if value is not None:
                general[key] = value

    return multi, general


def _build_field_template(multi: dict[str, Any]) -> str:
    """Build the per-mode field list for the output schema."""
    lines = []
    for field in multi:
        if field == "penalties":
            lines.append(
                '      "penalties": [<penalty objects from the pool for this mode, or omit>]'
            )
        else:
            lines.append(f'      "{field}": <one value from the {field} pool>')
    return ",\n".join(lines)


def synthesize_modes(
    specs_dict: dict[str, Any],
    parsed: ParsedDatasheet,
    *,
    run_dir: Path | None = None,
    model_id: str | None = None,
    base_url: str = BASE_URL,
    temperature: float = 0.1,
    max_tokens: int = 16384,
) -> tuple[dict[str, Any] | None, dict[str, Any], dict[str, Any]]:
    """Run mode synthesis and return (modes_result, multi_atoms, general_params).

    Returns (None, multi, general) on failure.
    """
    multi, general = separate_atoms(specs_dict)

    if not multi:
        logger.info("No multi-valued mode fields — single mode module.")
        return {"modes": [{"label": "default", **{k: v for k, v in specs_dict.items() if k in MODE_FIELDS and v is not None}}]}, multi, general

    client = OpenAI(base_url=f"{base_url}/v1", api_key="no-key", timeout=600.0)

    if not model_id:
        models_resp = client.models.list()
        model_id = models_resp.data[0].id if models_resp.data else "default"

    content = parsed.markdown or parsed.full_text

    # Filter to only provenance-referenced sections if available
    provenance = specs_dict.get("provenance_datasheet_sections")
    if provenance and isinstance(provenance, (str, list)):
        content = _filter_sections_by_provenance(content, provenance)

    if len(content) > 80_000:
        content = content[:80_000] + "\n\n[...truncated...]"

    field_template = _build_field_template(multi)
    context = {key: value for key, value in general.items() if key != "suggestions"}
    prompt = USER_PROMPT_TEMPLATE.format(
        atoms=json.dumps(multi, indent=2),
        context=json.dumps(context, indent=2),
        content=content,
        field_template=field_template,
    )

    logger.info("Synthesizing modes: %d multi-valued fields, model=%s", len(multi), model_id)

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": LINKING_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    choice = response.choices[0]
    raw_response = choice.message.content or ""

    if run_dir is not None:
        (run_dir / "raw_llm_modes_response.json").write_text(
            json.dumps(
                {
                    "finish_reason": choice.finish_reason,
                    "content": raw_response,
                    "reasoning_content": getattr(choice.message, "reasoning_content", None),
                },
                indent=2,
            ),
            encoding="utf-8",
        )

    if not raw_response.strip():
        reasoning = getattr(choice.message, "reasoning_content", None) or ""
        if reasoning:
            raw_response = reasoning

    if not raw_response.strip():
        logger.error("Mode synthesis: empty LLM response (finish_reason=%s)", choice.finish_reason)
        return None, multi, general

    result = _parse_json_from_response(raw_response)
    if not isinstance(result, dict) or "modes" not in result:
        logger.warning("Mode synthesis: unexpected response structure")
        if isinstance(result, list):
            result = {"modes": result}
        else:
            return None, multi, general

    logger.info("Mode synthesis: %d modes identified", len(result.get("modes", [])))
    return result, multi, general


def store_modes(run_dir: Path, modes: dict[str, Any], multi: dict[str, Any], general: dict[str, Any]) -> None:
    """Save mode synthesis results to the run directory."""
    (run_dir / "raw_llm_modes.json").write_text(
        json.dumps(modes, indent=2), encoding="utf-8"
    )
    (run_dir / "modes.json").write_text(json.dumps(modes, indent=2), encoding="utf-8")
    (run_dir / "mode_atoms.json").write_text(
        json.dumps({"multi_valued": multi, "general": general}, indent=2),
        encoding="utf-8",
    )
    logger.info("Modes saved to %s", run_dir)
