#!/usr/bin/python3

import sys, socket, getopt

if __name__=='__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:t:f:')
    for (op,ar) in opt:
        if op == '-p':
            puerto = int(ar)
        if op == '-t':
            protocolo = str(ar)
        if op == '-f':
            ruta = str(ar)

    if protocolo == 'tcp':
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        serversocket.bind((host, puerto))
        serversocket.listen()
        print("Esperando conexiones")
        clientsocket, addr = serversocket.accept()
        while True:
            f = open(ruta, 'a')
            d = clientsocket.recv(1024)
            msg = d.decode('ascii')
            f.write(msg + '\n')
            print('Dirección:', addr)
            print('Mensaje Recibido: ', msg)
    else:
        if protocolo == 'udp':
            serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            host = socket.gethostname()
            serversocket.bind((host, puerto))
            print("Esperando conexiones")
            while True:
                f = open(ruta, 'a')
                d, addr = serversocket.recvfrom(1024)
                msg = d.decode('ascii')
                f.write(msg + "\n")
                direccion = addr[0]
                puerto = addr[1]

                print('Dirección:', addr, 'Puerto: ', puerto)
                print('Mensaje Recibido: ', msg)












