# Quick Start Guide

## 🚀 Get Running in 3 Steps

### Step 0: Verify Setup (Recommended)
```bash
python3.10 verify_setup.py
```
This will check that Python 3.10 and all dependencies are properly installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/captive.integralmass.com.git
cd captive.integralmass.com
```

### Step 2: Run the Simulation

**On Linux/Mac:**
```bash
./run_simulation.sh
```

**On Windows:**
```cmd
run_simulation.bat
```

**Manual (any OS):**
```bash
python3.10 -m pip install -r requirements.txt
cd src
python3.10 main.py
```

### Step 3: View Results

**Open the website:**
```bash
# Option 1: Direct
open docs/index.html  # Mac
xdg-open docs/index.html  # Linux
start docs/index.html  # Windows

# Option 2: Local server
python -m http.server 8000 --directory docs
# Then visit: http://localhost:8000
```

---

## 📊 What Gets Generated

After running the simulation, you'll find:

### Graphs (in `docs/assets/`)
- `financial_instrument_comparison.png` - Equity accumulation scenarios
- `queue_simulation_results.png` - GC utilization and wait times
- `monte_carlo_results.png` - Solvency analysis

### Data Files (in `data/`)
- `monte_carlo_results.csv` - Full simulation results
- `completed_units.csv` - Installation tracking
- `risk_events.csv` - Risk event log
- `scenario_*.csv` - Financial instrument scenarios

### Reports (in `docs/`)
- `simulation_summary.md` - Executive summary

---

## 🔧 Troubleshooting

### "Python not found"
Install Python 3.10 specifically from [python.org](https://python.org/downloads/)

**Linux/Mac:**
```bash
# Check if Python 3.10 is installed
python3.10 --version

# If not, install it:
# Ubuntu/Debian
sudo apt install python3.10 python3.10-venv

# macOS (using Homebrew)
brew install python@3.10
```

**Windows:**
1. Download Python 3.10.x from python.org
2. Run installer and check "Add Python to PATH"
3. Restart command prompt

### "pip install fails"
Try:
```bash
python3.10 -m pip install --upgrade pip
python3.10 -m pip install -r requirements.txt
```

### "Module not found"
Make sure you're in the virtual environment:
```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate.bat  # Windows
```

### Simulation runs but no graphs
Check that matplotlib is installed:
```bash
python3.10 -m pip install matplotlib
```

---

## 📖 Understanding the Output

### Financial Instrument Graph
- **Green line**: Perfect payments (baseline)
- **Red dashed line**: No insurance (shows equity loss)
- **Blue line**: With insurance (maintains trajectory)

### Queue Simulation Graph
- **Top Left**: GC utilization (jobs completed per contractor)
- **Top Right**: Wait time distribution
- **Bottom Left**: Risk events by market
- **Bottom Right**: Market share pie chart

### Monte Carlo Graph
- **Top Left**: Final capital distribution
- **Top Right**: Solvency ratio over time
- **Bottom Left**: Sample capital trajectories
- **Bottom Right**: Key risk metrics

---

## 🎯 Key Files to Review

| File | Purpose |
|------|---------|
| `docs/index.html` | Main landing page |
| `docs/simulation.html` | Results dashboard |
| `docs/compliance.html` | Regulatory documentation |
| `src/main.py` | Simulation orchestrator |
| `src/risk_model.py` | Monte Carlo engine |
| `IMPLEMENTATION_SUMMARY.md` | Complete project overview |

---

## 💡 Tips

1. **First time?** Start with `docs/index.html` to understand the business model
2. **Want to modify?** Edit parameters in `src/risk_model.py` and re-run
3. **Need data?** All CSV files are in `data/` folder
4. **Sharing results?** Push to GitHub and enable GitHub Pages

---

## 📞 Need Help?

- Check `IMPLEMENTATION_SUMMARY.md` for detailed documentation
- Review `README.md` for technical details
- Open an issue on GitHub for questions

---

**Ready to impress the Arizona Captive Insurance Association? Run the simulation and explore the results!**
