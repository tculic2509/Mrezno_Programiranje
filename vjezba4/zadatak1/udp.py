import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
MESSAGE = b"Hello, World!"

print("UDP IP: %s" % UDP_IP)
print("UDP port: %s" % UDP_PORT)
print("Message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
