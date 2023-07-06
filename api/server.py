from http.server import HTTPServer
from handler import WebRequestHandler

PORT = 8080

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), WebRequestHandler)
    print(f"🚀 Server fired on port {PORT}...")
    server.serve_forever()
