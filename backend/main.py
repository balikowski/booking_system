from http.server import HTTPServer, BaseHTTPRequestHandler
import json 
from urllib.parse import urlparse
import os

HOST = os.getenv("HOST","localhost")
PORT = int(os.getenv("PORT","3333"))

class BookingSystem(BaseHTTPRequestHandler):
    def send_json(self, data: dict, status=200) -> None:
        self.send_response(status) 
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_POST(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path 

        content_length = int(self.headers.get("Content-Length",0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        if data is None:
            self.send_json({"error":" Request body is required"},400)

        routes = {
            "/test_post": self.handle_test_post
        }
        
        handler = routes.get(path)
        if handler is None:
            self.send_json({"error":"Endpoint not found"},404)
            return
        
        handler(data)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path 

        routes = {
            "/test_get": self.handle_test_get
        }

        handler = routes.get(path)
        if handler is None:
            self.send_json({"error":"Endpoint not found"},404)
            return
        
        handler(parsed_path)



    def handle_test_post(self, data: dict) -> None:
        test = data.get("test")
        self.send_json({
            "status": "succes",
            "test": test
        })

    def handle_test_get(self, parsed_path) -> None:
        self.send_json({
            "status": "succes",
            "test": parsed_path
        })


def run_server():
    server = HTTPServer((HOST,PORT),BookingSystem)
    print(f"The server runs on http://{HOST}:{str(PORT)}")
    server.serve_forever()
    
if __name__ == "__main__":
    run_server()