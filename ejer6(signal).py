#!/usr/bin/python3

import signal, os, time


def handler_padre(s, f):
    os.kill(proceso2, signal.SIGUSR1)


def padre():
    for i in range(10):
        signal.signal(signal.SIGUSR1, handler_padre)
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.pause()
        time.sleep(5)


def hijo1():
    for i in range(10):
        print('---------------------------------------------')
        print('Repetición: ', i + 1)
        print('Soy el hijo 1, con PID: ', os.getpid(), 'ping')
        os.kill(os.getppid(), signal.SIGUSR1)
        time.sleep(5)
    os.kill(os.getppid(), signal.SIGTERM)


def hijo2_handler(s, f):
    print('Soy el hijo 2, con PID: ', os.getpid(), 'pong')


def hijo2():
    for i in range(10):
        signal.signal(signal.SIGUSR1, hijo2_handler)
        signal.pause()
        time.sleep(5)


if __name__ == '__main__':
    proceso = os.fork()
    if proceso == 0:
        time.sleep(0.3)
        hijo1()
    else:
        proceso2 = os.fork()
        if proceso2 == 0:
            hijo2()
        else:
            padre()

