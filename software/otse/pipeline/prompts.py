"""Extraction and mode-linking prompts.

``extraction_schema_text()`` renders ``TransceiverSpecs`` and omits
pipeline-derived canonical fields.
"""

from __future__ import annotations

import json
from typing import Any

from otse.transceiver_models import DERIVED_FIELDS, TransceiverSpecs

EXTRACTION_SYSTEM_PROMPT = """\
You are an optical-network transceiver datasheet extraction engine.
Extract only values explicitly printed for this module and return JSON for the schema.

Rules:
- Copy every number and unit exactly as printed. Do not convert, scale, or round.
- If a value is absent, use null. Absence does not mean the capability is unsupported.
- Do not infer vendor, FEC type, fiber, emitter, photodetector, or interface IDs
  from a standard, logo, URL, or footer.
- Fill vendor only when the datasheet explicitly names the manufacturer.
- Examples in descriptions are not closed lists. Store the printed form factor,
  connector, media, and modulation even when the example list omits them.
- Ordering-information and part-number tables are in scope. A value printed on
  one orderable row goes on that variant only.
- Use module temperature, reach, bit rate, and wavelength only when one value
  applies to every part. When grades or part numbers differ, fill variants and
  leave the module copies null.
- Put transmit and receive wavelengths in the tx and rx fields. Use the unscoped
  wavelength fields only when one range covers both directions.
- Average power, OMA, and optical power budget are different measurements.
  Power budget is not channel insertion loss and not transmitter power.
- Store a dBm field only when the printed unit is dBm. For dB, µW, or mW, leave
  the dBm field null and copy the printed statement into notes.
- A formula, such as "-6.5 + TECQ", is not a float. Leave the numeric field null
  and copy the expression into notes.
- comparator is eq for a plain number, lt for "<", le for "<=", gt for ">",
  and ge for ">=". statistic is min, typ, or max only when that label is printed.
- For a minimum/typical/maximum row, store the minimum and the maximum.
  Store a typical value only when it is the only value printed.
- For list fields, collect the distinct printed values. Do not merge part numbers
  into one range.
- "@" means the value before it was measured at the condition after it.
  "26dB@-12dBm" in an OSNR row is OSNR 26 dB at receiver power -12 dBm.
- A penalty needs a printed magnitude in dB. Add penalized_value or conditions
  only when they are printed. A dispersion or path penalty given only as a
  maximum in dB is still a penalty point.
- Put TDECQ, TECQ, and TDP measurements in tdecq_db, tecq_db, and tdp_db.
- Do not invent hex interface IDs or MSA names that are not printed.
- notes is for ambiguity, brand conflict, formulas, and conditions.
  suggestions is only for a printed value that cannot be stored without
  changing its meaning. Do not list absent parameters in either field.
- provenance_datasheet_sections names the headings that supplied values,
  including ordering information when that table was used.
- Return only valid JSON matching the schema. No commentary outside the JSON.
- Join text split across lines inside one table cell with a space.
- When both an acronym and its full form appear, store one of them.

Printed reach of 500 m:
{"value": 500, "unit": "m", "comparator": "eq", "statistic": "max"}

Consumption printed as "< 1 W":
{"value": 1, "unit": "W", "comparator": "lt", "statistic": "max"}

Dispersion penalty printed only as 2 dB:
{"target_parameter": "dispersion_penalty_db", "penalty_db": 2,
 "penalized_value": null, "conditions": [],
 "source": "Optical characteristics | Dispersion penalty"}
"""

EXTRACTION_USER_PROMPT_TEMPLATE = """\
## Target Schema

{schema}

## Section Headings

{headings}

## Datasheet Content

{content}

---

Extract all parameters into the JSON schema above. Return only the JSON object.
"""

LINKING_SYSTEM_PROMPT = """\
You group extracted optical-transceiver parameters into selectable operating modes.
Each mode is one configuration whose values co-occur in the source: one table row,
one application code, or one host-to-media binding.

An orderable variant is already bound to its part number. It is not a mode.
Do not create a mode only to represent a temperature grade or a part number.

Rules:
- Assign values to a mode only when the datasheet shows that they co-occur.
- Copy extracted values unchanged, including printed number objects.
  Do not convert units.
- Several interfaces may belong to one mode.
- When both amplified and unamplified values are printed, make separate modes.
- Keep a penalty with the mode identified by its source. Copy the penalty object
  unchanged, including one that has no penalized value or no conditions.
- Do not add interface IDs, FEC types, or any value missing from the extracted
  parameters and the datasheet.
- Set variant_model only when a row ties that mode to one part number.
  Otherwise use null.
- Return only JSON matching the output schema.
"""

LINKING_USER_PROMPT_TEMPLATE = """\
## Module and variant context

```json
{context}
```

## Multi-valued parameters to group

```json
{atoms}
```

## Original Datasheet Content

{content}

---

## Output Schema

Return a JSON object:
```json
{{
  "modes": [
    {{
      "label": "<short mode name>",
      "variant_model": "<part number, or null>",
      {field_template}
    }}
  ]
}}
```

Group the multi-valued parameters into modes. Return only the JSON.
"""


def _is_derived(info: dict[str, Any]) -> bool:
    return info.get("filled_by") == "pipeline"


def _format_type(info: dict[str, Any]) -> str:
    """Render a JSON-schema node as a short type name."""
    if _is_derived(info):
        return ""
    if "$ref" in info:
        return info["$ref"].split("/")[-1]
    if "enum" in info:
        values = ", ".join(repr(value) for value in info["enum"])
        return f"enum[{values}]"
    if "anyOf" in info:
        options = [
            _format_type(option)
            for option in info["anyOf"]
            if option.get("type") != "null"
        ]
        options = [option for option in options if option]
        return " | ".join(options) if options else "any"
    type_name = info.get("type")
    if type_name == "array":
        return f"list[{_format_type(info.get('items', {}))}]"
    return {"number": "float", "integer": "int", "string": "string", "boolean": "bool"}.get(
        type_name or "",
        type_name or "any",
    )


def _definition_text(name: str, schema: dict[str, Any]) -> dict[str, str]:
    properties = schema.get("$defs", {}).get(name, {}).get("properties", {})
    rendered: dict[str, str] = {}
    for field_name, info in properties.items():
        if field_name in DERIVED_FIELDS or _is_derived(info):
            continue
        description = info.get("description", "")
        type_name = _format_type(info)
        rendered[field_name] = f"{type_name} — {description}" if description else type_name
    return rendered


def _referenced_definitions(type_name: str, schema: dict[str, Any], seen: list[str]) -> None:
    for name in schema.get("$defs", {}):
        if name in type_name and name not in seen:
            seen.append(name)
            nested = " ".join(_definition_text(name, schema).values())
            _referenced_definitions(nested, schema, seen)


def extraction_schema_text() -> str:
    """Return the schema text inserted into the extraction prompt."""
    schema = TransceiverSpecs.model_json_schema()
    compact: dict[str, str] = {}
    for name, info in schema.get("properties", {}).items():
        if name in DERIVED_FIELDS or _is_derived(info):
            continue
        description = info.get("description", "")
        type_name = _format_type(info)
        compact[name] = f"{type_name} — {description}" if description else type_name

    referenced: list[str] = []
    _referenced_definitions(" ".join(compact.values()), schema, referenced)
    sections = [json.dumps(compact, ensure_ascii=False, indent=2)]
    definition_order = ("PrintedNumber", "PenaltyCondition", "PenaltyPoint", "OrderableVariant")
    for name in definition_order:
        if name not in referenced:
            continue
        body = json.dumps(_definition_text(name, schema), ensure_ascii=False, indent=2)
        sections.append(f"## {name}\n\n{body}")
    return "\n\n".join(sections)
