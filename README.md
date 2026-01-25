# Integral Mass Captive Insurance

**A Feasibility Study Rendered in Code**

> ⚠️ **IMPORTANT**: This project requires **Python 3.10** specifically. See [PYTHON_310_REQUIREMENTS.md](PYTHON_310_REQUIREMENTS.md) for installation instructions.

This repository serves as both a simulation engine and public-facing documentation for the Integral Mass Captive Insurance Company, prepared for Arizona Captive Insurance Association (ACIA) licensing review.

## 🎯 Project Overview

Integral Mass Captive provides insurance coverage for 12 General Contractors installing prefab housing units across three distinct market segments:

- **Student Housing**: ADUs near university campuses
- **Multi-Generational**: Rent-to-equity financial instruments with accessibility features
- **Rural Development**: Remote properties with utility infrastructure challenges

## 🏗️ Repository Structure

```
captive.integralmass.com/
├── .github/workflows/   # CI/CD automation
├── docs/                # Public website (GitHub Pages)
│   ├── index.html       # Landing page
│   ├── markets.html     # Market segment details
│   ├── simulation.html  # Simulation results
│   ├── compliance.html  # Regulatory compliance
│   └── assets/          # CSS, images, graphs
├── src/                 # Python simulation engine
│   ├── main.py          # Main runner script
│   ├── actors.py        # GC, Unit, Tenant classes
│   ├── financial_instrument.py  # Multi-gen equity model
│   ├── queue_sim.py     # Queuing theory simulation
│   └── risk_model.py    # Monte Carlo risk analysis
├── data/                # Simulation outputs (CSV)
├── requirements.txt     # Python dependencies
└── project_plan.csv     # Microsoft Project timeline
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.10** (required - not 3.11 or 3.12)
- pip

**First time?** Run the verification script:
```bash
python3.10 verify_setup.py
```

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/captive.integralmass.com.git
cd captive.integralmass.com

# Verify Python 3.10 is installed
python3.10 --version

# Install dependencies
python3.10 -m pip install -r requirements.txt

# Run simulations
cd src
python3.10 main.py
```

### View Results

After running simulations, open `docs/index.html` in your browser or visit the GitHub Pages site.

## 📊 Simulation Components

### 1. Financial Instrument Analysis
Models the multi-generational rent-to-equity instrument, demonstrating how insurance coverage maintains equity accumulation during payment disruptions.

**Key Output**: `docs/assets/financial_instrument_comparison.png`

### 2. Queuing Simulation
Uses SimPy to model resource allocation across 12 GCs serving three markets simultaneously.

**Key Output**: `docs/assets/queue_simulation_results.png`

### 3. Monte Carlo Risk Analysis
Runs 5,000+ simulations over 10 years to validate solvency and capital adequacy.

**Key Output**: `docs/assets/monte_carlo_results.png`

## 📈 Key Results

- **Probability of Ruin**: <1% over 10 years
- **Solvency Ratio**: 2.8x expected annual claims
- **Initial Capitalization**: $1,000,000 (4x regulatory minimum)
- **Risk Event Rate**: 15% (validated through queuing simulation)

## 🔧 Technology Stack

- **Python**: Core simulation engine
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Visualization
- **SimPy**: Discrete event simulation
- **GitHub Actions**: Automated simulation runs
- **GitHub Pages**: Static website hosting

## 📋 Regulatory Compliance

This project demonstrates compliance with Arizona Revised Statutes Title 20, Chapter 5, Article 2:

- ✅ Risk Distribution: 12 independent risk units
- ✅ Minimum Capitalization: $1M (4x minimum)
- ✅ Feasibility Study: Comprehensive simulation analysis
- ✅ Business Plan: Detailed operational model
- ✅ Pro Forma Financials: 10-year projections

## 🤝 Contributing

This is a regulatory submission project. For questions or suggestions, please open an issue.

## 📄 License

See [LICENSE](LICENSE) file for details.

## 📞 Contact

Prepared for Arizona Captive Insurance Association review.

---

**Note**: This is a feasibility study rendered in executable code. All simulations use industry-standard actuarial and operations research methods.