#!/usr/bin/python3

import socket, sys, getopt
from datetime import datetime


def archivo_log(comando, fecha):
    contenido = (fecha + '   ' + comando + '   ')
    archivo = open('log', 'a')
    archivo.writelines(contenido)
    archivo.close()





s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6000
print("Haciendo el connect")
s.connect((host, port))
print("Handshake realizado con exito!")
while True:
    comando = input('Ingrese los comandos a ejecutar:')
    (opt, arg) = getopt.getopt(sys.argv[1:], 'l', [])
    for (op, ar) in opt:
        if (op == '-l'):
            fecha = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
            archivo_log(comando, fecha)
    s.send(comando.encode('utf8'))
    salida = s.recv(1024)
    salida.decode('utf8')
    print(salida)

