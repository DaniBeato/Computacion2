#!/usr/bin/python3

import getopt
import sys
import os


(opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')


for (op, ar) in opt:
    if (op in ['-c']):
        comando = ar
    if (op in ['-f']):
        archivo = os.path.isfile(ar)
        nombre_archivo = ar
        if archivo == False:
            os.system('touch '+ar)
    if (op in ['-l']):
        log = os.path.isfile(ar)
        nombre_log = ar
        if log == False:
            os.system('touch '+ar)


os.system(comando+' >> '+nombre_archivo)
os.system(comando+' 2>> '+nombre_log)



'''Esta es la resolución con Popen, pero no devuelve el error stándar en el archivo deseado. Por eso el ejercicio 
ha sido resuelto con system, que sí devuelve tanto la salida stándard, como el error stándard, en los archivos deseados.'''

#import subprocess


#archivo_salida = open(nombre_archivo, 'w')
#archivo_error = open(nombre_log, 'w')
#subprocess.Popen([comando], stdout=archivo_salida)
#subprocess.Popen([comando], stderr=archivo_error)



