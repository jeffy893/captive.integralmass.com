# Single Source of Truth - Policy Data Configuration

**Date**: 2026-01-31  
**Status**: ✅ Complete

## Problem Solved

The website was unable to load policy slips because:
1. The JSON file was in `captive.integralmass.com/data/` (outside the web server's directory)
2. The web server runs from `docs/` directory
3. Fetch requests to `../data/simulatedPolicies.json` resulted in 404 errors

## Solution Implemented

**Single Source of Truth Location**: `captive.integralmass.com/docs/data/simulatedPolicies.json`

### Changes Made

1. **Created** `docs/data/` directory
2. **Moved** `simulatedPolicies.json` from `data/` to `docs/data/`
3. **Updated** `policy-slips.html` to fetch from `data/simulatedPolicies.json` (relative path)
4. **Deleted** old copy from `captive.integralmass.com/data/`
5. **Preserved** all other CSV files in `captive.integralmass.com/data/` (simulation data)
6. **Created** README files in both locations explaining the structure

### File Structure

```
captive.integralmass.com/
├── data/                              # Simulation data (CSV files)
│   ├── README.md                      # Explains policy data is in docs/data/
│   ├── completed_units.csv
│   ├── monte_carlo_results.csv
│   ├── risk_events.csv
│   └── ... (other CSV files)
│
└── docs/                              # Website files (HTTP server root)
    ├── policy-slips.html              # Fetches data/simulatedPolicies.json
    ├── index.html
    └── data/                          # ← Policy data location
        ├── README.md                  # Explains this is single source of truth
        └── simulatedPolicies.json     # ← EDIT THIS FILE ONLY!
```

## How to Edit Policy Data

1. Open: `captive.integralmass.com/docs/data/simulatedPolicies.json`
2. Make your changes
3. Save the file
4. Refresh browser - changes appear immediately

## Verification

Server logs show successful fetch:
```
[31/Jan/2026 10:42:16] "GET /data/simulatedPolicies.json HTTP/1.1" 200 -
```

## Benefits

✅ Single source of truth - no duplicate files  
✅ Website can access the data (no CORS/404 errors)  
✅ Simulation CSV files preserved in original location  
✅ Clear documentation in both directories  
✅ Immediate updates when editing the JSON file  

## Server Configuration

- **Server Root**: `captive.integralmass.com/docs/`
- **Port**: 8080
- **URL**: http://localhost:8080/policy-slips.html
- **Data URL**: http://localhost:8080/data/simulatedPolicies.json
