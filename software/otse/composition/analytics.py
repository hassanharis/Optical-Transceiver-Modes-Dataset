"""Composition statistics and filtering."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from statistics import mean, median
from typing import Any, Literal

from otse.composition.fields import (
    RecordLevel,
    expand_literals,
    iter_field_values,
)
from otse.composition.loader import CorpusRecord

CountMode = Literal["module", "mention"]


@dataclass
class OverviewStats:
    n_runs_total: int
    n_modules: int
    n_modes: int
    validation_passed: int
    page_count_median: float | None
    page_count_mean: float | None
    table_count_median: float | None
    table_count_mean: float | None
    modes_per_module_median: float | None


def composition_overview(
    records: list[CorpusRecord],
    *,
    total_run_folders: int | None = None,
) -> OverviewStats:
    pages = [r.meta.get("page_count") for r in records if isinstance(r.meta.get("page_count"), (int, float))]
    tables = [r.meta.get("table_count") for r in records if isinstance(r.meta.get("table_count"), (int, float))]
    passed = sum(1 for r in records if r.meta.get("validation_passed") is True)
    mode_counts = [len(r.modes) for r in records]

    return OverviewStats(
        n_runs_total=total_run_folders if total_run_folders is not None else len(records),
        n_modules=len(records),
        n_modes=sum(mode_counts),
        validation_passed=passed,
        page_count_median=float(median(pages)) if pages else None,
        page_count_mean=float(mean(pages)) if pages else None,
        table_count_median=float(median(tables)) if tables else None,
        table_count_mean=float(mean(tables)) if tables else None,
        modes_per_module_median=float(median(mode_counts)) if mode_counts else None,
    )


def _record_has_literal(
    record: CorpusRecord,
    field_name: str,
    level: RecordLevel,
    selected: set[str],
) -> bool:
    for raw in iter_field_values(record, field_name, level):
        if selected.intersection(expand_literals(raw, field_name)):
            return True
    return False


def filter_records(
    records: list[CorpusRecord],
    filters: dict[tuple[str, RecordLevel], set[str]],
) -> list[CorpusRecord]:
    """Keep modules matching all field filters (AND). Empty set = no filter for that field."""
    if not filters:
        return list(records)

    active = {k: v for k, v in filters.items() if v}
    if not active:
        return list(records)

    out: list[CorpusRecord] = []
    for rec in records:
        if all(_record_has_literal(rec, name, level, vals) for (name, level), vals in active.items()):
            out.append(rec)
    return out


def literal_counts(
    records: list[CorpusRecord],
    field_name: str,
    level: RecordLevel,
    *,
    count_mode: CountMode = "module",
) -> Counter[str]:
    """
    Count literal frequencies.

    ``module``: each datasheet counts at most once per literal (if any value matches).
    ``mention``: each list element / scalar occurrence counts separately.
    """
    counts: Counter[str] = Counter()
    for rec in records:
        seen_in_record: set[str] = set()
        for raw in iter_field_values(rec, field_name, level):
            lits = expand_literals(raw, field_name)
            if count_mode == "mention":
                for lit in lits:
                    counts[lit] += 1
            else:
                seen_in_record.update(lits)
        if count_mode == "module":
            for lit in seen_in_record:
                counts[lit] += 1
    return counts


def field_coverage(
    records: list[CorpusRecord],
    field_name: str,
    level: RecordLevel,
) -> dict[str, Any]:
    n = len(records)
    if n == 0:
        return {"field": field_name, "level": level.value, "n_modules": 0, "coverage_pct": 0.0}

    if level == RecordLevel.MODE:
        with_value = sum(
            1
            for rec in records
            if any(
                expand_literals(mode.get(field_name), field_name)
                for mode in rec.modes
                if field_name in mode
            )
        )
    else:
        with_value = sum(
            1
            for rec in records
            if expand_literals(rec.specs.get(field_name), field_name) or expand_literals(
                rec.meta.get(field_name), field_name
            )
        )

    return {
        "field": field_name,
        "level": level.value,
        "n_modules": n,
        "with_value": with_value,
        "coverage_pct": round(100.0 * with_value / n, 2),
    }


def coverage_table(
    records: list[CorpusRecord],
    fields: list[tuple[str, RecordLevel]],
) -> list[dict[str, Any]]:
    return [field_coverage(records, name, level) for name, level in fields]


def cross_tab(
    records: list[CorpusRecord],
    field_a: str,
    level_a: RecordLevel,
    field_b: str,
    level_b: RecordLevel,
    *,
    count_mode: CountMode = "module",
    top_a: int = 12,
    top_b: int = 12,
) -> tuple[list[str], list[str], list[list[int]]]:
    """Pivot counts for two categorical fields (top-N literals per axis)."""
    ca = literal_counts(records, field_a, level_a, count_mode=count_mode)
    cb = literal_counts(records, field_b, level_b, count_mode=count_mode)
    rows = [k for k, _ in ca.most_common(top_a)]
    cols = [k for k, _ in cb.most_common(top_b)]
    matrix = [[0 for _ in cols] for _ in rows]

    for rec in records:
        la = set()
        lb = set()
        for raw in iter_field_values(rec, field_a, level_a):
            la.update(expand_literals(raw, field_a))
        for raw in iter_field_values(rec, field_b, level_b):
            lb.update(expand_literals(raw, field_b))
        la = {x for x in la if x in rows}
        lb = {x for x in lb if x in cols}
        if count_mode == "module":
            for a in la:
                for b in lb:
                    matrix[rows.index(a)][cols.index(b)] += 1
        else:
            for raw in iter_field_values(rec, field_a, level_a):
                for a in expand_literals(raw, field_a):
                    if a not in rows:
                        continue
                    for raw_b in iter_field_values(rec, field_b, level_b):
                        for b in expand_literals(raw_b, field_b):
                            if b in cols:
                                matrix[rows.index(a)][cols.index(b)] += 1
    return rows, cols, matrix


def numeric_summary(
    records: list[CorpusRecord],
    field_name: str,
    level: RecordLevel,
) -> dict[str, float | int | None]:
    values: list[float] = []
    for rec in records:
        for raw in iter_field_values(rec, field_name, level):
            if isinstance(raw, (int, float)) and not isinstance(raw, bool):
                values.append(float(raw))
            elif isinstance(raw, list):
                for item in raw:
                    if isinstance(item, (int, float)) and not isinstance(item, bool):
                        values.append(float(item))
    if not values:
        return {"count": 0, "min": None, "max": None, "mean": None, "median": None}
    values.sort()
    return {
        "count": len(values),
        "min": values[0],
        "max": values[-1],
        "mean": float(mean(values)),
        "median": float(median(values)),
    }
