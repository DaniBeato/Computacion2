from PIL import Image
import numpy as np

archivo = input('Ingrese la ruta de la imagen ppm que desea rotar: ')
img = Image.open(archivo)
matriz_roja = np.asarray(img)
matriz_verde = np.asarray(img)
matriz_azul = np.asarray(img)
matriz_roja_aux = np.asarray(img)
matriz_verde_aux = np.asarray(img)
matriz_azul_aux = np.asarray(img)
matriz_final = np.asarray(img)
dimension = matriz_roja.shape

for x in range(dimension[0]):
    for y in range(dimension[1]):
        matriz_roja[x,y] = (matriz_roja[x,y][0],0,0)

for x in range(dimension[0]):
    for y in range(dimension[1]):
        matriz_roja_aux[x,y] = (matriz_roja_aux[x,y][0],0,0)

j = -1
for x in range(dimension[0]):
    i = dimension[0]-1
    j += 1
    for y in range(dimension[1]):
        if i >= 0:
            matriz_roja[x,y] = (matriz_roja_aux[i,j])
            i -= 1
        else:
            matriz_roja[x, y] = (0,0,0)




for x in range(dimension[0]):
    for y in range(dimension[1]):
        matriz_verde[x,y] = (0,matriz_verde[x,y][1],0)

for x in range(dimension[0]):
    for y in range(dimension[1]):
        matriz_verde_aux[x,y] = (0,matriz_verde_aux[x,y][1],0)

j = -1
for x in range(dimension[0]):
    i = dimension[0]-1
    j += 1
    for y in range(dimension[1]):
        if i >= 0:
            matriz_verde[x, y] = (matriz_verde_aux[i, j])
            i -= 1
        else:
            matriz_verde[x, y] = (0, 0, 0)



for x in range(dimension[0]):
    for y in range(dimension[1]):
        matriz_azul[x,y] = (0,0,matriz_azul[x,y][2])

for x in range(dimension[0]):
    for y in range(dimension[1]):
        matriz_azul_aux[x,y] = (0,0,matriz_azul_aux[x,y][2])

j = -1
for x in range(dimension[0]):
    i = dimension[0]-1
    j += 1
    for y in range(dimension[1]):
        if i >= 0:
            matriz_azul[x, y] = (matriz_azul_aux[i, j])
            i -= 1
        else:
            matriz_azul[x, y] = (0, 0, 0)



for x in range(dimension[0]):
    for y in range(dimension[1]):
            matriz_final[x,y] = (matriz_roja[x,y][0],matriz_verde[x,y][1],matriz_azul[x,y][2])

img_original = Image.fromarray(np.uint8(matriz_final))
Image.Image.show(img_original)

