#!/usr/bin/python3

import time, threading, os, getopt, sys, socket

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:c:r:')
for (op, ar) in opt:
    if op == '-h':
        host = ar
    if op == '-p':
        port = ar
    if op == '-c':
        letter = ar
    if op == '-r':
        loop = ar


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Haciendo el connect")
t = (host, int(port))
s.connect(t)
print("Handshake realizado con éxito!")


if __name__ == '__main__':
    letter = letter.encode('utf8')
    s.send(letter)
    time.sleep(0.3)
    loop = loop.encode('utf8')
    s.send(loop)