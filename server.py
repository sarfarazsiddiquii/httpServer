from http.server import BaseHTTPRequestHandler, HTTPServer
from handlers.header_processing import process_headers
from handlers.message_handler import handle_get_messages, handle_post_message, handle_put_message, handle_delete_message
import json


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        process_headers(self.headers)

        if self.path == '/messages':
            response = handle_get_messages()
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def do_POST(self):
        process_headers(self.headers)

        if self.path == '/messages':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = json.loads(self.rfile.read(content_length).decode('utf-8'))
            response = handle_post_message(post_data)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def do_PUT(self):
        process_headers(self.headers)

        if self.path.startswith('/messages/'):
            try:
                message_id = int(self.path.split('/')[-1])
            except ValueError:
                self._send_response({"status": "error", "message": "Invalid message ID"})
                return

            content_length = int(self.headers.get('Content-Length', 0))
            put_data = json.loads(self.rfile.read(content_length).decode('utf-8'))

            response = handle_put_message(message_id, put_data)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def do_DELETE(self):
    
        process_headers(self.headers)

    
        if self.path.startswith('/messages/'):
            try:
                message_id = int(self.path.split('/')[-1])
            except ValueError:
                self._send_response({"status": "error", "message": "Invalid message ID"})
                return


            response = handle_delete_message(message_id)
        else:
            response = {"status": "error", "message": "Invalid endpoint"}

        self._send_response(response)

    def _send_response(self, response):
        """Helper method to send a JSON response."""
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


HOST = 'localhost'
PORT = 3000

server = HTTPServer((HOST, PORT), CustomHTTPRequestHandler)
print(f"Server is running at http://{HOST}:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down the server.")
    server.server_close()
