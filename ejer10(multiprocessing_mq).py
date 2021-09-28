#!/usr/bin/python3
import multiprocessing, os, time

def funcion(n, pila):
   print('Proceso:', n + 1,', ', 'PID: ', os.getpid())
   time.sleep(10)
   pila.put(os.getpid())


if __name__ == '__main__':
   pila = multiprocessing.Queue()
   for n in range(10):
      hijo = multiprocessing.Process(target = funcion, args = (n, pila,))
      hijo.start()
      hijo.join()
   print('Contenido de la pila: ')
   for i in range(10):
      print(pila.get())