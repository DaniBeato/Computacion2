#!/usr/bin/python3

import multiprocessing, os


def hijo1(emisor):
    msg = input('Ingrese algo...')
    emisor.send(msg)


def hijo2(receptor):
        msg = receptor.recv()
        print('Leyendo (pid: ', os.getpid(), '):', msg)


if __name__ == '__main__':
        emisor, receptor = multiprocessing.Pipe()
        child1 = multiprocessing.Process(target = hijo1, args=(emisor,))
        child2 = multiprocessing.Process(target = hijo2, args=(receptor,))
        while True:
            child1.run()
            child2.run()





