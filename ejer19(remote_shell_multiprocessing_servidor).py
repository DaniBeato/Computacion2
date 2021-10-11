#!/usr/bin/python3
import socketserver, subprocess, os, threading, socket


class ThreadedRequestHandler(socketserver.BaseRequestHandler,):
    def handle(self):
        while True:
            data = self.request.recv(1024)
            data = (data.decode('utf8'))
            data = subprocess.Popen([data], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = data.communicate()
            if data.returncode == 0:
                envio = ("OK     " + stdout)
                self.request.send(envio.encode('utf8'))
            else:
                envio = ("ERROR   " + stderr)
                self.request.send(envio.encode('utf8'))

class ThreadedServer(socketserver.ThreadingMixIn,socketserver.TCPServer,):
    pass


if __name__ == '__main__':
    address = (socket.gethostname(), 6000)
    server = ThreadedServer(address, ThreadedRequestHandler)
    print("Esperando conexiones remotas (accept)")
    server.serve_forever()

