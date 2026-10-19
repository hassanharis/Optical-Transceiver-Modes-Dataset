"""Step 1: PDF parsing — text and table extraction from a datasheet PDF."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pymupdf
import pymupdf4llm

logger = logging.getLogger(__name__)


@dataclass
class ParsedPage:
    index: int
    text: str


@dataclass
class ParsedTable:
    page_index: int
    bbox: tuple[float, float, float, float]
    rows: list[list[str]] = field(default_factory=list)
    label: str | None = None


@dataclass
class ParsedDatasheet:
    """Container for all extracted content from a single PDF."""

    source_path: Path
    pages: list[ParsedPage] = field(default_factory=list)
    tables: list[ParsedTable] = field(default_factory=list)
    markdown: str = ""

    @property
    def full_text(self) -> str:
        return "\n\n".join(p.text for p in self.pages)

    @property
    def page_count(self) -> int:
        return len(self.pages)


def parse_pdf(path: str | Path) -> ParsedDatasheet:
    """Parse a PDF file and return structured content."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    doc = pymupdf.open(str(path))
    try:
        result = ParsedDatasheet(source_path=path)

        # Extract per-page text
        for page in doc:
            try:
                text = page.get_text("text")
            except Exception as exc:
                logger.warning("Page %d text extraction failed: %s", page.number, exc)
                text = ""
            result.pages.append(ParsedPage(index=page.number, text=text))

        # Extract markdown (best for LLM consumption)
        try:
            result.markdown = pymupdf4llm.to_markdown(doc)
        except Exception as exc:
            logger.warning("Markdown extraction failed: %s", exc)
            result.markdown = result.full_text

        # Extract tables
        for page_index, page in enumerate(doc):
            try:
                finder = page.find_tables()
                tables = getattr(finder, "tables", finder) or []
                for t in tables:
                    raw_rows = t.extract()
                    rows = _clean_rows(raw_rows)
                    if rows:
                        result.tables.append(ParsedTable(
                            page_index=page_index,
                            bbox=tuple(t.bbox),
                            rows=rows,
                            label=_find_table_label(page, t.bbox),
                        ))
            except Exception as exc:
                logger.warning("Table extraction page %d failed: %s", page_index, exc)

        logger.info(
            "Parsed %s: %d pages, %d tables, %d chars markdown",
            path.name, result.page_count, len(result.tables), len(result.markdown),
        )
        return result
    finally:
        doc.close()


def _clean_rows(grid: list[list[Any]]) -> list[list[str]]:
    if not grid:
        return []
    rows = [
        [("" if c is None else str(c).replace("\n", " ").strip()) for c in row]
        for row in grid
    ]
    rows = [r for r in rows if any(c for c in r)]
    return rows


def _find_table_label(page: Any, bbox: tuple) -> str | None:
    import re
    try:
        text = page.get_text("text")
    except Exception:
        return None
    matches = re.findall(r"(Table\s+\d+[-.\u2013]\d+[A-Za-z]?)", text)
    return matches[-1] if matches else None

