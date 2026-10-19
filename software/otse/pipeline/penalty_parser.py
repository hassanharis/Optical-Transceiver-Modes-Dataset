"""Deterministic penalty extraction from markdown tables.

Datasheets express penalties in an "@" notation that LLMs often misread:

* Column style: header ``Rx OSNR @0.5dB penalty`` with cells like ``24.2dB@-14dBm``
  -> penalized OSNR 24.2 dB at Rx power -14 dBm, penalty 0.5 dB.
* Inline style: cell ``26.5dB@-14dBm & 0.5dB penalty`` under a row labelled
  ``OSNR tolerance 400G``.

Every table row is expanded into one penalty point, tagged with a ``source``
string (section + row key) so mode linking can bind it to the right mode.
"""

from __future__ import annotations

import re
from typing import Any

_NUM = r"[-+]?\d+(?:\.\d+)?"

_HEADER_PENALTY_RE = re.compile(rf"@\s*({_NUM})\s*dB\s*penalty", re.I)
_VALUE_AT_COND_RE = re.compile(
    rf"({_NUM})\s*dB(?!m)\s*@\s*({_NUM})\s*(dBm|ps/nm|ps)\b", re.I
)
_INLINE_PENALTY_RE = re.compile(
    rf"({_NUM})\s*dB(?!m)\s*@\s*({_NUM})\s*(dBm|ps/nm|ps)\b[^|]*?({_NUM})\s*dB\s*penalty",
    re.I,
)

_UNIT_TO_CONDITION = {
    "dbm": "rx_power_dbm",
    "ps/nm": "chromatic_dispersion_ps_nm",
    "ps": "pmd_ps",
}


def _clean(cell: str) -> str:
    cell = re.sub(r"<br\s*/?>", " ", cell, flags=re.I)
    cell = cell.replace("**", "")
    return re.sub(r"\s+", " ", cell).strip()


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [_clean(c) for c in line.split("|")]


def _is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells)


def _target_for(label: str) -> str | None:
    text = label.lower()
    if "osnr" in text:
        return "rx_osnr_db"
    if "sens" in text:
        return "rx_sensitivity_dbm"
    return None


def _point(target: str, penalty: str, value: str, cond_value: str, unit: str, source: str) -> dict[str, Any]:
    return {
        "target_parameter": target,
        "penalty_db": float(penalty),
        "penalized_value": float(value),
        "conditions": [
            {"parameter": _UNIT_TO_CONDITION[unit.lower()], "value": float(cond_value)}
        ],
        "source": source,
    }


def _iter_tables(md_text: str):
    """Yield (section_heading, rows) for each markdown table."""
    section = ""
    rows: list[list[str]] = []
    for line in md_text.splitlines():
        heading = re.match(r"^#{1,6}\s+(.+)$", line.strip())
        if heading:
            if rows:
                yield section, rows
                rows = []
            section = heading.group(1).strip()
            continue
        if line.strip().startswith("|"):
            cells = _split_row(line)
            if not _is_separator(cells):
                rows.append(cells)
        elif rows:
            yield section, rows
            rows = []
    if rows:
        yield section, rows


def extract_table_penalties(md_text: str) -> list[dict[str, Any]]:
    """Return penalty points found in markdown tables (column and inline styles)."""
    points: list[dict[str, Any]] = []

    for section, rows in _iter_tables(md_text):
        header, body = rows[0], rows[1:]

        # Column style: header carries the penalty, cells carry value@condition.
        penalty_cols = {}
        for idx, title in enumerate(header):
            m = _HEADER_PENALTY_RE.search(title)
            target = _target_for(title)
            if m and target:
                penalty_cols[idx] = (m.group(1), target)

        for row in body:
            row_key = f"{header[0]}={row[0]}" if header and row and row[0] else ""
            for idx, (penalty, target) in penalty_cols.items():
                if idx >= len(row):
                    continue
                m = _VALUE_AT_COND_RE.search(row[idx])
                if m:
                    source = " | ".join(p for p in (section, row_key) if p)
                    points.append(_point(target, penalty, m.group(1), m.group(2), m.group(3), source))

        # Inline style: "26.5dB@-14dBm & 0.5dB penalty"; labels carry forward to blank rows.
        label = ""
        for row in rows:
            first_text = next((c for c in row if c), "")
            if first_text and not _VALUE_AT_COND_RE.search(first_text):
                label = first_text
            target = _target_for(label)
            if not target:
                continue
            for cell in row:
                for m in _INLINE_PENALTY_RE.finditer(cell):
                    source = " | ".join(p for p in (section, label) if p)
                    points.append(
                        _point(target, m.group(4), m.group(1), m.group(2), m.group(3), source)
                    )

    return points


def _signature(point: dict[str, Any]) -> tuple:
    conds = tuple(
        sorted(
            (c.get("parameter"), c.get("value"))
            for c in point.get("conditions") or []
            if isinstance(c, dict)
        )
    )
    return (point.get("target_parameter"), point.get("penalty_db"), point.get("penalized_value"), conds)


def merge_penalties(
    table_points: list[dict[str, Any]], llm_points: list[dict[str, Any]] | None
) -> list[dict[str, Any]]:
    """Table-derived points win; keep LLM points only when they add new information."""
    merged = list(table_points)
    seen = {_signature(p) for p in table_points}
    for point in llm_points or []:
        if isinstance(point, dict) and _signature(point) not in seen:
            seen.add(_signature(point))
            merged.append(point)
    return merged
