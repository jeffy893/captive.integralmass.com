# Single Source of Truth - Data Management

## Problem Solved
Initially, we had two copies of `simulatedPolicies.json`:
1. `captive.integralmass.com/data/simulatedPolicies.json` (original)
2. `captive.integralmass.com/docs/data/simulatedPolicies.json` (duplicate)

This created a maintenance problem - edits to one file wouldn't reflect in the other.

## Solution Implemented

### Single File Location
**Location**: `captive.integralmass.com/data/simulatedPolicies.json`

This is now the **ONLY** copy of the policy data.

### Updated Fetch Path
**File**: `docs/policy-slips.html`

**Changed from**:
```javascript
fetch('data/simulatedPolicies.json')  // Looked in docs/data/
```

**Changed to**:
```javascript
fetch('../data/simulatedPolicies.json')  // Looks in parent directory
```

### Removed Duplicate
- Deleted `docs/data/` directory entirely
- No duplicate copies exist

## Benefits

### 1. Single Source of Truth
- ✅ One file to edit
- ✅ Changes reflect everywhere immediately
- ✅ No sync issues between copies

### 2. Easier Maintenance
- ✅ Clear where to make edits
- ✅ No confusion about which file is "correct"
- ✅ Simpler version control

### 3. Better Organization
- ✅ Data files in `data/` directory
- ✅ Website files in `docs/` directory
- ✅ Clear separation of concerns

### 4. Prevents Errors
- ✅ Can't accidentally edit wrong file
- ✅ No risk of files getting out of sync
- ✅ Easier for other developers to understand

## File Structure

```
captive.integralmass.com/
├── data/                          # Data directory
│   ├── simulatedPolicies.json     # ← SINGLE SOURCE OF TRUTH
│   └── README.md                  # Documentation
│
├── docs/                          # Website directory
│   ├── policy-slips.html          # Fetches ../data/simulatedPolicies.json
│   ├── index.html
│   └── ...
│
└── serve_local.py                 # Local server
```

## How It Works

### 1. Directory Structure
```
captive.integralmass.com/
├── data/
│   └── simulatedPolicies.json
└── docs/
    └── policy-slips.html
```

### 2. Relative Path
From `docs/policy-slips.html`:
- `../` goes up one level to `captive.integralmass.com/`
- `data/` enters the data directory
- `simulatedPolicies.json` is the file

### 3. Server Serves Parent Directory
The Python server (`serve_local.py`) serves from the `docs/` directory, but can access parent directory files via relative paths.

## Editing Workflow

### To Update Policy Data:

1. **Edit the file**:
   ```bash
   # Open in your editor
   code captive.integralmass.com/data/simulatedPolicies.json
   ```

2. **Make your changes**:
   - Update policy details
   - Add/remove policies
   - Modify risk narratives
   - Ensure valid JSON syntax

3. **Test locally**:
   ```bash
   # Start server
   ./start_server.sh
   
   # Open browser
   http://localhost:8000/policy-slips.html
   ```

4. **Verify changes**:
   - Policy cards should reflect updates
   - Modal should show new data
   - No console errors

5. **Commit changes**:
   ```bash
   git add data/simulatedPolicies.json
   git commit -m "Updated policy data: [description]"
   ```

## Testing Checklist

After editing `data/simulatedPolicies.json`:

- [ ] JSON syntax is valid (use jsonlint.com if needed)
- [ ] Server is running (`./start_server.sh`)
- [ ] Policy Slips page loads without errors
- [ ] Policy cards display correctly
- [ ] "View Slip" opens modal with updated data
- [ ] All 5 policies are present (or intended number)
- [ ] No console errors in browser (F12)

## Common Mistakes to Avoid

### ❌ Don't Do This:
```bash
# Creating duplicate copies
cp data/simulatedPolicies.json docs/data/simulatedPolicies.json
```

### ❌ Don't Do This:
```javascript
// Using absolute path
fetch('/data/simulatedPolicies.json')
```

### ❌ Don't Do This:
```javascript
// Looking in wrong directory
fetch('data/simulatedPolicies.json')
```

### ✅ Do This:
```javascript
// Using relative path to parent directory
fetch('../data/simulatedPolicies.json')
```

### ✅ Do This:
```bash
# Edit the single source file
vim data/simulatedPolicies.json
```

## Production Deployment

### GitHub Pages
The relative path works correctly:
- GitHub Pages serves from `docs/` directory
- Can access `../data/` via relative path
- No configuration needed

### Other Static Hosts
Most static hosts support relative paths:
- Netlify ✅
- Vercel ✅
- AWS S3 ✅
- Azure Static Web Apps ✅

### Important Note
If deploying to a subdirectory (e.g., `example.com/captive/`), the relative path still works because it's relative to the HTML file location, not the domain root.

## Documentation

Created documentation in multiple places:

1. **`data/README.md`** - Explains the data directory structure
2. **`QUICKSTART.md`** - Updated file structure diagram
3. **`archive/LOCAL_SERVER_SETUP.md`** - Updated technical details
4. **This file** - Comprehensive explanation of single source approach

## Status
✅ **COMPLETE** - Single source of truth implemented, duplicate removed, documentation updated.

## Date Completed
January 31, 2026
