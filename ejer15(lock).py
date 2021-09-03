#!/usr/bin/python3

import time, threading, os, sys, getopt

(opt, arg) = getopt.getopt(sys.argv[1:], 'n:f:r:')
for (op, ar) in opt:
    if op == '-n':
        hilos = int(ar)
    if op == '-f':
        nom_archivo = str(ar)
    if op == '-r':
        iteraciones = int(ar)


if os.path.exists(nom_archivo):
    os.remove(nom_archivo)

letra = 0

def escritor(nom_archivo, iteraciones, letra, lock):
    lock.acquire()
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    archivo = open(nom_archivo, 'a')
    for j in range(iteraciones):
        archivo.writelines(letras[letra])
        time.sleep(1)
    archivo.close()
    lock.release()


if __name__=="__main__":
    lock = threading.Lock()


for i in range(hilos):
    threading.Thread(target=escritor, args=(nom_archivo, iteraciones, letra, lock)).start()
    letra = letra + 1




