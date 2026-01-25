#!/usr/bin/env python3.10
"""
Setup Verification Script for Integral Mass Captive Insurance
Checks that Python 3.10 and all dependencies are properly installed.
"""
import sys
import subprocess

def check_python_version():
    """Verify Python 3.10 is being used."""
    print("Checking Python version...")
    version = sys.version_info
    
    if version.major == 3 and version.minor == 10:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} detected")
        print("   ERROR: Python 3.10 is required")
        print("\n   Installation instructions:")
        print("   - Ubuntu/Debian: sudo apt install python3.10 python3.10-venv")
        print("   - macOS: brew install python@3.10")
        print("   - Windows: Download from https://www.python.org/downloads/")
        return False

def check_dependencies():
    """Check if all required packages are installed."""
    print("\nChecking dependencies...")
    
    required_packages = [
        'pandas',
        'numpy',
        'matplotlib',
        'simpy',
        'scipy'
    ]
    
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("\nTo install missing packages:")
        print(f"   python3.10 -m pip install {' '.join(missing)}")
        return False
    
    return True

def check_file_structure():
    """Verify required files and directories exist."""
    print("\nChecking file structure...")
    
    import os
    
    required_paths = [
        'src/main.py',
        'src/actors.py',
        'src/financial_instrument.py',
        'src/queue_sim.py',
        'src/risk_model.py',
        'docs/index.html',
        'docs/assets/style.css',
        'data/GC_roster.csv',
        'data/risk_tables.csv',
        'requirements.txt'
    ]
    
    all_exist = True
    
    for path in required_paths:
        if os.path.exists(path):
            print(f"✓ {path}")
        else:
            print(f"❌ {path} NOT FOUND")
            all_exist = False
    
    return all_exist

def main():
    """Run all verification checks."""
    print("="*60)
    print("Integral Mass Captive Insurance - Setup Verification")
    print("="*60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("File Structure", check_file_structure)
    ]
    
    results = []
    
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ Error during {name} check: {e}")
            results.append((name, False))
    
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    
    all_passed = True
    for name, result in results:
        status = "✓ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n✓ All checks passed! You're ready to run simulations.")
        print("\nNext steps:")
        print("  1. Run: ./run_simulation.sh (Linux/Mac)")
        print("     Or:  run_simulation.bat (Windows)")
        print("  2. View results in docs/index.html")
        return 0
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
