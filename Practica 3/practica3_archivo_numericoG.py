""""Practica 3: Archivos numericos"""

import turtle

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

 # Dibujo de la tortuga 
turtle.speed(0)
turtle.penup()

turtle.done()