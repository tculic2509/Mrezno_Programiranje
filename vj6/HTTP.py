import http.server
import socketserver


# Definirajte klasu koja će obrađivati zahtjeve klijenata
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Postavite HTTP status kod 200 (OK)
        self.send_response(200)

        # Postavite zaglavlje Content-type
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Definirajte sadržaj web stranice u HTML formatu
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

        # Pošaljite sadržaj kao odgovor klijentu
        self.wfile.write(content.encode())


# Postavite server na željeni port (u ovom slučaju 8000)
port = 8000
# Slušajte na svim dostupnim sučeljima (0.0.0.0)
server_address = ('', port)

# Stvorite instancu HTTPServer klase s definiranim request handlerom
httpd = socketserver.TCPServer(server_address, MyHttpRequestHandler)

# Pokrenite server
print(f"Server sluša na portu {port}.")
httpd.serve_forever()

