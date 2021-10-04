#!/usr/bin/python3

import sys, socket, getopt


(opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
for (op, ar) in opt:
    if op == '-a':
        host = (ar)
    if op == '-p':
        puerto = int(ar)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, puerto))
msg = input('Introduzca un texto: ')
s.send(msg.encode('utf8'))
s.close()
