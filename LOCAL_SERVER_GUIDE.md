# Local Development Server Guide

## Why You Need a Local Server

The Policy Slips page uses JavaScript to fetch data from `data/simulatedPolicies.json`. Due to browser security restrictions (CORS policy), this won't work when opening HTML files directly from your file system (`file://` protocol). You need to run a local web server.

## Quick Start

### Option 1: Using the Provided Scripts (Easiest)

#### On Mac/Linux:
```bash
cd captive.integralmass.com
./start_server.sh
```

#### On Windows:
```cmd
cd captive.integralmass.com
start_server.bat
```

The server will start on **http://localhost:8000**

### Option 2: Using Python Directly

If you have Python 3 installed:

```bash
cd captive.integralmass.com
python3 serve_local.py
```

Or use Python's built-in HTTP server:

```bash
cd captive.integralmass.com/docs
python3 -m http.server 8000
```

### Option 3: Using Node.js (if you have it installed)

```bash
cd captive.integralmass.com/docs
npx http-server -p 8000
```

## Accessing the Website

Once the server is running, open your browser and go to:

- **Home Page**: http://localhost:8000/index.html
- **Policy Slips**: http://localhost:8000/policy-slips.html
- **Policies**: http://localhost:8000/policies.html
- **Markets**: http://localhost:8000/markets.html
- **Simulation**: http://localhost:8000/simulation.html
- **Compliance**: http://localhost:8000/compliance.html
- **Organization**: http://localhost:8000/organization.html

## Stopping the Server

Press **Ctrl+C** in the terminal/command prompt where the server is running.

## Troubleshooting

### "Port 8000 is already in use"
Another application is using port 8000. Either:
1. Stop the other application
2. Edit `serve_local.py` and change `PORT = 8000` to a different number (e.g., `PORT = 8080`)

### "Python not found"
Install Python 3 from https://www.python.org/downloads/

### Policy cards not showing
1. Make sure you're accessing via `http://localhost:8000` (not `file://`)
2. Check the browser console (F12) for errors
3. Verify `data/simulatedPolicies.json` exists

### JSON file not loading
1. Ensure you're in the correct directory when starting the server
2. The server should be serving from the `docs/` directory
3. Check that the path to JSON is correct: `data/simulatedPolicies.json`

## Features of the Custom Server Script

The `serve_local.py` script includes:
- ✅ CORS headers enabled (allows fetch requests)
- ✅ Cache control disabled (always loads fresh content)
- ✅ Custom logging with timestamps
- ✅ Helpful startup message with all page URLs
- ✅ Graceful shutdown with Ctrl+C

## Alternative: VS Code Live Server Extension

If you use Visual Studio Code:
1. Install the "Live Server" extension
2. Right-click on `index.html` in the `docs/` folder
3. Select "Open with Live Server"

## Alternative: Browser Extensions

Some browsers have extensions that can bypass CORS for local development:
- Chrome: "Allow CORS: Access-Control-Allow-Origin"
- Firefox: "CORS Everywhere"

**⚠️ Warning**: Only use these for local development, and disable them when browsing the web!

## Viewing on Mobile Devices

To view the site on your phone/tablet on the same network:

1. Find your computer's local IP address:
   - **Mac/Linux**: `ifconfig | grep inet`
   - **Windows**: `ipconfig`
   
2. Look for something like `192.168.1.x`

3. On your mobile device, go to: `http://192.168.1.x:8000/index.html`

## Production Deployment

For production deployment to GitHub Pages or other hosting:
- The site is static HTML/CSS/JS
- No server-side processing required
- Just upload the `docs/` folder contents
- GitHub Pages will serve it correctly with proper CORS headers

## Questions?

If you encounter issues:
1. Check the browser console (F12 → Console tab)
2. Check the server terminal output for errors
3. Verify file paths are correct
4. Ensure you're accessing via `http://localhost:8000` not `file://`
