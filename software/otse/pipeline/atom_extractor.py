"""Step 2: Atomic parameter extraction via LLM.

Sends parsed datasheet content to an LLM and extracts each field from
TransceiverSpecs as an independent atomic value.

Uses a local llama-server router (OpenAI-compatible at 127.0.0.1:8080).
"""

from __future__ import annotations

import json
import logging
import re
from typing import Any

from openai import OpenAI
from pydantic import ValidationError

from otse.pipeline.pdf_parser import ParsedDatasheet
from otse.pipeline.penalty_parser import extract_table_penalties, merge_penalties
from otse.pipeline.prompts import (
    EXTRACTION_SYSTEM_PROMPT,
    EXTRACTION_USER_PROMPT_TEMPLATE,
    extraction_schema_text,
)
from otse.pipeline.units import normalize_quantities
from otse.transceiver_models import OrderableVariant, TransceiverSpecs

logger = logging.getLogger(__name__)

_LIST_FIELDS: set[str] = {
    f for f, info in TransceiverSpecs.model_fields.items()
    if "list" in str(info.annotation).lower()
}


def _coerce_types(raw: dict[str, Any]) -> dict[str, Any]:
    """Normalize scalar/list mismatches before Pydantic validation."""
    for key, value in list(raw.items()):
        if value is None:
            continue
        if key in _LIST_FIELDS:
            if not isinstance(value, list):
                raw[key] = [value]
        elif key == "penalties":
            if isinstance(value, dict):
                raw["penalties"] = [value]
        else:
            if isinstance(value, list) and len(value) == 1:
                raw[key] = value[0]

    if isinstance(raw.get("penalties"), list):
        raw["penalties"] = _normalize_penalties(raw["penalties"])

    _coerce_variant_lists(raw)
    normalize_quantities(raw)
    return raw


def _expand_penalty(item: dict[str, Any]) -> list[dict[str, Any]]:
    """Split a penalty whose values were given as lists into scalar penalty points.

    Equal-length lists are zipped (row-wise); a lone multi-valued list is fanned out.
    """
    conds = item.get("conditions")
    if isinstance(conds, dict):
        conds = [conds]
    conds = [c for c in conds or [] if isinstance(c, dict)]

    pv = item.get("penalized_value")
    pv_list = pv if isinstance(pv, list) else [pv]
    cond_lists = [c.get("value") if isinstance(c.get("value"), list) else [c.get("value")] for c in conds]

    n = max([len(pv_list), *map(len, cond_lists)], default=1) or 1

    def pick(values: list, i: int):
        if not values:
            return None
        return values[i] if len(values) == n else values[0] if len(values) == 1 else None

    points = []
    for i in range(n):
        point = {k: v for k, v in item.items() if k not in ("penalized_value", "conditions")}
        point["penalized_value"] = pick(pv_list, i)
        point["conditions"] = [
            {**c, "value": pick(vals, i)} for c, vals in zip(conds, cond_lists)
        ]
        if any(c["value"] is None for c in point["conditions"]):
            logger.warning("Dropping ambiguous penalty (mismatched list lengths): %s", item)
            return []
        points.append(point)
    return points


def _normalize_penalties(items: list[Any]) -> list[dict[str, Any]]:
    """Scalarize penalty points.

    A point with a penalty magnitude and no degraded value is kept. Conditions
    are optional.
    """
    out: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if item.get("conditions") is None:
            item["conditions"] = []
        for point in _expand_penalty(item):
            if point.get("conditions") is None:
                point["conditions"] = []
            out.append(point)
    return out


def _coerce_variant_lists(raw: dict[str, Any]) -> None:
    """Wrap scalar variant fields the same way top-level list fields are wrapped."""
    variants = raw.get("variants")
    if isinstance(variants, dict):
        variants = [variants]
        raw["variants"] = variants
    if not isinstance(variants, list):
        return
    list_fields = {
        name
        for name, info in OrderableVariant.model_fields.items()
        if "list" in str(info.annotation).lower()
    }
    for variant in variants:
        if not isinstance(variant, dict):
            continue
        for key, value in list(variant.items()):
            if value is not None and key in list_fields and not isinstance(value, list):
                variant[key] = [value]


SYSTEM_PROMPT = EXTRACTION_SYSTEM_PROMPT
USER_PROMPT_TEMPLATE = EXTRACTION_USER_PROMPT_TEMPLATE

BASE_URL = "http://127.0.0.1:8080"

def _truncate(text: str, max_chars: int = 120_000) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n\n[...truncated...]"


def _extract_headings(md_text: str) -> str:
    """Return a newline-separated list of markdown headings found in the text."""
    headings = [
        line.strip() for line in md_text.splitlines()
        if re.match(r"^#{1,6}\s+", line)
    ]
    return "\n".join(headings) if headings else "(none found)"


def _parse_json_from_response(raw: str) -> Any:
    """Extract JSON dict from LLM response, handling fences and preamble."""
    s = raw.strip()
    # Strip markdown fences
    m = re.search(r"```(?:json)?\s*\n?(.*?)```", s, re.DOTALL)
    if m:
        s = m.group(1).strip()
    try:
        v = json.loads(s)
        if isinstance(v, dict):
            return v
    except json.JSONDecodeError:
        pass
    # Fallback: find first { to last }
    start = s.find("{")
    end = s.rfind("}")
    if start >= 0 and end > start:
        try:
            return json.loads(s[start : end + 1])
        except json.JSONDecodeError:
            pass
    return {}


def extract_atoms(
    parsed: ParsedDatasheet,
    *,
    model_id: str | None = None,
    max_chars: int = 120_000,
    base_url: str = BASE_URL,
    temperature: float = 0.1,
    max_tokens: int = 16384,
) -> tuple[TransceiverSpecs | None, dict[str, Any]]:
    """Run LLM extraction and return (validated_specs, raw_dict).

    Returns (None, raw_dict) if validation fails but JSON was parsed.
    Returns (None, {}) on total failure.
    """
    client = OpenAI(base_url=f"{base_url}/v1", api_key="no-key", timeout=600.0)

    content = _truncate(parsed.markdown or parsed.full_text, max_chars)
    schema_text = extraction_schema_text()
    headings = _extract_headings(parsed.markdown or parsed.full_text)
    prompt = USER_PROMPT_TEMPLATE.format(schema=schema_text, headings=headings, content=content)

    # Auto-detect model if not specified
    if not model_id:
        models_resp = client.models.list()
        model_id = models_resp.data[0].id if models_resp.data else "default"

    logger.info("Extracting atoms: %d chars content, model=%s", len(content), model_id)

    response = client.chat.completions.create(
        model=model_id,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    choice = response.choices[0]
    raw_response = choice.message.content or ""

    # Thinking models may put output in reasoning_content if content is empty
    if not raw_response.strip():
        reasoning = getattr(choice.message, "reasoning_content", None) or ""
        if reasoning:
            logger.info("Content empty, checking reasoning_content (%d chars)", len(reasoning))
            raw_response = reasoning

    if not raw_response.strip():
        logger.error("LLM returned completely empty response (finish_reason=%s)", choice.finish_reason)
        return None, {}

    raw_dict = _parse_json_from_response(raw_response)

    if not isinstance(raw_dict, dict):
        logger.error("LLM returned non-dict: %s", type(raw_dict))
        return None, {}

    raw_dict = _coerce_types(raw_dict)

    table_penalties = extract_table_penalties(parsed.markdown or parsed.full_text or "")
    if table_penalties:
        raw_dict["penalties"] = merge_penalties(table_penalties, raw_dict.get("penalties"))
        logger.info("Penalties: %d from tables, %d total after merge",
                    len(table_penalties), len(raw_dict["penalties"]))

    try:
        specs = TransceiverSpecs.model_validate(raw_dict)
        logger.info("Extraction validated successfully.")
        return specs, raw_dict
    except ValidationError as exc:
        logger.warning("Validation failed: %s", exc.error_count())
        for err in exc.errors():
            logger.debug("  %s: %s", err["loc"], err["msg"])
        return None, raw_dict
