#!/usr/bin/python3
import socket, subprocess, asyncio


async def servidor(lector, escritor):
    direccion = escritor.get_extra_info('peername')
    print("Got a connection from %s" % str(direccion))
    datos = await lector.read(200)
    datos = datos.decode('ascii')
    datos = subprocess.Popen([datos], shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
    stdout, stderr = datos.communicate()
    if datos.returncode == 0:
        envio = ("OK     "+stdout)
    else:
        envio = ("ERROR   "+stderr)
    escritor.write(envio.encode('ascii'))
    await escritor.drain()



async def main():
    host = socket.gethostname()
    port = 6000
    server = await asyncio.start_server(
        servidor, host, port)
    direccion = server.sockets[0].getsockname()
    async with server:
        print("Esperando conexiones remotas (accept)")
        await server.serve_forever()


asyncio.run(main())