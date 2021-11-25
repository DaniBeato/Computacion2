#!/usr/bin/python3

import socket, sys, getopt, asyncio
from datetime import datetime


async def archivo_log(comando, fecha):
    contenido = (fecha + '   ' + comando + '   ')
    archivo = open('log', 'a')
    archivo.writelines(contenido)
    archivo.close()


async def main():
    host = socket.gethostname()
    port = 6000
    print("Haciendo el connect")
    lector, escritor = await asyncio.open_connection(host, port)
    print("Handshake realizado con éxito!")
    while True:
        comando = input('Ingrese los comandos a ejecutar:')
        (opt, arg) = getopt.getopt(sys.argv[1:], 'l', [])
        for (op, ar) in opt:
            if (op == '-l'):
                fecha = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
                archivo_log(comando, fecha)
        escritor.write(comando.encode('ascii'))
        await escritor.drain()
        salida = await lector.read(200)
        salida.decode('ascii')
        print(salida)

asyncio.run(main())