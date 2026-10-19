"""Entry point: parse PDF → extract atomic params → store run."""

from __future__ import annotations

import argparse
import logging
import time
from pathlib import Path

from otse.pipeline.pdf_parser import parse_pdf
from otse.pipeline.atom_extractor import extract_atoms
from otse.pipeline.runtime_store import store_run, update_run_timings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def run(
    pdf_path: str | Path,
    *,
    model_id: str | None = None,
    runs_dir: Path | None = None,
) -> Path:
    """Execute the full pipeline and return the run directory."""
    pipeline_started = time.perf_counter()
    timings: dict[str, float] = {}

    logger.info("=== Step 1: Parsing PDF ===")
    stage_started = time.perf_counter()
    parsed = parse_pdf(pdf_path)
    timings["parse_pdf"] = time.perf_counter() - stage_started
    logger.info("Step 1 completed in %.3f seconds", timings["parse_pdf"])

    logger.info("=== Step 2: Extracting atomic parameters ===")
    stage_started = time.perf_counter()
    specs, raw_dict = extract_atoms(parsed, model_id=model_id)
    timings["extract_atoms"] = time.perf_counter() - stage_started
    logger.info("Step 2 completed in %.3f seconds", timings["extract_atoms"])

    logger.info("=== Step 3: Storing run ===")
    stage_started = time.perf_counter()
    run_dir = store_run(
        parsed,
        raw_dict,
        specs,
        model_id=model_id,
        runs_dir=runs_dir,
        timings_seconds=timings,
    )
    timings["store_run"] = time.perf_counter() - stage_started
    timings["total"] = time.perf_counter() - pipeline_started
    update_run_timings(run_dir, timings)
    logger.info("Step 3 completed in %.3f seconds", timings["store_run"])

    status = "VALID" if specs else "PARTIAL (validation failed)"
    logger.info(
        "=== Done [%s] in %.3f seconds — results in %s ===", status, timings["total"], run_dir
    )
    return run_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract transceiver specs from a PDF datasheet.")
    parser.add_argument("pdf", help="Path to the PDF datasheet")
    parser.add_argument("--model", default=None, help="Model ID on the llama-server router")
    parser.add_argument("--runs-dir", default=None, help="Directory to store runs")
    args = parser.parse_args()

    runs_dir = Path(args.runs_dir) if args.runs_dir else None
    run_dir = run(args.pdf, model_id=args.model, runs_dir=runs_dir)
    print(f"Run saved: {run_dir}")


if __name__ == "__main__":
    main()
