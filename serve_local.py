#!/usr/bin/env python3
"""
Simple HTTP server for local development of the Integral Mass Captive website.
Serves the docs/ directory on http://localhost:8000
"""

import http.server
import socketserver
import os
import sys

# Change to the docs directory
docs_dir = os.path.join(os.path.dirname(__file__), 'docs')
os.chdir(docs_dir)

PORT = 8080

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow fetch requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.log_date_time_string()}] {format % args}")

Handler = MyHTTPRequestHandler

print("=" * 60)
print("Integral Mass Captive Insurance - Local Development Server")
print("=" * 60)
print(f"\nServing from: {os.getcwd()}")
print(f"Server running at: http://localhost:{PORT}")
print("\nAvailable pages:")
print(f"  • Home:          http://localhost:{PORT}/index.html")
print(f"  • Markets:       http://localhost:{PORT}/markets.html")
print(f"  • Simulation:    http://localhost:{PORT}/simulation.html")
print(f"  • Compliance:    http://localhost:{PORT}/compliance.html")
print(f"  • Organization:  http://localhost:{PORT}/organization.html")
print(f"  • Policies:      http://localhost:{PORT}/policies.html")
print(f"  • Policy Slips:  http://localhost:{PORT}/policy-slips.html")
print("\nPress Ctrl+C to stop the server")
print("=" * 60)
print()

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\n\nServer stopped.")
    sys.exit(0)
except OSError as e:
    if e.errno == 48:  # Address already in use
        print(f"\n❌ Error: Port {PORT} is already in use.")
        print(f"   Try closing other applications or use a different port.")
        sys.exit(1)
    else:
        raise
