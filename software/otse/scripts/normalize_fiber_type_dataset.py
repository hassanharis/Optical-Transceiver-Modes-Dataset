#!/usr/bin/env python3
"""Deprecated: use python -m otse.scripts.apply_field_replacements."""

from __future__ import annotations

from otse.scripts.apply_field_replacements import main as apply_replacements


def main() -> None:
    print("Note: normalize_fiber_type_dataset.py delegates to apply_field_replacements.py")
    apply_replacements()


if __name__ == "__main__":
    main()
