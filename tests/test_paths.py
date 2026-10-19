import os
import json
import importlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from otse import paths


class PathTests(unittest.TestCase):
    def test_outputs_are_separate_from_published_dataset(self):
        settings = {name: "" for name in os.environ if name.startswith("OTSE_")}
        settings["TRANSCEIVER_RUNS_DIR"] = ""
        with patch.dict(os.environ, settings):
            import importlib

            defaults = importlib.reload(paths)
            self.assertEqual(defaults.RUNS_DIR, defaults.PROJECT_ROOT / "workspace" / "runs")
            self.assertFalse(defaults.RUNS_DIR.is_relative_to(defaults.DATASET_DIR))
            self.assertEqual(defaults.LEXICON_PATH.name, "harmonization_lexicon.json")

    def test_explicit_environment_override(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"TRANSCEIVER_RUNS_DIR": directory}):
                self.assertEqual(
                    paths.configured_path("TRANSCEIVER_RUNS_DIR", Path("unused")),
                    Path(directory).resolve(),
                )

    def test_paths_do_not_depend_on_working_directory(self):
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(paths.SOURCE_ROOT / "software")
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-c", "from otse.paths import PROJECT_ROOT; print(PROJECT_ROOT)"],
                cwd=directory,
                env=environment,
                capture_output=True,
                text=True,
                check=True,
            )
        self.assertEqual(Path(result.stdout.strip()), paths.PROJECT_ROOT)


class PackageTests(unittest.TestCase):
    def test_shared_consumers_and_lexicon(self):
        from otse.composition.field_replacer import DEFAULT_CONFIG_PATH, default_config
        from otse.composition.loader import default_runs_dir
        from otse.pipeline.runtime_store import DEFAULT_RUNS_DIR

        self.assertEqual(default_runs_dir(), paths.RUNS_DIR)
        self.assertEqual(DEFAULT_RUNS_DIR, paths.RUNS_DIR)
        self.assertEqual(DEFAULT_CONFIG_PATH, paths.LEXICON_PATH)
        self.assertGreater(len(default_config().rules), 0)

    def test_all_library_modules_import(self):
        modules = (
            "otse.transceiver_models", "otse.pipeline.pdf_parser",
            "otse.pipeline.atom_extractor", "otse.pipeline.mode_linker",
            "otse.pipeline.penalty_parser", "otse.pipeline.runtime_store",
            "otse.composition.analytics", "otse.composition.fields",
            "otse.composition.loader", "otse.composition.field_replacer",
        )
        for module in modules:
            with self.subTest(module=module):
                importlib.import_module(module)

    def test_cli_help_from_another_directory(self):
        modules = (
            "otse.launch", "otse.pipeline.run", "otse.scripts.apply_field_replacements",
            "otse.scripts.build_inventory", "otse.scripts.cleanup_runs",
            "otse.scripts.composition_report", "otse.scripts.export_all_modes",
            "otse.scripts.generate_report", "otse.scripts.generate_modes_report",
            "otse.scripts.normalize_fiber_type_dataset", "otse.scripts.refresh_reports",
            "otse.scripts.repair_runs",
        )
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(paths.SOURCE_ROOT / "software")
        with tempfile.TemporaryDirectory() as directory:
            for module in modules:
                with self.subTest(module=module):
                    result = subprocess.run(
                        [sys.executable, "-m", module, "--help"],
                        cwd=directory, env=environment, capture_output=True, text=True,
                        timeout=60,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn("usage:", result.stdout.lower())

    def test_report_refresh_dry_run_does_not_create_output(self):
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(paths.SOURCE_ROOT / "software")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            runs = root / "runs"
            runs.mkdir()
            reports = root / "new" / "reports"
            result = subprocess.run(
                [sys.executable, "-m", "otse.scripts.refresh_reports", "--runs-dir",
                 str(runs), "--reports-dir", str(reports), "--dry-run"],
                cwd=directory, env=environment, capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertFalse(reports.exists())

    def test_reports_and_exports_use_explicit_output_paths(self):
        environment = os.environ.copy()
        environment["PYTHONPATH"] = str(paths.SOURCE_ROOT / "software")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "runs" / "test_run"
            run.mkdir(parents=True)
            (run / "meta.json").write_text(
                json.dumps({"source_file": "example.pdf", "validation_passed": True}),
                encoding="utf-8",
            )
            (run / "specs.json").write_text("{}", encoding="utf-8")
            (run / "modes.json").write_text('{"modes": []}', encoding="utf-8")
            for module in ("generate_report", "generate_modes_report"):
                with self.subTest(module=module):
                    output = root / "nested" / f"{module}.html"
                    result = subprocess.run(
                        [sys.executable, "-m", f"otse.scripts.{module}", str(run),
                         "-o", str(output)],
                        cwd=directory, env=environment, capture_output=True, text=True,
                        timeout=60,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertIn("<html", output.read_text(encoding="utf-8"))
            (run / "modes.json").write_text(
                '{"modes": [{"mode_id": "example", "modulation": "QPSK"}]}',
                encoding="utf-8",
            )
            output = root / "exports" / "all_modes.csv"
            result = subprocess.run(
                [sys.executable, "-m", "otse.scripts.export_all_modes", "--runs-dir",
                 str(run.parent), "-o", str(output)],
                cwd=directory, env=environment, capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("test_run", output.read_text(encoding="utf-8-sig"))

    def test_new_runs_use_configured_workspace(self):
        from otse.pipeline.pdf_parser import ParsedDatasheet
        from otse.pipeline import runtime_store

        with tempfile.TemporaryDirectory() as directory:
            runs = Path(directory) / "workspace" / "runs"
            parsed = ParsedDatasheet(source_path=Path("example.pdf"), markdown="example")
            with patch.object(runtime_store, "DEFAULT_RUNS_DIR", runs):
                run = runtime_store.store_run(parsed, {}, None)
                self.assertEqual(run.parent, runs)
                self.assertEqual(runtime_store.list_runs(), [run])
                self.assertEqual(runtime_store.load_run(run)["meta"]["source_file"], "example.pdf")

    def test_app_launcher_selects_packaged_script(self):
        from otse.launch import APPS, main

        for app, (filename, port) in APPS.items():
            with self.subTest(app=app):
                with patch.object(sys, "argv", ["otse-app", app]):
                    with patch("otse.launch.subprocess.call", return_value=0) as launch:
                        with self.assertRaises(SystemExit) as exit_status:
                            main()
                self.assertEqual(exit_status.exception.code, 0)
                command = launch.call_args.args[0]
                self.assertEqual(Path(command[4]).name, filename)
                self.assertTrue(Path(command[4]).is_file())
                self.assertEqual(command[5:7], ["--server.port", str(port)])

    def test_installed_package_from_another_directory(self):
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, "-c",
                 "import otse; from otse.paths import PROJECT_ROOT; print(PROJECT_ROOT)"],
                cwd=directory, env=environment, capture_output=True, text=True, timeout=60,
            )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(Path(result.stdout.strip()), paths.PROJECT_ROOT)

    def test_streamlit_apps_start(self):
        from streamlit.testing.v1 import AppTest
        from otse.launch import APPS

        with patch.dict(os.environ, {"TRANSCEIVER_RUNS_DIR": str(paths.DATASET_DIR / "runs")}):
            for app, (filename, port) in APPS.items():
                with self.subTest(app=app):
                    script = paths.SOURCE_ROOT / "software" / "otse" / "scripts" / filename
                    with patch("requests.get") as request:
                        request.return_value.ok = False
                        result = AppTest.from_file(str(script)).run(timeout=60)
                    self.assertEqual(len(result.exception), 0, str(result.exception))