#!/usr/bin/python3

import os, time

proceso = os.fork()
if proceso == 0:
    for hijo in range(5):
        print('Soy el hijo: ', os.getpid())
    print(os.getpid(),' terminado')
else:
    for padre in range(2):
        print('Soy el padre: ', os.getpid())
    time.sleep(2)
    print('Mi propio hijo', proceso,'terminó')