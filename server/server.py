from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

hostName = "0.0.0.0"
serverPort = 80

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Redirect to Streamlit app
            self.send_response(302)  # HTTP 302 is for redirect
            self.send_header("Location", "http://localhost:8501")  # Streamlit default port
            self.end_headers()
        else:
            self.send_response(404)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

if __name__ == "__main__":
    # Start the HTTP server
    webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
    print(f"Server started at http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
