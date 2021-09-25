#!/usr/bin/python3
import getopt
import os
import signal, sys, time


def hijo_handler(s, f):
    print('Soy el PID: ', os.getpid(), ' recibí la señal: ', s, ' de mi padre PID: ', os.getppid())


def hijo():
    signal.signal(signal.SIGUSR2, hijo_handler)
    signal.pause()



if __name__ == '__main__':
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process:'])
    pid_hijos = []
    for (op,ar) in opt:
        repeticiones = ar
    proceso = 1
    for i in range(int(repeticiones)):
         if proceso != 0:
            proceso = os.fork()
            if proceso != 0:
                pid_hijos.append(proceso)
                print('Creando proceso: ', proceso)
            else:
                hijo()
    if proceso != 0:
        for i in range(int(repeticiones)):
            time.sleep(0.1)
            os.kill(pid_hijos[i], signal.SIGUSR2)













