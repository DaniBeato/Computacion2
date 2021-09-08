#!/usr/bin/python3

import getopt
import sys
import shutil

(opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:')

for (op, ar) in opt:
    if (op in ['-i']):
        origen = ar
    if (op in ['-o']):
        destino = ar




nuevo_archivo = shutil.copy2(origen, destino)
print('Se ha copiado el archivo ', origen, 'al nuevo archivo', destino)