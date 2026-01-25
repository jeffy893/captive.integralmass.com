#!/bin/bash

# Integral Mass Captive Insurance - Simulation Runner
# This script runs all simulations and generates the website assets

echo "=========================================="
echo "Integral Mass Captive Insurance"
echo "Simulation Runner"
echo "=========================================="
echo ""

# Check if Python 3.10 is installed
if ! command -v python3.10 &> /dev/null; then
    echo "❌ Error: Python 3.10 is not installed"
    echo "Please install Python 3.10"
    echo ""
    echo "Installation options:"
    echo "  Ubuntu/Debian: sudo apt install python3.10 python3.10-venv"
    echo "  macOS: brew install python@3.10"
    echo "  Or download from: https://www.python.org/downloads/"
    exit 1
fi

echo "✓ Python found: $(python3.10 --version)"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment with Python 3.10..."
    python3.10 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Run simulations
echo "=========================================="
echo "Running Simulations"
echo "=========================================="
echo ""

cd src
python main.py

# Check if simulation was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ Simulation Complete!"
    echo "=========================================="
    echo ""
    echo "Results saved to:"
    echo "  - docs/assets/       (graphs)"
    echo "  - data/              (CSV files)"
    echo ""
    echo "To view the website:"
    echo "  1. Open docs/index.html in your browser"
    echo "  2. Or run: python -m http.server 8000 --directory docs"
    echo "     Then visit: http://localhost:8000"
    echo ""
else
    echo ""
    echo "❌ Simulation failed. Check error messages above."
    exit 1
fi

# Deactivate virtual environment
deactivate
