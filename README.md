# Integral Mass Captive Insurance

**A Unified Risk-Management & Financial Suite for Prefab Housing**

> 🏠 **Mission:** Accelerate the manufacturing, installation, and renting of Prefabricated Homes and Accessory Dwelling Units (ADUs) to address the housing crisis.

> ⚠️ **IMPORTANT**: This project requires **Python 3.10** specifically. See installation instructions below.

> 📋 **Disclaimer**: This is a feasibility study presenting actuarially informed concepts awaiting formal review. The platform insures **fortuitous risk** (unforeseen, accidental losses) only—**not speculative risk** (market gambles).

---

## 🎯 What is Integral Mass Captive?

Integral Mass Captive is a **Protected Cell Company (PCC)** providing insurance coverage for the prefab housing ecosystem:

- **General Contractors** installing prefab units across three market segments
- **Property Owners** operating prefab villages (student housing, trailer parks, rural communities)
- **Homebuyers** financing ADU construction through integrated mortgage services
- **Tenants** renting in captive-covered properties

### The Three Market Segments

| Segment | Description | Key Risk Profile |
|---------|-------------|------------------|
| 🎓 **Student Housing** | ADUs near university campuses | High turnover, seasonal demand |
| 👨‍👩‍👧‍👦 **Multi-Generational** | Rent-to-equity instruments with accessibility | Long-term, family transitions |
| 🌾 **Rural Development** | Remote properties with infrastructure challenges | Utility integration, site access |

---

## 🛡️ Core Insurance Products

### 1. Home Gap Coverage
Like auto gap insurance—but for your ADU project. Covers the delta between expected and actual installation costs due to fortuitous events (site complications, supply chain disruptions, utility failures).

### 2. GC Innovation Insurance
Modeled after corporate R&D captives. General Contractors pay premiums to protect against the learning-curve risks of adopting new prefab installation techniques.

### 3. Mortgage-as-a-Service (MaaS)
Conceptual API integration for unified ADU financing. Apply for mortgages directly on the platform with bundled insurance coverage.

### 4. Tenant Portal (In-House Renter's Insurance)
Property owners operating prefab villages can offer renter's insurance directly to tenants through an integrated web portal and AI chatbot.

---

## 🏛️ Protected Cell Company (PCC) Architecture

The captive uses a **cell structure** allowing independent groups to create segregated risk pools:

```
┌─────────────────────────────────────────────────────────┐
│                  INTEGRAL MASS CORE                      │
│    Regulatory Compliance • Reinsurance • Admin          │
└─────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼────┐       ┌────▼────┐       ┌────▼────┐
   │ CELL A  │       │ CELL B  │       │ CELL C  │
   │ Student │       │  Rural  │       │ Property│
   │ Housing │       │  Dev    │       │ Owners  │
   │   GCs   │       │   GCs   │       │ Alliance│
   └─────────┘       └─────────┘       └─────────┘
```

**Benefits:**
- Asset protection (cell failures don't affect other cells)
- Cost efficiency (shared compliance infrastructure)
- Tailored coverage per market segment
- Scalable growth without restructuring

---

## 🏗️ Repository Structure

```
captive.integralmass.com/
├── .github/workflows/   # CI/CD automation
├── docs/                # Public website (GitHub Pages)
│   ├── index.html       # Landing page
│   ├── home-gap-coverage.html
│   ├── mortgage-as-a-service.html
│   ├── tenant-portal.html
│   ├── markets.html
│   ├── simulation.html
│   ├── compliance.html
│   ├── organization.html  # PCC Structure
│   └── assets/          # CSS, images, graphs
├── src/                 # Python simulation engine
│   ├── main.py          # Main runner script
│   ├── actors.py        # GC, Unit, Tenant classes
│   ├── financial_instrument.py
│   ├── queue_sim.py
│   └── risk_model.py
├── data/                # Simulation outputs
└── requirements.txt     # Python dependencies
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10** (required)
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/captive.integralmass.com.git
cd captive.integralmass.com

# Verify Python 3.10
python3.10 --version

# Install dependencies
python3.10 -m pip install -r requirements.txt

# Run simulations
cd src
python3.10 main.py
```

### View Results
Open `docs/index.html` in your browser or visit the live site.

---

## 📊 Simulation Results

| Metric | Value | Significance |
|--------|-------|--------------|
| **Probability of Ruin** | <1% | Over 10-year horizon |
| **Solvency Ratio** | 2.8x | Expected annual claims |
| **Initial Capitalization** | $1M | 4x regulatory minimum |
| **Risk Event Rate** | 15% | Validated via queuing simulation |

---

## 📋 Regulatory Compliance

Demonstrates compliance with **Arizona Revised Statutes Title 20, Chapter 5, Article 2**:

- ✅ Risk Distribution: 12+ independent risk units
- ✅ Minimum Capitalization: $1M (4x minimum)
- ✅ Feasibility Study: Comprehensive simulation analysis
- ✅ PCC Structure: A.R.S. § 20-1098 et seq.

---

## 🔧 Technology Stack

| Layer | Technologies |
|-------|--------------|
| **Simulation** | Python, NumPy, Pandas, SimPy |
| **Visualization** | Matplotlib |
| **Website** | HTML5, CSS3, JavaScript |
| **Hosting** | GitHub Pages |
| **CI/CD** | GitHub Actions |

---

## ⚠️ Important Disclaimers

1. **Not Actuarially Certified**: This is a feasibility study presenting actuarially informed concepts. Formal actuarial review is pending.

2. **Fortuitous Risk Only**: The captive covers fortuitous risk (accidental, unforeseen events) only. Speculative risk (market fluctuations, investment losses, business gambles) is expressly excluded.

3. **Demonstration Purposes**: All forms, portals, and API examples are conceptual demonstrations. No actual insurance policies are issued through this platform.

---

## 📄 License

See [LICENSE](LICENSE) file for details.

## 📞 Contact

Prepared for **Arizona Captive Insurance Association** review.

**Website:** [captive.integralmass.com](https://captive.integralmass.com)

---

*Part of the [Integral Mass](https://www.integralmass.com) ecosystem*
