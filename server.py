import http.server
import socketserver
import urllib.parse
import os
import sys

DEFAULT_PORT = 3005

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        # Handle Next.js image optimization endpoint fallback
        if parsed.path == '/_next/image':
            query = urllib.parse.parse_qs(parsed.query)
            if 'url' in query:
                img_url = query['url'][0]
                self.path = img_url
        elif parsed.path == '/' or parsed.path == '':
            self.path = '/index.html'
        
        return super().do_GET()

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.js'):
            return 'application/javascript; charset=utf-8'
        if path.endswith('.css'):
            return 'text/css; charset=utf-8'
        return super().guess_type(path)

def run():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PORT
    while port < 65535:
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(f"\n======================================================")
                print(f"RehanXP portfolio is live at: http://localhost:{port}")
                print(f"======================================================\n")
                httpd.serve_forever()
                break
        except OSError:
            print(f"Port {port} is in use, trying {port + 1}...")
            port += 1

if __name__ == '__main__':
    run()
