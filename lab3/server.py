import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((socket.gethostname(), 8080))

socket_server.listen(5)
