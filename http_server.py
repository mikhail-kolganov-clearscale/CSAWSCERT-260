import http.server
import socketserver
from http import HTTPStatus
import os

if "MY_HTTP_PORT" in os.environ:
    try:
        port = int(os.environ["MY_HTTP_PORT"])
    except Exception as e:
        port = 8080
else:
    port = 8080

print(f"Starting HTTP server on the port: {port}")

text="This is my initial Hello-World text!!!"


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(str.encode(text))


httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()