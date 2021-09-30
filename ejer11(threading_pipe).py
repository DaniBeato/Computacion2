#!/usr/bin/python3

import threading, os, time, sys


def hijo1(w):
    w = os.fdopen(w, 'w')
    sys.stdin = open(0)
    while True:
        msg = input('Ingrese algo, (pid): '+ str(os.getpid()) + ' (thread_id): ' + str(threading.get_ident()) + ' ') + '\n'
        w.write(msg)
        w.flush()
        time.sleep(0.1)



def hijo2(r):
    r = os.fdopen(r, 'r')
    while True:
        msg = ('Leyendo (pid): ' + str(os.getpid())  + ' (thread_id): ' + str(threading.get_ident()) + ' ' + r.readline())
        print(msg)

if __name__ == '__main__':
    r, w = os.pipe()
    child1 = threading.Thread(target = hijo1, args = (w,), daemon=True)
    child2 = threading.Thread(target = hijo2, args = (r,), daemon=True)
    child1.start()
    child2.start()
    child1.join()
    child2.join()





