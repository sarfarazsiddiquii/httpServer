from http.server import BaseHTTPRequestHandler, HTTPServer
from handlers.header_processing import process_headers

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        header_info = process_headers(self.headers)
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "message": "Headers detected",
            "headers": header_info
        }
        self.wfile.write(str(response).encode())

HOST = 'localhost'
PORT = 3000

server = HTTPServer((HOST, PORT), CustomHTTPRequestHandler)
print(f"Server is running at http://{HOST}:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server.")
    server.server_close()
