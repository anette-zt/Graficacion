""""Practica 3: Archivos numericos"""

import os
import turtle

print("Carpeta actual:", os.getcwd())

 # Dibujo de la tortuga 

turtle.speed(20)
turtle.penup()

# Asignacion de numeros a colores
colores = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow",
    4: "purple",
    5: "orange",
    6: "pink",
    7: "brown",
    8: "gray",
    9: "black"
}

def cargar_matriz():
    # Funcion con la que cargamos la matriz del archivo txt
    filename = 'matriz.txt'
    matriz = []
    for line in open(filename):
        seq = line.split() 
        fila = [int(num) for num in seq] 
        matriz.append(fila)
    return matriz

matriz = cargar_matriz()

pixel = 6
inicio_x = -len(matriz[0]) * pixel // 2
inicio_y = len(matriz) * pixel // 2

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        numero = matriz[i][j]
        color = colores.get(numero, "gray")
        turtle.goto(inicio_x + j * pixel, inicio_y - i * pixel)
        turtle.dot(pixel, color)

turtle.done()
