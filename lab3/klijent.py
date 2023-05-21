import socket

socket_klijent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_klijent.connect(("www.google.com", 80))
