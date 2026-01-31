# Policy Data - Single Source of Truth

## simulatedPolicies.json

**This is the ONLY copy of the simulated policies data.**

### Location
`captive.integralmass.com/docs/data/simulatedPolicies.json`

### Usage
- The website fetches this file from `data/simulatedPolicies.json` (relative path)
- Edit this file to update policy data
- Changes are immediately reflected on the website

### Why Here?
The web server runs from the `docs/` directory, so data files must be inside `docs/` to be accessible via HTTP. This prevents CORS errors and 404s.

### File Structure
```
captive.integralmass.com/
├── data/                          # Simulation CSV files (Monte Carlo, etc.)
└── docs/                          # Website files (served by HTTP server)
    ├── policy-slips.html          # Fetches data/simulatedPolicies.json
    └── data/                      # ← You are here
        └── simulatedPolicies.json # ← Single source of truth - edit this!
```

### Editing Policy Data
1. Open `captive.integralmass.com/docs/data/simulatedPolicies.json`
2. Make your changes
3. Save the file
4. Refresh the browser - changes appear immediately
