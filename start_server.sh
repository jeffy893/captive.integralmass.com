#!/bin/bash
# Mac/Linux shell script to start the local development server

echo "Starting Integral Mass Captive Insurance local server..."
echo ""

# Try Python 3.10 first, then fall back to python3, then python
if command -v python3.10 &> /dev/null; then
    python3.10 serve_local.py
elif command -v python3 &> /dev/null; then
    python3 serve_local.py
elif command -v python &> /dev/null; then
    python serve_local.py
else
    echo "ERROR: Python not found!"
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi
