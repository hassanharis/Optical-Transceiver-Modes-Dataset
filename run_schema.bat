@echo off
setlocal
cd /d "%~dp0"
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"
python -c "from otse.pipeline.atom_extractor import _build_schema_text; print(_build_schema_text())"