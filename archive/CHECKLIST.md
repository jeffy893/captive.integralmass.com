# Pre-Execution Checklist

Before running the simulations, verify all requirements are met:

## ✅ Python 3.10 Installation

- [ ] Python 3.10 is installed (not 3.11, 3.12, or other versions)
- [ ] Command `python3.10 --version` works and shows 3.10.x
- [ ] pip is available: `python3.10 -m pip --version`

**Verification Command:**
```bash
python3.10 verify_setup.py
```

## ✅ Dependencies

- [ ] pandas >= 2.0.0
- [ ] numpy >= 1.24.0
- [ ] matplotlib >= 3.7.0
- [ ] simpy >= 4.0.0
- [ ] scipy >= 1.10.0

**Installation Command:**
```bash
python3.10 -m pip install -r requirements.txt
```

## ✅ File Structure

- [ ] `src/` directory with all Python files
- [ ] `docs/` directory with HTML files
- [ ] `data/` directory with CSV files
- [ ] `requirements.txt` exists
- [ ] `.python-version` file exists

## ✅ Execution Scripts

- [ ] `run_simulation.sh` is executable (Linux/Mac)
- [ ] `run_simulation.bat` exists (Windows)
- [ ] `verify_setup.py` is executable

**Make Executable (Linux/Mac):**
```bash
chmod +x run_simulation.sh
chmod +x verify_setup.py
```

## ✅ Output Directories

The following directories will be created automatically:
- [ ] `docs/assets/` (for generated graphs)
- [ ] `data/` (for CSV outputs)

## 🚀 Ready to Run?

If all items above are checked, you're ready to execute:

**Linux/Mac:**
```bash
./run_simulation.sh
```

**Windows:**
```cmd
run_simulation.bat
```

**Manual:**
```bash
cd src
python3.10 main.py
```

## 📊 Expected Outputs

After successful execution, you should see:

### Generated Graphs (in `docs/assets/`)
- [ ] `financial_instrument_comparison.png`
- [ ] `queue_simulation_results.png`
- [ ] `monte_carlo_results.png`

### Data Files (in `data/`)
- [ ] `monte_carlo_results.csv`
- [ ] `completed_units.csv`
- [ ] `risk_events.csv`
- [ ] `scenario_a_perfect.csv`
- [ ] `scenario_b_no_insurance.csv`
- [ ] `scenario_c_with_insurance.csv`
- [ ] `risk_statistics.txt`

### Reports (in `docs/`)
- [ ] `simulation_summary.md`

## 🔍 Verification

After running simulations:

1. **Check graphs exist:**
   ```bash
   ls -lh docs/assets/*.png
   ```

2. **Check data files:**
   ```bash
   ls -lh data/*.csv
   ```

3. **View website:**
   ```bash
   open docs/index.html  # Mac
   xdg-open docs/index.html  # Linux
   start docs/index.html  # Windows
   ```

4. **Or start local server:**
   ```bash
   python3.10 -m http.server 8000 --directory docs
   # Visit: http://localhost:8000
   ```

## ❌ Troubleshooting

If something fails:

1. **Check Python version:**
   ```bash
   python3.10 --version
   ```
   Must show 3.10.x

2. **Reinstall dependencies:**
   ```bash
   python3.10 -m pip install --upgrade pip
   python3.10 -m pip install -r requirements.txt
   ```

3. **Check for errors:**
   - Read error messages carefully
   - Check that all files exist
   - Verify write permissions in `docs/` and `data/`

4. **Run verification:**
   ```bash
   python3.10 verify_setup.py
   ```

## 📚 Documentation

For more help, see:
- [PYTHON_310_REQUIREMENTS.md](PYTHON_310_REQUIREMENTS.md) - Python 3.10 installation guide
- [QUICK_START.md](QUICK_START.md) - Quick start guide
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Complete project overview
- [README.md](README.md) - Main documentation

## 🎯 Success Criteria

You've successfully completed the setup when:

✅ `python3.10 verify_setup.py` shows all checks passed  
✅ Simulation runs without errors  
✅ All graphs are generated  
✅ Website displays correctly  
✅ Data files contain results  

---

**Ready to impress the Arizona Captive Insurance Association!**
