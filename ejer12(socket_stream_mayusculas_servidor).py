#!/usr/bin/python3

import sys, socket, getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'p:')
for (op, ar) in opt:
    if op == '-p':
        puerto = int(ar)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, puerto))
serversocket.listen()
print('Esperando conexiones remotas...')
print('host: ', host, 'puerto: ', puerto)
clientsocket, addr = serversocket.accept()
print('Se ha conetado:', str(addr))
datos = clientsocket.recv(1024)
clientsocket.close()
print('Se ha recibido: ', datos.decode('utf8').upper())

