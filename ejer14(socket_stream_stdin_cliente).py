#!/usr/bin/python3

import sys, socket, getopt

if __name__=='__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:t:')
    for (op,ar) in opt:
        if op == '-a':
            host = (ar)
        if op == '-p':
            puerto = int(ar)
        if op == '-t':
            protocolo = str(ar)

    if protocolo == 'tcp':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, puerto))
        while True:
            try:
                msg = input('Ingrese el mensaje a enviar: ')
                s.send(msg.encode('ascii'))
            except EOFError:
                s.close()
                break
    else:
        if protocolo == 'udp':
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                try:
                    msg = input('Ingrese el mensaje a enviar: ').encode()
                    s.sendto(msg, (host, puerto))
                except EOFError:
                    s.sendto("".encode(), (host, puerto))
                    s.close()
                    break






