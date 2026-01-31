# Quick Start Guide - Integral Mass Captive Insurance Website

## 🚀 Start the Local Server

### Mac/Linux:
```bash
cd captive.integralmass.com
./start_server.sh
```

### Windows:
```cmd
cd captive.integralmass.com
start_server.bat
```

## 🌐 Open in Browser

Once the server starts, open your browser and go to:

**http://localhost:8000/index.html**

## 📄 View Policy Slips

Navigate to the Policy Slips page to see the simulated policies:

**http://localhost:8000/policy-slips.html**

Or click "Policy Slips" in the navigation menu.

## ⚠️ Important Notes

1. **You MUST use a local server** - Opening HTML files directly (`file://`) won't work due to browser security restrictions
2. The server must be running to view the Policy Slips page
3. Press **Ctrl+C** to stop the server when done

## 📁 File Structure

```
captive.integralmass.com/
├── docs/                          # Website files
│   ├── index.html                 # Home page
│   ├── policy-slips.html          # Policy slips page (fetches ../data/simulatedPolicies.json)
│   ├── policies.html              # Policies page
│   └── assets/                    # CSS, images, etc.
├── data/                          # Data files (single source of truth)
│   └── simulatedPolicies.json     # Policy data - edit this file only!
├── serve_local.py                 # Python server script
├── start_server.sh                # Mac/Linux startup script
└── start_server.bat               # Windows startup script
```

**Important**: The JSON file is in `data/` (parent directory), not `docs/data/`. This ensures a single source of truth - edit `data/simulatedPolicies.json` and changes will be reflected immediately.

## 🔧 Troubleshooting

**Problem**: Policy cards not showing
- **Solution**: Make sure you're accessing via `http://localhost:8000` not `file://`

**Problem**: Port 8000 already in use
- **Solution**: Edit `serve_local.py` and change `PORT = 8000` to `PORT = 8080`

**Problem**: Python not found
- **Solution**: Install Python 3 from https://www.python.org/downloads/

## 📱 View on Mobile

1. Find your computer's IP address (e.g., 192.168.1.5)
2. On your phone, go to: `http://192.168.1.5:8000/index.html`

## 🎯 Key Features to Explore

1. **Policy Slips Page** - View 5 simulated high-tech industrial risk policies
2. **Modal View** - Click "View Slip" to see detailed policy documentation
3. **ACORD 25 Header** - Professional insurance certificate format
4. **Lloyd's MRC Body** - Comprehensive risk details and narratives
5. **Mobile Responsive** - Tables scroll horizontally on mobile devices
6. **Simulated Disclaimer** - Clear warning that policies are for demonstration

Enjoy exploring the Integral Mass Captive Insurance feasibility study!
