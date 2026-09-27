import time, os
from http.server import HTTPServer, BaseHTTPRequestHandler

class SupernovaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "alive", "name": "Supernova AI", "wallet": "0x0389EC6C58Fce8976787D782d8d8bF9Dd4dAb967"}')

def run_server():
    port = int(os.environ.get("PORT", 8000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, SupernovaHandler)
    print(f"Supernova Agent menyala di port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
