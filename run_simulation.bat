@echo off
REM Integral Mass Captive Insurance - Simulation Runner (Windows)

echo ==========================================
echo Integral Mass Captive Insurance
echo Simulation Runner
echo ==========================================
echo.

REM Check if Python 3.10 is installed
python --version 2>&1 | findstr /C:"3.10" >nul
if errorlevel 1 (
    echo Error: Python 3.10 is not installed
    echo Please install Python 3.10 from https://www.python.org/downloads/
    echo.
    echo Make sure to:
    echo   1. Download Python 3.10.x installer
    echo   2. Check "Add Python to PATH" during installation
    echo   3. Restart your command prompt after installation
    pause
    exit /b 1
)

echo Python 3.10 found
echo.

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo Dependencies installed
echo.

REM Run simulations
echo ==========================================
echo Running Simulations
echo ==========================================
echo.

cd src
python main.py

if errorlevel 1 (
    echo.
    echo Simulation failed. Check error messages above.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Simulation Complete!
echo ==========================================
echo.
echo Results saved to:
echo   - docs\assets\       (graphs)
echo   - data\              (CSV files)
echo.
echo To view the website:
echo   1. Open docs\index.html in your browser
echo   2. Or run: python -m http.server 8000 --directory docs
echo      Then visit: http://localhost:8000
echo.

REM Deactivate virtual environment
call deactivate

pause
