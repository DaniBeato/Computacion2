#!/usr/bin/python3

import getopt
import sys
import os

(opt, arg) = getopt.getopt(sys.argv[1:], 'n:')


for (op, ar) in opt:
    procesos = ar
    for i in range(int(procesos)):
        proceso = os.fork()
        if proceso == 0:
          print('Soy el proceso: ', os.getpid(), 'mi padre es: ', os.getppid())
          sys.exit()
