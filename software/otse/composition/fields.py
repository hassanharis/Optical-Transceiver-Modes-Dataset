"""Discover schema fields and categorical literals from corpus JSON."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Iterable

from otse.composition.field_replacer import default_config, replace_scalar
from otse.composition.loader import CorpusRecord

SKIP_SPEC_KEYS = frozenset(
    {
        "notes",
        "suggestions",
        "provenance_datasheet_sections",
        "penalties",
        "frame",
    }
)


class RecordLevel(str, Enum):
    MODULE = "module"
    MODE = "mode"


class FieldKind(str, Enum):
    CATEGORICAL = "categorical"
    NUMERIC = "numeric"
    BOOLEAN = "boolean"
    COMPLEX = "complex"


@dataclass(frozen=True)
class FieldInfo:
    name: str
    level: RecordLevel
    kind: FieldKind
    literal_count: int = 0


def _is_scalar(value: Any) -> bool:
    return value is None or isinstance(value, (str, int, float, bool))


def canonicalize_literal(field_name: str | None, literal: str) -> str:
    """Map a display literal using the harmonization lexicon."""
    if field_name is None:
        return literal
    config = default_config()
    if not config.has_field(field_name):
        return literal
    return replace_scalar(field_name, literal, config)


def normalize_fiber_type_value(value: Any) -> Any:
    """Normalize ``fiber_type`` using the shared replacement config."""
    from otse.composition.field_replacer import replace_field_value

    return replace_field_value("fiber_type", value, default_config())


def _normalize_literal(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        text = value.strip()
        return text if text else None
    return None


def iter_field_values(
    record: CorpusRecord,
    field_name: str,
    level: RecordLevel,
) -> Iterable[Any]:
    if level == RecordLevel.MODULE:
        if field_name in record.meta:
            yield record.meta[field_name]
            return
        if field_name in record.specs:
            yield record.specs[field_name]
        return

    for mode in record.modes:
        if field_name in mode:
            yield mode[field_name]


def expand_literals(value: Any, field_name: str | None = None) -> list[str]:
    """Turn a JSON value into zero or more display literals for filtering."""
    if value is None:
        return []
    if isinstance(value, list):
        out: list[str] = []
        for item in value:
            out.extend(expand_literals(item, field_name))
        return out
    lit = _normalize_literal(value)
    if lit is not None:
        lit = canonicalize_literal(field_name, lit)
    return [lit] if lit is not None else []


def classify_values(values: Iterable[Any]) -> FieldKind:
    kinds: set[FieldKind] = set()
    for raw in values:
        if raw is None:
            continue
        if isinstance(raw, bool):
            kinds.add(FieldKind.BOOLEAN)
        elif isinstance(raw, (int, float)) and not isinstance(raw, bool):
            kinds.add(FieldKind.NUMERIC)
        elif isinstance(raw, str):
            kinds.add(FieldKind.CATEGORICAL)
        elif isinstance(raw, list):
            if not raw:
                continue
            if all(_is_scalar(x) for x in raw):
                if any(isinstance(x, (int, float)) and not isinstance(x, bool) for x in raw):
                    kinds.add(FieldKind.NUMERIC)
                if any(isinstance(x, str) for x in raw):
                    kinds.add(FieldKind.CATEGORICAL)
            else:
                kinds.add(FieldKind.COMPLEX)
        else:
            kinds.add(FieldKind.COMPLEX)

    if FieldKind.COMPLEX in kinds:
        return FieldKind.COMPLEX
    if FieldKind.CATEGORICAL in kinds:
        return FieldKind.CATEGORICAL
    if FieldKind.NUMERIC in kinds:
        return FieldKind.NUMERIC
    if FieldKind.BOOLEAN in kinds:
        return FieldKind.BOOLEAN
    return FieldKind.COMPLEX


def discover_fields(
    records: list[CorpusRecord],
    *,
    include_meta: bool = True,
) -> list[FieldInfo]:
    """Collect all field names seen in specs, meta, or mode objects."""
    module_keys: set[str] = set()
    mode_keys: set[str] = set()

    for rec in records:
        module_keys.update(rec.specs.keys())
        if include_meta:
            module_keys.update(rec.meta.keys())
        for mode in rec.modes:
            mode_keys.update(mode.keys())

    module_keys -= SKIP_SPEC_KEYS

    fields: list[FieldInfo] = []
    for name in sorted(module_keys):
        values = []
        for rec in records:
            values.extend(iter_field_values(rec, name, RecordLevel.MODULE))
        kind = classify_values(values)
        literals = set()
        if kind == FieldKind.CATEGORICAL:
            for rec in records:
                for raw in iter_field_values(rec, name, RecordLevel.MODULE):
                    literals.update(expand_literals(raw, name))
        fields.append(
            FieldInfo(
                name=name,
                level=RecordLevel.MODULE,
                kind=kind,
                literal_count=len(literals),
            )
        )

    for name in sorted(mode_keys):
        values = []
        for rec in records:
            values.extend(iter_field_values(rec, name, RecordLevel.MODE))
        kind = classify_values(values)
        literals = set()
        if kind == FieldKind.CATEGORICAL:
            for rec in records:
                for raw in iter_field_values(rec, name, RecordLevel.MODE):
                    literals.update(expand_literals(raw, name))
        fields.append(
            FieldInfo(
                name=name,
                level=RecordLevel.MODE,
                kind=kind,
                literal_count=len(literals),
            )
        )

    return fields


def field_literals(
    records: list[CorpusRecord],
    field_name: str,
    level: RecordLevel,
) -> list[str]:
    """Sorted unique literals for a categorical (or numeric-as-string) field."""
    literals: set[str] = set()
    for rec in records:
        for raw in iter_field_values(rec, field_name, level):
            literals.update(expand_literals(raw, field_name))
    return sorted(literals, key=lambda s: (len(s), s.lower()))
