#!/usr/bin/python3

import sys, socket, getopt


def resp(datos):
    if datos == '200':
        print(datos, 'OK')
    else:
        if datos == '400':
            print(datos, 'Comando válido, pero fuera de secuencia.')
        else:
            if datos == '500':
                print((datos, 'Comando inválido.'))
            else:
                if datos == '404':
                    print(datos, 'Clave errónea.')
                else:
                    if datos == '405':
                        print(datos, 'Cadena nula.')


if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:')
    for (op,ar) in opt:
        if op == '-a':
            host = ar
        if op == '-p':
            puerto = int(ar)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, puerto))

    ok = '200'
    while True:
        nombre = input('Ingrese su nombre: ')
        msg = 'hello|' + nombre
        s.send(msg.encode('ascii'))
        datos = s.recv(512).decode("ascii")
        resp(datos)
        if datos == ok:
            while True:
                email = input('Ingrese su email: ')
                msg = 'email|' + email
                s.send(msg.encode('ascii'))
                datos = s.recv(512).decode('ascii')
                resp(datos)
                if datos == ok:
                    while True:
                        clave = str(input('Ingrese la clave: '))
                        msg = 'key|' + str(clave)
                        s.send(msg.encode('ascii'))
                        datos = s.recv(512).decode('ascii')
                        resp(datos)
                        if datos == ok:
                            print('Finalizando conexión...')
                            msg = 'salir'
                            s.send(msg.encode('ascii'))
                            data = s.recv(512).decode('ascii')
                            resp(datos)
                            if datos == ok:
                                s.close()
                                sys.exit(0)


