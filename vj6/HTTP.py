import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        content = """
        <html>
        <head>
            <title>Moja web stranica</title>
        </head>
        <body>
            <h1>Informacije o studentu</h1>
            <p>Ime: Toni</p>
            <p>Prezime: Culic</p>
            <p>Datum: 2. lipnja 2023.</p>
        </body>
        </html>
        """
        self.wfile.write(content.encode())

port = 8000
server_address = ('', port)
httpd = socketserver.TCPServer(server_address, MyHttpRequestHandler)

print(f"Server sluša na portu {port}.")
httpd.serve_forever()

