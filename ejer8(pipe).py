#!/usr/bin/python3

import os, signal, time

def proc_A_handler(s, f):
    re = os.fdopen(r)
    wr = os.close(w)
    print('A (PID = ', os.getpid(), '), leyendo: ')
    for i in range(2):
        print(re.readline())

def proc_A(proceso):
    os.kill(proceso, signal.SIGUSR1)
    signal.signal(signal.SIGUSR2, proc_A_handler)
    signal.pause()


def proc_B_handler(s, f):
    re = os.close(r)
    wr = os.fdopen(w, 'w')
    wr.write('Mensaje 1 (PID = ' + str(os.getpid()) + ')\n')


def proc_B(proceso):
    signal.signal(signal.SIGUSR1, proc_B_handler)
    signal.pause()
    os.kill(proceso, signal.SIGUSR1)


def proc_C_handler(s, f):
    #os.kill(proceso, signal.SIGUSR1)
    re = os.close(r)
    wr = os.fdopen(w, 'w')
    wr.write('Mensaje 2 (PID = ' + str(os.getpid()) + ')\n')


def proc_C(pid_padre):
    signal.signal(signal.SIGUSR1, proc_C_handler)
    signal.pause()
    os.kill(pid_padre, signal.SIGUSR2)


if __name__ == "__main__":
    r, w = os.pipe()
    pid_padre = os.getpid()
    proceso = os.fork()
    if proceso == 0:
        proceso = os.fork()
        if proceso == 0:
            time.sleep(1)
            proc_C(pid_padre)
        else:
            proc_B(proceso)
    else:
        time.sleep(1)
        proc_A(proceso)


