# -- coding: utf-8 --
#echo_client.py

import socket
import datetime

from vj_zad1 import print_machine_info

print(datetime.datetime.now())
print_machine_info()

host = socket.gethostname()
port = 12345

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect_ex((host, port))

upit=input('Unesite tekst: ')
ime='kbs'

if(upit == ime):
    print('Unos nije podržan.')



client_socket.send(upit.encode('ascii'))

data = client_socket.recv(1024)

print (data.decode('ascii'))
client_socket.close()
