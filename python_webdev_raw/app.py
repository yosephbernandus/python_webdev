import http.server
import socketserver
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        hello_world = "Hello World"
        self.wfile.write(f"{hello_world}".encode())


httpd = socketserver.TCPServer(("", 8002), Handler)
print("Starting HTTP Server on PORT 8002")
httpd.serve_forever()
