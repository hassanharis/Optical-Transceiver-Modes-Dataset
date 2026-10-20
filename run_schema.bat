@echo off
setlocal
cd /d "%~dp0"
if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"
python -c "from otse.pipeline.prompts import extraction_schema_text; print(extraction_schema_text())"