from os import environ

config = {
    'app_version': "1.2.1",
    'client_id': environ.get("CLIENT_ID", "DefaultID"),
    'client_secret': environ.get("CLIENT_SECRET", "DefaultSecret"),
    'http_port': environ.get("HTTP_PORT", 8080),
}
