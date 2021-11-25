import sys, socket, getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:o:n:m:')
for (op, ar) in opt:
    if op == '-h':
        host = ar
    else:
        if op == '-p':
            port = int(ar)
        else:
            if op == '-o':
                operacion = ar
            else:
                if op == '-n':
                    x = ar
                else:
                    if op == '-m':
                        y = ar
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(operacion.encode('utf-8'))
data = s.recv(512).decode('utf-8')
s.send(x.encode('utf-8'))
data = s.recv(512).decode()
s.send(y.encode('utf-8'))
data = s.recv(512).decode()
print(data)
s.close()
sys.exit()
