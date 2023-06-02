
import socket
import subprocess
import sys
from datetime import datetime
from print_machine import print_machine_info

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

hostname = input("Upisi host name: ")
hostnameIP = socket.gethostbyname(hostname)
print("IP adresa od hostaamea {} je: {}".format(hostname, hostnameIP))

port1 = int(input("Upisi pocetni port: "))
port2 = int(input("Upisi zavrsni port: "))
print("prvi port: {}, drugi port: {}".format(port1, port2))


def portscanner(port):
    if socket.connect_ex((hostname, port)):
        print("Port {} je otvoren." % (port))


try:
    for port in range(port1, port2 + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostnameIP, port))
        print("Skeniram port {}.".format(port))
        if result == 0:
            portscanner(port)
            sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

print('skeniranje završeno.')
