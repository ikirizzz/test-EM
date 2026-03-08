from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('/', ''):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Hello from Effective Mobile!')
        else:
            self.send_error(404)
            self.end_headers()

if __name__ == "__main__":
    httpd = HTTPServer(('0.0.0.0', 8080), HelloHandler)
    print('Backend started on port 8080')
    httpd.serve_forever()
