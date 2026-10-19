@echo off
setlocal
cd /d "%~dp0"

if exist ".venv\Scripts\activate.bat" call ".venv\Scripts\activate.bat"
python -m otse.launch composition %*
if errorlevel 1 echo Install OTSE first: python -m pip install -e .
pause
