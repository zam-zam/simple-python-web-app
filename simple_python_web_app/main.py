from http.server import HTTPServer

from config import config
from http_handler import HttpHandler

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", config['http_port']), HttpHandler).serve_forever()
