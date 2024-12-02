from http.server import BaseHTTPRequestHandler, HTTPServer
from handlers.header_processing import process_headers
from handlers.message_handler import handle_get_messages, handle_post_message, handle_put_message, handle_delete_message
from urllib.parse import parse_qs, urlparse
from utils.logger import log_request
import json

class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        process_headers(self.headers)
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)
        
        log_request("GET", path, query_params)

        if path == '/messages':
            response = handle_get_messages(query_params)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def do_POST(self):
        process_headers(self.headers)
        log_request("POST", self.path, None)
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = json.loads(self.rfile.read(content_length).decode('utf-8'))

        if self.path == '/messages':
            response = handle_post_message(post_data)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def do_PUT(self):
        process_headers(self.headers)
        log_request("PUT", self.path, None)
        content_length = int(self.headers.get('Content-Length', 0))
        put_data = json.loads(self.rfile.read(content_length).decode('utf-8'))
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path.startswith('/messages'):
            response = handle_put_message(query_params, put_data)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def do_DELETE(self):
        process_headers(self.headers)
        log_request("DELETE", self.path, None)
        parsed_url = urlparse(self.path)
        path = parsed_url.path
        query_params = parse_qs(parsed_url.query)

        if path.startswith('/messages'):
            response = handle_delete_message(query_params)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def _send_response(self, response):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

HOST = 'localhost'
PORT = 3000

server = HTTPServer((HOST, PORT), CustomHTTPRequestHandler)
print(f"Server is running at http://{HOST}:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server.")
    server.server_close()
