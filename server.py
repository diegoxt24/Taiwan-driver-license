import http.server
import socketserver
import os
import sys
import socket
import json

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(DIRECTORY, "user_sync_state.json")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Accept')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path.startswith('/api/sync') or self.path.startswith('/user_sync_state.json'):
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                new_state = json.loads(post_data.decode('utf-8'))
                
                # Merge with existing file state on server disk
                current_state = {}
                if os.path.exists(STATE_FILE):
                    try:
                        with open(STATE_FILE, 'r', encoding='utf-8') as f:
                            current_state = json.load(f)
                    except Exception:
                        current_state = {}

                # Deep union merge for all users and modules
                for prof in ['diego', 'johana', 'alejandro']:
                    if prof in new_state:
                        if prof not in current_state:
                            current_state[prof] = new_state[prof]
                        else:
                            for mod in ['motorcycle', 'car']:
                                if mod in new_state[prof]:
                                    if mod not in current_state[prof]:
                                        current_state[prof][mod] = new_state[prof][mod]
                                    else:
                                        # Merge studied, failed, bookmarks
                                        for key in ['studiedQuestions', 'failedQuestions', 'bookmarks']:
                                            c_list = current_state[prof][mod].get(key, [])
                                            n_list = new_state[prof][mod].get(key, [])
                                            merged = list(set(c_list + n_list))
                                            current_state[prof][mod][key] = merged
                                        # Keep latest lastIndices
                                        if 'lastIndices' in new_state[prof][mod]:
                                            current_state[prof][mod]['lastIndices'] = new_state[prof][mod]['lastIndices']

                current_state['last_updated'] = new_state.get('last_updated', 0)
                
                # Save to disk
                with open(STATE_FILE, 'w', encoding='utf-8') as f:
                    json.dump(current_state, f, indent=2, ensure_ascii=False)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "data": current_state}).encode('utf-8'))
                print("✓ Successfully synchronized and saved state from device to server disk!")
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
                return

        super().do_POST()

    def do_PUT(self):
        self.do_POST()

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
