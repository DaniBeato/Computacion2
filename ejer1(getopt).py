#!/usr/bin/python3

import getopt
import sys

suma = False
resta = False
multiplicacion = False
division = False

(opt, arg) = getopt.getopt(sys.argv[1:], 'n:o:m:')

for (op, ar) in opt:


    if (op in ['-n']):
        num1 = int(ar)



    if(op in ['-o']):
        if ar == '+':
            suma = True
        if ar == '-':
            resta = True
        if ar == '*':
            multiplicacion = True
        if ar == '/':
            division = True


    if (op in ['-m']):
        num2 = int(ar)


if suma == True:
    resultado = num1 + num2
    print('El resultado de la suma es ', resultado)

if resta == True:
    resultado = num1 - num2
    print('El resultado de la resta es ', resultado)

if multiplicacion == True:
    resultado = num1 * num2
    print('El resultado de la multiplicacion es ', resultado)

if division == True:
    resultado = num1 / num2
    print('El resultado de la división es ', resultado)



