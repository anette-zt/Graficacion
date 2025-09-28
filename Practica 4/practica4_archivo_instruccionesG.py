""" practica4_archivo_instruccionesG"""

import turtle

# Configuracion de la ventana que sera negra como mi alma 
ventana = turtle.Screen()
ventana.setup(600, 600)
ventana.bgcolor("black")
ventana.title("Practica 4 - Dibujante")

# Nace la tortuga
z = turtle.Turtle()
z.speed(1)

# Lee el txt donde vienen las isntrucciones
archivo = open("dibujante.txt", "r")
lineas = archivo.readlines()
archivo.close()

# Procesador de cada linea del archivo
for linea in lineas:
    partes = linea.split()
    if len(partes) == 0:
        continue

# Instrucciones de dibujo para cuadro, triangulo, circulo y linea
# Cada instrccion se le puso el lado donde empueza y termina, jubto con sus colores
    instruccion = partes[0]

    if instruccion == "cuadro":
        x = int(partes[1])
        y = int(partes[2])
        lado = int(partes[3])
        color = partes[4]
        z.penup()
        z.goto(x, y)
        z.pendown()
        z.fillcolor(color)
        z.begin_fill()
        for i in range(4):
            z.forward(lado)
            z.right(90)
        z.end_fill()

    elif instruccion == "triangulo":
        x = int(partes[1])
        y = int(partes[2])
        lado = int(partes[3])
        color = partes[4]
        z.penup()
        z.goto(x, y)
        z.pendown()
        z.fillcolor(color)
        z.begin_fill()
        for i in range(3):
            z.forward(lado)
            z.right(120)
        z.end_fill()

    elif instruccion == "circulo":
        x = int(partes[1])
        y = int(partes[2])
        radio = int(partes[3])
        color = partes[4]
        z.penup()
        z.goto(x, y - radio)
        z.pendown()
        z.fillcolor(color)
        z.begin_fill()
        z.circle(radio)
        z.end_fill()

    elif instruccion == "linea":
        x1 = int(partes[1])
        y1 = int(partes[2])
        x2 = int(partes[3])
        y2 = int(partes[4])
        color = partes[5]
        z.penup()
        z.goto(x1, y1)
        z.pendown()
        z.color(color)
        z.goto(x2, y2)

# La tortuga muere
turtle.done()