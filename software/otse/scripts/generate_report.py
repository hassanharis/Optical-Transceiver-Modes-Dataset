"""Generate a standalone HTML report from a pipeline run directory.

Usage:
    python -m otse.scripts.generate_report runs/20260805_195140
    python -m otse.scripts.generate_report runs/20260805_195140 -o report.html
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


def _load_dict(run_dir: Path, name: str) -> dict:
    data = _load(run_dir, name)
    return data if isinstance(data, dict) else {}


def _load_text(run_dir: Path, name: str, max_chars: int = 2000) -> str:
    p = run_dir / name
    if not p.exists():
        return ""
    text = p.read_text(encoding="utf-8")
    if len(text) > max_chars:
        text = text[:max_chars] + "\n..."
    return text


def _json_highlight(obj: dict) -> str:
    """Syntax-highlight a dict as HTML spans."""
    raw = json.dumps(obj, indent=2, ensure_ascii=False)
    out = []
    for line in raw.split("\n"):
        line = escape(line)
        # keys
        line = line.replace('&quot;', '"')
        import re
        line = re.sub(
            r'"([^"]+)"(\s*:\s*)',
            r'<span class="key">"\1"</span>\2',
            line,
        )
        # string values
        line = re.sub(
            r':\s*"([^"]*)"',
            lambda m: f': <span class="str">"{m.group(1)}"</span>',
            line,
        )
        # null
        line = re.sub(r'\bnull\b', '<span class="null">null</span>', line)
        # numbers (negative, float, int)
        line = re.sub(
            r'(?<=[\s\[,:])(-?\d+\.?\d*)',
            r'<span class="num">\1</span>',
            line,
        )
        out.append(line)
    return "\n".join(out)


def _badges(values: list) -> str:
    return " ".join(f'<span class="badge">{escape(str(v))}</span>' for v in values)


def _mode_table(modes: list[dict]) -> str:
    if not modes:
        return "<p>No modes synthesized.</p>"

    # Collect all keys across modes (preserving order from first mode)
    all_keys: list[str] = []
    for m in modes:
        for k in m:
            if k not in all_keys:
                all_keys.append(k)

    header = "<tr>" + "".join(f"<th>{escape(k)}</th>" for k in all_keys) + "</tr>"
    rows = []
    for m in modes:
        cells = []
        for k in all_keys:
            v = m.get(k, "")
            if k == "label":
                cells.append(f'<td><strong>{escape(str(v))}</strong></td>')
            elif "hex" in k:
                cells.append(f'<td><span class="badge">{escape(str(v))}</span></td>')
            else:
                cells.append(f"<td>{escape(str(v))}</td>")
        rows.append("<tr>" + "".join(cells) + "</tr>")

    return f"<table>{header}{''.join(rows)}</table>"


def generate_html(run_dir: Path) -> str:
    meta = _load_dict(run_dir, "meta.json")
    raw_llm = _load_dict(run_dir, "raw_llm.json")
    specs = _load_dict(run_dir, "specs.json") or raw_llm
    mode_atoms = _load_dict(run_dir, "mode_atoms.json")
    modes_data = _load(run_dir, "modes.json") or {}
    md_excerpt = escape(_load_text(run_dir, "content.md", max_chars=2000))

    modes = modes_data.get("modes", []) if isinstance(modes_data, dict) else modes_data
    multi = mode_atoms.get("multi_valued", {}) if isinstance(mode_atoms, dict) else {}
    general = mode_atoms.get("general", {}) if isinstance(mode_atoms, dict) else {}

    source = Path(meta.get("source_file", "unknown")).name
    vendor = specs.get("vendor") or ""
    model = specs.get("model") or source
    title = f"{vendor} {model}"
    title = title.strip() or source
    ts = meta.get("timestamp", "")[:16].replace("T", " ")
    model_id = shorten(meta.get("model_id", "unknown"), width=30, placeholder="…")

    # Multi-valued table rows
    multi_rows = ""
    for field, values in multi.items():
        if isinstance(values, list):
            multi_rows += f"<tr><td>{escape(field)}</td><td>{_badges(values)}</td></tr>\n"

    # General table rows
    general_rows = ""
    for field, value in general.items():
        if isinstance(value, list):
            display = ", ".join(str(v) for v in value)
        else:
            display = str(value) if value is not None else ""
        general_rows += f"<tr><td>{escape(field)}</td><td>{escape(display)}</td></tr>\n"

    has_modes = bool(modes)
    has_mode_atoms = bool(multi) or bool(general)

    return f"""\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pipeline Output — {escape(title)}</title>
<style>
  :root {{ --bg: #0f172a; --surface: #1e293b; --card: #334155; --accent: #38bdf8; --accent2: #a78bfa; --accent3: #34d399; --accent4: #fb923c; --text: #e2e8f0; --muted: #94a3b8; --border: #475569; }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: 'JetBrains Mono', 'Fira Code', 'Cascadia Code', monospace; background: var(--bg); color: var(--text); line-height: 1.6; padding: 2rem; }}
  .container {{ max-width: 1200px; margin: 0 auto; }}
  header {{ text-align: center; margin-bottom: 3rem; }}
  header h1 {{ font-size: 1.6rem; color: var(--accent); }}
  header p {{ color: var(--muted); font-size: 0.85rem; margin-top: 0.3rem; }}
  .pipeline {{ display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin: 1.5rem 0; flex-wrap: wrap; }}
  .pipeline .stage-dot {{ padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.75rem; font-weight: 600; border: 1px solid var(--border); }}
  .pipeline .arrow {{ color: var(--muted); font-size: 1.2rem; }}
  .stage-dot.s1 {{ background: rgba(56,189,248,0.15); color: var(--accent); border-color: var(--accent); }}
  .stage-dot.s2 {{ background: rgba(167,139,250,0.15); color: var(--accent2); border-color: var(--accent2); }}
  .stage-dot.s3 {{ background: rgba(52,211,153,0.15); color: var(--accent3); border-color: var(--accent3); }}
  .stage-dot.s4 {{ background: rgba(251,146,60,0.15); color: var(--accent4); border-color: var(--accent4); }}
  .stage {{ margin-bottom: 2.5rem; }}
  .stage-header {{ display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem; }}
  .stage-num {{ width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700; }}
  .stage-num.n1 {{ background: var(--accent); color: var(--bg); }}
  .stage-num.n2 {{ background: var(--accent2); color: var(--bg); }}
  .stage-num.n3 {{ background: var(--accent3); color: var(--bg); }}
  .stage-num.n4 {{ background: var(--accent4); color: var(--bg); }}
  .stage-title {{ font-size: 1.1rem; font-weight: 600; }}
  .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 1.25rem; margin-bottom: 1rem; overflow-x: auto; }}
  .meta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 0.75rem; }}
  .meta-item {{ background: var(--card); border-radius: 6px; padding: 0.6rem 0.8rem; }}
  .meta-item .label {{ font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; }}
  .meta-item .value {{ font-size: 0.95rem; font-weight: 600; margin-top: 0.15rem; }}
  pre {{ font-size: 0.78rem; line-height: 1.5; white-space: pre-wrap; word-break: break-word; color: var(--muted); max-height: 300px; overflow-y: auto; }}
  pre .key {{ color: var(--accent); }}
  pre .str {{ color: var(--accent3); }}
  pre .num {{ color: var(--accent4); }}
  pre .null {{ color: #6b7280; }}
  .json-block {{ background: var(--card); border-radius: 6px; padding: 1rem; margin-top: 0.5rem; }}
  .md-excerpt {{ background: var(--card); border-radius: 6px; padding: 1rem; font-size: 0.78rem; color: var(--muted); max-height: 200px; overflow-y: auto; white-space: pre-wrap; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.8rem; }}
  th, td {{ border: 1px solid var(--border); padding: 0.45rem 0.65rem; text-align: left; }}
  th {{ background: var(--card); color: var(--accent); font-weight: 600; white-space: nowrap; }}
  th {{ white-space: normal; }}
  td {{ white-space: nowrap; }}
  tr:hover td {{ background: rgba(56,189,248,0.04); }}
  .badge {{ display: inline-block; background: rgba(56,189,248,0.15); color: var(--accent); padding: 0.1rem 0.4rem; border-radius: 3px; font-size: 0.72rem; margin: 0.1rem; }}
  .cols-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }}
  @media (max-width: 768px) {{ .cols-2 {{ grid-template-columns: 1fr; }} }}
  .section-label {{ font-size: 0.75rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; font-weight: 600; }}
  footer {{ text-align: center; color: var(--muted); font-size: 0.72rem; margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--border); }}
</style>
</head>
<body>
<div class="container">

<header>
  <h1>Transceiver Spec Extraction Pipeline</h1>
  <p>LLM-powered structured extraction from PDF datasheets</p>
  <div class="pipeline">
    <span class="stage-dot s1">PDF Parse</span>
    <span class="arrow">&rarr;</span>
    <span class="stage-dot s2">Atom Extraction</span>
    {"" if not has_mode_atoms else '<span class="arrow">&rarr;</span><span class="stage-dot s3">Mode Separation</span>'}
    {"" if not has_modes else '<span class="arrow">&rarr;</span><span class="stage-dot s4">Mode Synthesis</span>'}
  </div>
</header>

<!-- STAGE 1: PDF PARSE -->
<div class="stage">
  <div class="stage-header">
    <span class="stage-num n1">1</span>
    <span class="stage-title">PDF Parse</span>
  </div>
  <div class="card">
    <div class="meta-grid">
      <div class="meta-item"><div class="label">Source</div><div class="value">{escape(source)}</div></div>
      <div class="meta-item"><div class="label">Pages</div><div class="value">{meta.get("page_count", "?")}</div></div>
      <div class="meta-item"><div class="label">Tables Detected</div><div class="value">{meta.get("table_count", "?")}</div></div>
      <div class="meta-item"><div class="label">Model</div><div class="value">{escape(model_id)}</div></div>
      <div class="meta-item"><div class="label">Timestamp</div><div class="value">{escape(ts)}</div></div>
    </div>
  </div>
  <div class="card">
    <div class="section-label">Extracted Markdown (excerpt)</div>
    <div class="md-excerpt">{md_excerpt}</div>
  </div>
</div>

<!-- STAGE 2: ATOM EXTRACTION -->
<div class="stage">
  <div class="stage-header">
    <span class="stage-num n2">2</span>
    <span class="stage-title">Atom Extraction (LLM &rarr; JSON)</span>
  </div>
  <div class="card">
    <div class="section-label">Raw LLM Output &mdash; Structured Parameters</div>
    <div class="json-block"><pre>{_json_highlight(raw_llm)}</pre></div>
  </div>
</div>

{"" if not has_mode_atoms else f'''
<!-- STAGE 3: MODE SEPARATION -->
<div class="stage">
  <div class="stage-header">
    <span class="stage-num n3">3</span>
    <span class="stage-title">Mode Separation</span>
  </div>
  <div class="cols-2">
    <div class="card">
      <div class="section-label">Multi-Valued (need linking)</div>
      <table>
        <tr><th>Field</th><th>Values</th></tr>
        {multi_rows}
      </table>
    </div>
    <div class="card">
      <div class="section-label">General (module-level)</div>
      <table>
        <tr><th>Field</th><th>Value</th></tr>
        {general_rows}
      </table>
    </div>
  </div>
</div>
'''}

{"" if not has_modes else f'''
<!-- STAGE 4: MODE SYNTHESIS -->
<div class="stage">
  <div class="stage-header">
    <span class="stage-num n4">4</span>
    <span class="stage-title">Mode Synthesis (LLM Linking)</span>
  </div>
  <div class="card" style="overflow-x:auto;">
    <div class="section-label">Synthesized Operating Modes</div>
    {_mode_table(modes)}
  </div>
</div>
'''}

<footer>
  Generated by Transceiver Spec Extraction Pipeline &middot; {escape(model_id)} &middot; Run {escape(ts)}
</footer>

</div>
</body>
</html>"""


def main():
    from otse.paths import REPORTS_DIR

    parser = argparse.ArgumentParser(description="Generate a pipeline HTML report")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir
    if not run_dir.is_dir():
        print(f"Error: {run_dir} is not a directory")
        sys.exit(1)

    out_path = args.output or REPORTS_DIR / f"{run_dir.name}_pipeline.html"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    html = generate_html(run_dir)
    out_path.write_text(html, encoding="utf-8")
    print(f"Report written to {out_path}")


if __name__ == "__main__":
    main()