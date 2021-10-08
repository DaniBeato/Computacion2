#!/usr/bin/python3

import time, threading, getopt, sys, socket

(opt, arg) = getopt.getopt(sys.argv[1:], 'p:f:')
for (op, ar) in opt:
    if op == '-p':
        port = ar
    if op == '-f':
        name_file = ar

serversocket = socket.socket(socket.AF_INET)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
t = (host,int(port))
serversocket.bind(t)
serversocket.listen()


def write_file(clientsocket):
    letter = clientsocket.recv(1024)
    letter = letter.decode('utf8')
    loop = clientsocket.recv(1024)
    loop = loop.decode('utf8')
    file = open(name_file, 'a')
    lock.acquire()
    for l in range(int(loop)):
        file.write(letter)
        file.flush()
        time.sleep(1)
    lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    while True:
        print("Esperando conexiones remotas (accept), host: ", host)
        clientsocket, addr = serversocket.accept()
        print("Got a connection from %s" % str(addr))
        son = threading.Thread(target=write_file, args=(clientsocket,), daemon=True)
        son.start()



