"""Launch packaged Streamlit applications without depending on the current directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys


APPS = {
    "extract": ("app.py", 8501),
    "composition": ("streamlit_composition.py", 8502),
    "harmonize": ("streamlit_field_replacer.py", 8503),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Launch an OTSE application")
    parser.add_argument("app", choices=APPS, nargs="?", default="extract")
    parser.add_argument("--port", type=int)
    args, streamlit_args = parser.parse_known_args()
    filename, default_port = APPS[args.app]
    script = Path(__file__).resolve().parent / "scripts" / filename
    raise SystemExit(
        subprocess.call(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                str(script),
                "--server.port",
                str(args.port if args.port is not None else default_port),
                *streamlit_args,
            ]
        )
    )


if __name__ == "__main__":
    main()