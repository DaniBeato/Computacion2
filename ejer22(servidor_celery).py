import sys, getopt, socket, ejer22_calculadora_celery

def calcular(operacion,x,y):
    if operacion == 'sumar':
            respuesta = ejer22_calculadora_celery.suma.delay(x,y)
    else:
        if operacion == 'restar':
            respuesta = ejer22_calculadora_celery.resta.delay(x,y)
        else:
            if operacion == 'mult':
                respuesta = ejer22_calculadora_celery.mult.delay(x,y)
            else:
                if operacion == 'div':
                    respuesta = ejer22_calculadora_celery.div.delay(x,y)
                else:
                    if operacion == 'pot':
                        respuesta = ejer22_calculadora_celery.pot.delay(x, y)
    return respuesta

(opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')
for (op, ar) in opt:
    if op == '-h':
        host = ar
    elif op == '-p':
        port = int(ar)
    else:
        sys.exit()
        
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen()
print("Esperando conexiones remotas (accept)")
while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    operacion = clientsocket.recv(512).decode()
    clientsocket.send('recibido'.encode('utf-8'))
    x = clientsocket.recv(512).decode()
    clientsocket.send('recibido'.encode('utf-8'))
    y = clientsocket.recv(512).decode()
    clientsocket.send('recibido'.encode('utf-8'))
    calculo = calcular(operacion, x, y)
    print('Se ha calculado ', x, ' ', operacion, ' ', y)
    print(calculo)
    clientsocket.send(str(calcular).encode('utf-8'))
