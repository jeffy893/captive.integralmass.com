# Local Server Setup - Complete

## Issue Identified
The Policy Slips page was not displaying policy cards because:
1. JavaScript uses `fetch()` to load `data/simulatedPolicies.json`
2. Browser security (CORS policy) blocks `fetch()` when opening files directly via `file://` protocol
3. A local web server is required to serve the files via `http://` protocol

## Solution Implemented

### 1. Created Python Server Script (`serve_local.py`)
- Simple HTTP server using Python's built-in `http.server` module
- Serves the `docs/` directory on port 8000
- Includes CORS headers to allow fetch requests
- Disables caching for development
- Custom logging with timestamps
- Helpful startup message with all page URLs
- Graceful shutdown with Ctrl+C

### 2. Created Startup Scripts

**Mac/Linux (`start_server.sh`):**
- Bash script to launch the Python server
- Tries python3.10, python3, then python
- Executable permissions set with `chmod +x`

**Windows (`start_server.bat`):**
- Batch file to launch the Python server
- Tries python3.10, python3, then python
- Error handling for missing Python

### 3. Single Source of Truth for Data
**Best Practice**: Keep JSON file in ONE location
- Location: `captive.integralmass.com/data/simulatedPolicies.json`
- HTML fetches from: `../data/simulatedPolicies.json` (relative path)
- **No duplicate copies** - edit once, changes reflect everywhere

**Why this matters**:
- Prevents sync issues between multiple copies
- Single file to maintain and update
- Clear source of truth for policy data
- Easier version control

### 4. Created Documentation

**QUICKSTART.md:**
- Simple instructions to start the server
- Browser URLs for all pages
- Key features to explore

**LOCAL_SERVER_GUIDE.md:**
- Comprehensive guide with multiple server options
- Troubleshooting section
- Mobile device viewing instructions
- Alternative methods (VS Code Live Server, Node.js, etc.)

## Files Created/Modified

### New Files:
1. `captive.integralmass.com/serve_local.py` - Python HTTP server
2. `captive.integralmass.com/start_server.sh` - Mac/Linux startup script
3. `captive.integralmass.com/start_server.bat` - Windows startup script
4. `captive.integralmass.com/QUICKSTART.md` - Quick start guide
5. `captive.integralmass.com/LOCAL_SERVER_GUIDE.md` - Comprehensive guide
6. `captive.integralmass.com/docs/data/simulatedPolicies.json` - Copied JSON file

### File Structure:
```
captive.integralmass.com/
├── docs/                          # Website root
│   ├── index.html
│   ├── policy-slips.html          # Fetches ../data/simulatedPolicies.json
│   ├── policies.html
│   ├── markets.html
│   ├── simulation.html
│   ├── compliance.html
│   ├── organization.html
│   └── assets/
│       ├── style.css
│       └── *.png
├── data/                          # Single source of truth for data
│   └── simulatedPolicies.json     # ← EDIT THIS FILE ONLY
├── serve_local.py                 # ← NEW
├── start_server.sh                # ← NEW
├── start_server.bat               # ← NEW
├── QUICKSTART.md                  # ← NEW
└── LOCAL_SERVER_GUIDE.md          # ← NEW
```

## How to Use

### Step 1: Start the Server
```bash
# Mac/Linux
cd captive.integralmass.com
./start_server.sh

# Windows
cd captive.integralmass.com
start_server.bat
```

### Step 2: Open Browser
Navigate to: **http://localhost:8000/index.html**

### Step 3: View Policy Slips
Click "Policy Slips" in the navigation or go to:
**http://localhost:8000/policy-slips.html**

### Step 4: Stop Server
Press **Ctrl+C** in the terminal

## Server Output Example
```
============================================================
Integral Mass Captive Insurance - Local Development Server
============================================================

Serving from: /path/to/captive.integralmass.com/docs
Server running at: http://localhost:8000

Available pages:
  • Home:          http://localhost:8000/index.html
  • Markets:       http://localhost:8000/markets.html
  • Simulation:    http://localhost:8000/simulation.html
  • Compliance:    http://localhost:8000/compliance.html
  • Organization:  http://localhost:8000/organization.html
  • Policies:      http://localhost:8000/policies.html
  • Policy Slips:  http://localhost:8000/policy-slips.html

Press Ctrl+C to stop the server
============================================================
```

## Why This Works

1. **HTTP Protocol**: Server serves files via `http://` instead of `file://`
2. **CORS Headers**: Server includes `Access-Control-Allow-Origin: *` header
3. **Relative Path**: HTML uses `../data/simulatedPolicies.json` to access parent directory
4. **Single Source**: One JSON file to maintain - no duplicate copies
5. **No Caching**: Cache-Control headers ensure fresh content on reload

## Browser Console Verification

When the page loads successfully, you should see in the browser console (F12):
```
Loaded 5 policies from simulatedPolicies.json
```

If there's an error, you'll see:
```
Error loading policies: [error message]
```

## Alternative Server Methods

### Python Built-in:
```bash
cd captive.integralmass.com/docs
python3 -m http.server 8000
```

### Node.js:
```bash
cd captive.integralmass.com/docs
npx http-server -p 8000
```

### VS Code:
1. Install "Live Server" extension
2. Right-click `index.html` in `docs/`
3. Select "Open with Live Server"

## Production Deployment

For GitHub Pages or other static hosting:
- Upload contents of `docs/` folder
- No server-side code needed
- Static hosting automatically provides correct CORS headers
- JSON file will load correctly

## Testing Checklist

✅ Server starts without errors
✅ Can access http://localhost:8000/index.html
✅ Navigation links work
✅ Policy Slips page loads
✅ Policy cards display (5 cards)
✅ "View Slip" button opens modal
✅ Modal shows policy details
✅ Claims table is visible
✅ Simulated disclaimer appears at bottom
✅ Mobile responsive (test at 768px width)
✅ Table scrolls horizontally on mobile

## Status
✅ **COMPLETE** - Local server setup working, JSON file in correct location, all documentation created.

## Date Completed
January 31, 2026
