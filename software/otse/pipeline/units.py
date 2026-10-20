"""Convert printed quantities to canonical units after extraction.

The printed value and unit are preserved. ``canonical_value`` stays null when
the printed unit cannot be converted, including nanometre channel spacing and
any dB or dBm value placed on a watt field.
"""

from __future__ import annotations

from typing import Any

from otse.transceiver_models import CANONICAL_UNITS

_ALIASES: dict[str, str] = {
    "m": "m",
    "meter": "m",
    "meters": "m",
    "metre": "m",
    "metres": "m",
    "km": "km",
    "kilometer": "km",
    "kilometers": "km",
    "kilometre": "km",
    "kilometres": "km",
    "mm": "mm",
    "nm": "nm",
    "kbps": "kbps",
    "kb/s": "kbps",
    "kbit/s": "kbps",
    "mbps": "Mbps",
    "mb/s": "Mbps",
    "mbit/s": "Mbps",
    "mbits/s": "Mbps",
    "gbps": "Gbps",
    "gb/s": "Gbps",
    "gbit/s": "Gbps",
    "gbits/s": "Gbps",
    "tbps": "Tbps",
    "tb/s": "Tbps",
    "tbit/s": "Tbps",
    "gbaud": "GBaud",
    "gbd": "GBaud",
    "mbaud": "MBaud",
    "mbd": "MBaud",
    "hz": "Hz",
    "khz": "kHz",
    "mhz": "MHz",
    "ghz": "GHz",
    "thz": "THz",
    "uw": "uW",
    "µw": "uW",
    "mw": "mW",
    "w": "W",
    "mv": "mV",
    "v": "V",
    "ma": "mA",
    "a": "A",
    "db": "dB",
    "dbm": "dBm",
}

_LENGTH_TO_M = {"mm": 0.001, "m": 1.0, "km": 1000.0}
_RATE_TO_GBPS = {"kbps": 1e-6, "Mbps": 1e-3, "Gbps": 1.0, "Tbps": 1e3}
_BAUD_TO_GBAUD = {"MBaud": 1e-3, "GBaud": 1.0}
_FREQ_TO_HZ = {"Hz": 1.0, "kHz": 1e3, "MHz": 1e6, "GHz": 1e9, "THz": 1e12}
_POWER_TO_W = {"uW": 1e-6, "mW": 1e-3, "W": 1.0}
_VOLT_TO_V = {"mV": 1e-3, "V": 1.0}
_CURRENT_TO_A = {"mA": 1e-3, "A": 1.0}


def canonical_unit(text: str | None) -> str | None:
    """Map a printed unit token to its normalized symbol."""
    if not isinstance(text, str):
        return None
    token = text.strip().replace("μ", "u").replace("µ", "u").lower().replace(" ", "")
    return _ALIASES.get(token)


def convert(value: float, unit: str | None, target: str) -> float | None:
    """Return ``value`` in ``target``, or null when the units are incompatible."""
    source = canonical_unit(unit)
    if source is None or not isinstance(value, (int, float)) or isinstance(value, bool):
        return None
    if target == "km":
        factor = _LENGTH_TO_M.get(source)
        return None if factor is None else _clean(value * factor / 1000.0)
    if target == "m":
        factor = _LENGTH_TO_M.get(source)
        return None if factor is None else _clean(value * factor)
    if target == "Gbps":
        factor = _RATE_TO_GBPS.get(source)
        return None if factor is None else _clean(value * factor)
    if target == "GBaud":
        factor = _BAUD_TO_GBAUD.get(source)
        return None if factor is None else _clean(value * factor)
    if target == "THz":
        factor = _FREQ_TO_HZ.get(source)
        return None if factor is None else _clean(value * factor / 1e12)
    if target == "GHz":
        factor = _FREQ_TO_HZ.get(source)
        return None if factor is None else _clean(value * factor / 1e9)
    if target == "W":
        factor = _POWER_TO_W.get(source)
        return None if factor is None else _clean(value * factor)
    if target == "V":
        factor = _VOLT_TO_V.get(source)
        return None if factor is None else _clean(value * factor)
    if target == "mA":
        factor = _CURRENT_TO_A.get(source)
        return None if factor is None else _clean(value * factor * 1000.0)
    return None


def _clean(value: float) -> float:
    """Drop binary noise while keeping engineering precision."""
    return float(f"{value:.12g}")


def _normalize_measurement(item: Any, target: str) -> Any:
    if not isinstance(item, dict):
        return item
    converted = convert(item.get("value"), item.get("unit"), target)
    item["canonical_value"] = converted
    item["canonical_unit"] = target if converted is not None else None
    return item


def _normalize_field(value: Any, target: str) -> Any:
    if isinstance(value, dict):
        return [_normalize_measurement(value, target)]
    if isinstance(value, list):
        return [_normalize_measurement(item, target) for item in value]
    return value


def normalize_quantities(data: dict[str, Any]) -> dict[str, Any]:
    """Fill canonical values on module and variant printed-number fields."""
    for field, target in CANONICAL_UNITS.items():
        if field in data:
            data[field] = _normalize_field(data[field], target)
    variants = data.get("variants")
    if isinstance(variants, dict):
        variants = [variants]
        data["variants"] = variants
    if isinstance(variants, list):
        for variant in variants:
            if not isinstance(variant, dict):
                continue
            for field, target in CANONICAL_UNITS.items():
                if field in variant:
                    variant[field] = _normalize_field(variant[field], target)
    return data
