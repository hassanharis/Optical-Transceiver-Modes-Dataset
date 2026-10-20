"""Checks for the printed-unit schema and the extraction pipeline helpers."""

from __future__ import annotations

import unittest

from otse.composition.fields import FieldKind, classify_values, expand_literals
from otse.pipeline.atom_extractor import _coerce_types
from otse.pipeline.mode_linker import separate_atoms
from otse.pipeline.penalty_parser import extract_table_penalties
from otse.pipeline.prompts import extraction_schema_text
from otse.pipeline.units import convert
from otse.scripts.build_inventory import discover_skus, resolve_mode_skus
from otse.transceiver_models import TransceiverSpecs


class UnitConversionTests(unittest.TestCase):
    def test_compatible_units_convert(self) -> None:
        self.assertEqual(convert(500, "m", "km"), 0.5)
        self.assertEqual(convert(1250, "Mb/s", "Gbps"), 1.25)
        self.assertEqual(convert(193.1, "THz", "THz"), 193.1)
        self.assertEqual(convert(100, "GHz", "THz"), 0.1)

    def test_incompatible_units_stay_empty(self) -> None:
        self.assertIsNone(convert(20, "nm", "GHz"))
        self.assertIsNone(convert(1, "dB", "W"))
        self.assertIsNone(convert(3, "dBm", "W"))


class ExtractionSchemaTests(unittest.TestCase):
    def test_prompt_schema_omits_derived_fields(self) -> None:
        text = extraction_schema_text()
        self.assertNotIn("canonical_value", text)
        self.assertNotIn("reach_km", text)
        self.assertIn('"reach": "list[PrintedNumber]', text)
        self.assertIn("## PrintedNumber", text)
        self.assertIn("## OrderableVariant", text)
        self.assertIn("## PenaltyPoint", text)

    def test_printed_values_and_penalty_magnitude_validate(self) -> None:
        raw = _coerce_types(
            {
                "reach": {
                    "value": 500,
                    "unit": "m",
                    "comparator": "eq",
                    "statistic": "max",
                },
                "power_consumption": {
                    "value": 1,
                    "unit": "W",
                    "comparator": "lt",
                    "statistic": "max",
                },
                "channel_spacing": {"value": 20, "unit": "nm"},
                "penalties": [
                    {
                        "target_parameter": "dispersion_penalty_db",
                        "penalty_db": 2,
                        "penalized_value": None,
                        "conditions": [],
                    }
                ],
                "variants": {
                    "model": "ABC-I",
                    "temp_grade": "I",
                    "temp_min_c": -40,
                    "temp_max_c": 85,
                    "bit_rate": {"value": 155, "unit": "Mbps"},
                },
            }
        )
        specs = TransceiverSpecs.model_validate(raw)
        assert specs.reach is not None
        assert specs.power_consumption is not None
        assert specs.channel_spacing is not None
        assert specs.penalties is not None
        assert specs.variants is not None
        self.assertEqual(specs.reach[0].canonical_value, 0.5)
        self.assertEqual(specs.reach[0].canonical_unit, "km")
        self.assertEqual(specs.power_consumption[0].comparator, "lt")
        self.assertEqual(specs.power_consumption[0].canonical_value, 1)
        self.assertIsNone(specs.channel_spacing[0].canonical_value)
        self.assertIsNone(specs.penalties[0].penalized_value)
        self.assertEqual(specs.penalties[0].conditions, [])
        self.assertEqual(specs.variants[0].bit_rate[0].canonical_value, 0.155)

    def test_variants_remain_module_context(self) -> None:
        multi, general = separate_atoms(
            {
                "vendor": "Acme",
                "suggestions": "schema note",
                "variants": [{"model": "A"}, {"model": "B"}],
                "bit_rate": [
                    {"value": 1, "unit": "Gbps"},
                    {"value": 10, "unit": "Gbps"},
                ],
            }
        )
        self.assertIn("bit_rate", multi)
        self.assertIn("variants", general)
        self.assertNotIn("variants", multi)


class PenaltyParserTests(unittest.TestCase):
    def test_magnitude_and_conditioned_penalties(self) -> None:
        markdown = """
## Optical

| Parameter | Value |
| --- | --- |
| Dispersion penalty | 2 dB |
| Path penalty | 1.5 dB |
| Transmitter and dispersion penalty | 3 dB |

| Appl | Rx OSNR @0.5dB penalty |
| --- | --- |
| 4 | 24.2dB@-14dBm |
"""
        found = {
            (point["target_parameter"], point["penalty_db"], point["penalized_value"])
            for point in extract_table_penalties(markdown)
        }
        self.assertIn(("dispersion_penalty_db", 2.0, None), found)
        self.assertIn(("path_penalty_db", 1.5, None), found)
        self.assertIn(("rx_osnr_db", 0.5, 24.2), found)
        self.assertFalse(any(item[0] == "tdp_db" for item in found))


class CompositionTests(unittest.TestCase):
    def test_printed_numbers_are_numeric_literals(self) -> None:
        value = [
            {
                "value": 500,
                "unit": "m",
                "canonical_value": 0.5,
                "canonical_unit": "km",
            }
        ]
        self.assertEqual(expand_literals(value), ["0.5 km"])
        self.assertEqual(classify_values([value]), FieldKind.NUMERIC)


class InventoryTests(unittest.TestCase):
    def test_orderable_variants_supply_skus(self) -> None:
        specs = {"variants": [{"model": "ABC-I"}, {"model": "ABC-C"}]}
        modes = [{"label": "10G", "variant_model": "ABC-I"}]
        self.assertEqual(discover_skus(specs, {}, modes), ["ABC-I", "ABC-C"])
        self.assertEqual(resolve_mode_skus(modes[0], ["ABC-I", "ABC-C"]), ["ABC-I"])


if __name__ == "__main__":
    unittest.main()
