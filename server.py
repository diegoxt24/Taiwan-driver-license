#!/usr/bin/env python3
"""
Taiwan Driving License Prep Server (Tailscale & Local Network Ready)
Run this server: python server.py
Access from PC, iPad, or Pixel 10 Pro over local Wi-Fi or Tailscale network!
"""
import http.server
import socketserver
import os
import sys
import socket

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def handle_one_request(self):
        try:
            super().handle_one_request()
        except (ConnectionResetError, BrokenPipeError):
            pass

def get_ip_addresses():
    ips = []
    try:
        hostname = socket.gethostname()
        for info in socket.getaddrinfo(hostname, None):
            ip = info[4][0]
            if ':' not in ip and ip not in ips and not ip.startswith('127.'):
                ips.append(ip)
    except Exception:
        pass
    return ips

if __name__ == "__main__":
    print("=" * 65)
    print(" 🇹🇼 TAIWAN DRIVING & MOTORCYCLE LICENSE PREP SERVER (SHEPPARD AIR STYLE)")
    print("=" * 65)
    print(f" Serving Directory: {DIRECTORY}")
    print(f" Local Machine Link: http://localhost:{PORT}")
    
    ips = get_ip_addresses()
    if ips:
        print("\n 📱 Access on your iPad & Google Pixel 10 Pro (Tailscale / Wi-Fi):")
        for ip in ips:
            print(f"   ➜ http://{ip}:{PORT}")
    else:
        print(f"\n 📱 Network Link: http://<YOUR_TAILSCALE_OR_WIFI_IP>:{PORT}")
    
    print("=" * 65)
    print(" Press Ctrl+C to stop server.\n")

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped safely.")
        sys.exit(0)
