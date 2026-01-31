@echo off
REM Windows batch file to start the local development server

echo Starting Integral Mass Captive Insurance local server...
echo.

REM Try Python 3.10 first, then fall back to python3, then python
where python3.10 >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python3.10 serve_local.py
    goto :end
)

where python3 >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python3 serve_local.py
    goto :end
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python serve_local.py
    goto :end
)

echo ERROR: Python not found!
echo Please install Python 3 from https://www.python.org/downloads/
pause

:end
