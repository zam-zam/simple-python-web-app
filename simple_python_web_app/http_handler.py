from http.server import BaseHTTPRequestHandler
from config import config
import json


class HttpHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        response = {
          'app_version': f'{config["app_version"]}',
          'client_id': f'{config["client_id"]}',
          'client_secret': f'{config["client_secret"]}'
        }
        self.wfile.write(json.dumps(response).encode(encoding='utf_8'))
