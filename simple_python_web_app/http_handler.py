from http.server import BaseHTTPRequestHandler
from config import config


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>simple_python_web_app</title></head>'.encode())
        self.wfile.write(f"""
                            <body>
                              <p><b>ID клиента:</b> {config['client_id']}</p>
                              <p><b>Секрет клиента:</b> {config['client_secret']}</p>
                            </body>
                         """.encode())
        self.wfile.write(f'</html>'.encode())
