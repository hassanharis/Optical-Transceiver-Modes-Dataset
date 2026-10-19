"""Generate a modes-only HTML report from a pipeline run directory.

Usage:
    python -m otse.scripts.generate_modes_report runs/20260806_102819
    python -m otse.scripts.generate_modes_report runs/20260806_102819 -o custom_output.html
"""

from __future__ import annotations

import json
import argparse
import sys
from html import escape
from pathlib import Path
from textwrap import shorten


def _load(run_dir: Path, name: str) -> dict | list | None:
    p = run_dir / name
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return None


def _badges(values: list) -> str:
    return " ".join(f'<span class="badge">{escape(str(v))}</span>' for v in values)


def _fmt_value(value) -> str:
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return str(value) if value is not None else ""


def _spec_item(label: str, value: str, wide: bool = False) -> str:
    cls = ' class="spec-item wide"' if wide else ' class="spec-item"'
    style = ' style="font-weight:400; font-size:0.78rem;"' if wide else ""
    return f'<div{cls}><div class="label">{escape(label)}</div><div class="value"{style}>{escape(value)}</div></div>'


# Field display names and units
_FIELD_DISPLAY = {
    "vendor": "Vendor",
    "model": "Model",
    "form_factor": "Form Factor",
    "wavelength_band": "Wavelength Band",
    "wavelength_min_nm": "Wavelength Min",
    "wavelength_max_nm": "Wavelength Max",
    "channel_total": "Channel Total",
    "connector_type": "Connector",
    "fiber_type": "Fiber Type",
    "temp_min_c": "Temp Min (°C)",
    "temp_max_c": "Temp Max (°C)",
    "power_consumption_w": "Power (W)",
    "baud_rate_gbaud": "Baud Rate (GBaud)",
    "tx_power_min_dbm": "TX Power Min (dBm)",
    "tx_power_max_dbm": "TX Power Max (dBm)",
    "rx_osnr_db": "RX OSNR (dB)",
    "rx_osnr_tolerance_db_max": "RX OSNR Tolerance (dB)",
    "rx_overload_dbm": "RX Overload (dBm)",
    "standards_claimed": "Standards",
    "notes": "Notes",
    "label": "Mode",
    "reach_km": "Reach (km)",
    "rx_sensitivity_dbm": "RX Sensitivity (dBm)",
    "cd_tolerance_ps_nm": "CD Tolerance (ps/nm)",
    "channel_spacing_ghz": "Channel Spacing (GHz)",
    "bit_rate_gbps": "Bit Rate (Gbps)",
    "modulation_formats": "Modulation",
    "fec_types": "FEC",
    "host_interface_name": "Host Interface",
    "media_interface_name": "Media Interface",
    "standards_code": "Standards code",
    "host_interface_id_hex": "Host Interface ID (hex)",
    "media_interface_id_hex": "Media Interface ID (hex)",
    "penalties": "Penalties",
}

def _fmt_penalty(p: dict) -> str:
    conds = ", ".join(f"{c.get('parameter')}={c.get('value')}" for c in p.get("conditions", []))
    target = p.get("target_parameter", "")
    pen = f"{p.get('penalty_db')} dB"
    val = f" (val={p.get('penalized_value')})" if p.get('penalized_value') is not None else ""
    return f"{target} +{pen}{val} [{conds}]"

def _mode_cell(key: str, value) -> str:
    if key == "label":
        return f'<td><strong>{escape(str(value))}</strong></td>'
    if key == "penalties" and isinstance(value, list):
        return f"<td>{escape('; '.join(_fmt_penalty(p) for p in value if isinstance(p, dict)))}</td>"
    if isinstance(value, list):
        return f"<td>{_badges(value)}</td>"
    return f"<td>{escape(str(value))}</td>"


def generate_modes_html(run_dir: Path) -> str:
    meta = _load(run_dir, "meta.json") or {}
    mode_atoms = _load(run_dir, "mode_atoms.json") or {}
    modes_data = _load(run_dir, "modes.json") or {}

    modes = modes_data.get("modes", []) if isinstance(modes_data, dict) else modes_data
    multi = mode_atoms.get("multi_valued", {}) if isinstance(mode_atoms, dict) else {}
    general = mode_atoms.get("general", {}) if isinstance(mode_atoms, dict) else {}

    vendor = general.get("vendor", "")
    model = general.get("model", "")
    title = f"{vendor} {model}".strip() or "Unknown"
    form_factor = _fmt_value(general.get("form_factor", ""))
    band = _fmt_value(general.get("wavelength_band", ""))
    channels = general.get("channel_total", "")
    subtitle_parts = [p for p in [form_factor, band, f"{channels} channels" if channels else ""] if p]
    subtitle = " &middot; ".join(subtitle_parts)

    ts = meta.get("timestamp", "")[:16].replace("T", " ")
    model_id = shorten(meta.get("model_id", "unknown"), width=30, placeholder="…")

    general_items = ""
    for field, value in general.items():
        if value is None:
            continue
        display_name = _FIELD_DISPLAY.get(field, field.replace("_", " ").title())
        formatted = _fmt_value(value)
        if not formatted:
            continue
        wide = field == "notes"
        general_items = general_items + f"      {_spec_item(display_name, formatted, wide=wide)}\n" if 'general_items' in locals() else f"      {_spec_item(display_name, formatted, wide=wide)}\n"

    # Mode table
    if modes:
        all_keys: list[str] = []
        for m in modes:
            for k in m:
                if k not in all_keys:
                    all_keys.append(k)

        header_cells = "".join(
            f"<th>{escape(_FIELD_DISPLAY.get(k, k))}</th>" for k in all_keys
        )
        rows = ""
        for m in modes:
            cells = "".join(_mode_cell(k, m.get(k, "")) for k in all_keys)
            rows += f"      <tr>{cells}</tr>\n"
        mode_table = f"""    <table>
      <tr>{header_cells}</tr>
{rows}    </table>"""
    else:
        mode_table = "    <p>No modes synthesized.</p>"

    # Multi-valued table
    multi_rows = ""
    for field, values in multi.items():
        if isinstance(values, list):
            multi_rows += f'      <tr><td>{escape(field)}</td><td>{_badges(values)}</td></tr>\n'

    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mode Report — {escape(title)}</title>
<style>
  :root {{ --bg: #f8fafc; --surface: #ffffff; --card: #f1f5f9; --accent: #0369a1; --accent2: #7c3aed; --accent3: #047857; --accent4: #c2410c; --text: #1e293b; --muted: #64748b; --border: #cbd5e1; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace; background: var(--bg); color: var(--text); line-height: 1.6; padding: 2rem; }}
  .container {{ max-width: 1000px; margin: 0 auto; }}
  header {{ text-align: center; margin-bottom: 2.5rem; }}
  header h1 {{ font-size: 1.5rem; color: var(--accent); }}
  header .subtitle {{ color: var(--muted); font-size: 0.85rem; margin-top: 0.3rem; }}
  header .model-name {{ font-size: 1.1rem; color: var(--accent3); margin-top: 0.5rem; font-weight: 600; }}
  .section {{ margin-bottom: 2rem; }}
  .section-header {{ display: flex; align-items: center; gap: 0.6rem; margin-bottom: 0.75rem; }}
  .section-icon {{ width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 700; }}
  .section-icon.g {{ background: var(--accent); color: #fff; }}
  .section-icon.m {{ background: var(--accent4); color: #fff; }}
  .section-icon.mv {{ background: var(--accent2); color: #fff; }}
  .section-title {{ font-size: 1rem; font-weight: 600; }}
  .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; overflow-x: auto; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }}
  .spec-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 0.6rem; }}
  .spec-item {{ background: var(--card); border-radius: 6px; padding: 0.5rem 0.75rem; }}
  .spec-item .label {{ font-size: 0.68rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.04em; }}
  .spec-item .value {{ font-size: 0.88rem; font-weight: 600; margin-top: 0.1rem; word-break: break-word; }}
  .spec-item.wide {{ grid-column: 1 / -1; }}
  table {{ width: 100%; border-collapse: collapse; table-layout: auto; font-size: 0.8rem; }}
  th, td {{ border: 1px solid var(--border); padding: 0.45rem 0.65rem; text-align: left; }}
  th {{ background: var(--card); color: var(--accent); font-weight: 600;}}
  th {{ white-space: normal; }}
  td {{ white-space: nowrap; }}
  tr:hover td {{ background: rgba(3,105,161,0.05); }}
  .badge {{ display: inline-block; background: rgba(3,105,161,0.1); color: var(--accent); padding: 0.15rem 0.45rem; border-radius: 3px; font-size: 0.72rem; margin: 0.1rem; border: 1px solid rgba(3,105,161,0.2); }}
  .note-box {{ background: rgba(124,58,237,0.06); border-left: 3px solid var(--accent2); border-radius: 0 6px 6px 0; padding: 0.75rem 1rem; margin-top: 0.75rem; font-size: 0.75rem; color: var(--text); }}
  footer {{ text-align: center; color: var(--muted); font-size: 0.72rem; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border); }}
</style>
</head>
<body>
<div class="container">

<header>
  <h1>Transceiver Mode Report</h1>
  <div class="model-name">{escape(title)}</div>
  <div class="subtitle">{subtitle}</div>
</header>

<!-- GENERAL SPECS -->
<div class="section">
  <div class="section-header">
    <span class="section-icon g">G</span>
    <span class="section-title">General Specifications</span>
  </div>
  <div class="card">
    <div class="spec-grid">
{general_items}    </div>
  </div>
</div>

<!-- OPERATING MODES -->
<div class="section">
  <div class="section-header">
    <span class="section-icon m">M</span>
    <span class="section-title">Operating Modes</span>
  </div>
  <div class="card">
{mode_table}
    <div class="note-box">
      Modes were synthesized from multi-valued fields below using LLM-based linking.
    </div>
  </div>
</div>

<!-- MULTI-VALUED SOURCE -->
<div class="section">
  <div class="section-header">
    <span class="section-icon mv">&ctdot;</span>
    <span class="section-title">Multi-Valued Fields (source for mode generation)</span>
  </div>
  <div class="card">
    <table>
      <tr><th>Field</th><th>Values</th></tr>
{multi_rows}    </table>
  </div>
</div>

<footer>
  Generated by OTSE Pipeline &middot; {escape(model_id)} &middot; Run {escape(ts)}
</footer>

</div>
</body>
</html>"""


def main():
    from otse.paths import REPORTS_DIR

    parser = argparse.ArgumentParser(description="Generate an operating-modes HTML report")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir
    if not run_dir.is_dir():
        print(f"Error: {run_dir} is not a directory")
        sys.exit(1)

    out_path = args.output or REPORTS_DIR / f"{run_dir.name}_modes.html"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    html = generate_modes_html(run_dir)
    out_path.write_text(html, encoding="utf-8")
    print(f"Modes report written to {out_path}")


if __name__ == "__main__":
    main()