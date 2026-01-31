# Python 3.10 Requirements

## Why Python 3.10 Specifically?

This project requires **Python 3.10** (not 3.11, 3.12, or other versions) for the following reasons:

1. **Stability**: Python 3.10 is a mature, stable release with excellent library support
2. **Compatibility**: All dependencies (pandas, numpy, matplotlib, simpy, scipy) are fully tested with 3.10
3. **Type Hints**: Uses Python 3.10's improved type hinting features (PEP 604, PEP 612)
4. **Match Statements**: Leverages structural pattern matching introduced in 3.10
5. **Consistency**: Ensures reproducible results across all environments

## Installation Instructions

### Linux (Ubuntu/Debian)
```bash
# Add deadsnakes PPA (if needed)
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Install Python 3.10
sudo apt install python3.10 python3.10-venv python3.10-dev

# Verify installation
python3.10 --version
```

### macOS
```bash
# Using Homebrew
brew install python@3.10

# Add to PATH (add to ~/.zshrc or ~/.bash_profile)
export PATH="/usr/local/opt/python@3.10/bin:$PATH"

# Verify installation
python3.10 --version
```

### Windows
1. Download Python 3.10.x from [python.org/downloads](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python 3.10 to PATH"
4. Complete installation
5. Open new Command Prompt and verify:
   ```cmd
   python --version
   ```
   Should show: `Python 3.10.x`

## Verification

After installation, run the verification script:

```bash
python3.10 verify_setup.py
```

This will check:
- ✓ Python 3.10 is installed
- ✓ All required packages are available
- ✓ File structure is correct

## Common Issues

### "python3.10: command not found"

**Linux/Mac:**
```bash
# Check if Python 3.10 is installed but not in PATH
which python3.10
ls /usr/bin/python3.10
ls /usr/local/bin/python3.10

# If found, create symlink or add to PATH
```

**Windows:**
- Reinstall Python 3.10 and ensure "Add to PATH" is checked
- Or manually add to PATH: `C:\Python310\` and `C:\Python310\Scripts\`

### Multiple Python Versions

If you have multiple Python versions:

```bash
# Always use python3.10 explicitly
python3.10 -m venv venv
python3.10 -m pip install -r requirements.txt
python3.10 src/main.py
```

### Virtual Environment

Create a Python 3.10 virtual environment:

```bash
# Create venv
python3.10 -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat  # Windows

# Verify Python version in venv
python --version  # Should show 3.10.x

# Install dependencies
pip install -r requirements.txt
```

## Files Configured for Python 3.10

The following files explicitly require Python 3.10:

- `.python-version` - Specifies Python 3.10 for pyenv
- `run_simulation.sh` - Checks for python3.10 command
- `run_simulation.bat` - Verifies Python 3.10 on Windows
- `.github/workflows/run-simulation.yml` - GitHub Actions uses Python 3.10
- `verify_setup.py` - Validates Python 3.10 installation
- All `src/*.py` files - Shebang: `#!/usr/bin/env python3.10`

## Dependencies (requirements.txt)

All packages are tested with Python 3.10:

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
simpy>=4.0.0
scipy>=1.10.0
```

## Troubleshooting

### Package Installation Fails

```bash
# Upgrade pip first
python3.10 -m pip install --upgrade pip

# Install packages one by one to identify issues
python3.10 -m pip install pandas
python3.10 -m pip install numpy
python3.10 -m pip install matplotlib
python3.10 -m pip install simpy
python3.10 -m pip install scipy
```

### ImportError Despite Installation

```bash
# Check which Python is running
which python3.10
python3.10 -c "import sys; print(sys.executable)"

# Check installed packages
python3.10 -m pip list

# Reinstall in user directory
python3.10 -m pip install --user -r requirements.txt
```

## Support

If you continue to have Python 3.10 issues:

1. Run `python3.10 verify_setup.py` and share the output
2. Check Python version: `python3.10 --version`
3. Check pip version: `python3.10 -m pip --version`
4. List installed packages: `python3.10 -m pip list`

---

**Remember**: Always use `python3.10` explicitly, not `python` or `python3`, to ensure the correct version is used.
