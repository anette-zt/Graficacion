"""practica1_figura"""

import turtle 

"""Configuracion de la ventana"""
ventana = turtle.Screen()
ventana.title("Dibujo de z")
ventana.bgcolor("black")

""""Creacion de la tortuga"""
z = turtle.Turtle()
z.speed(2)  

"""Funciones para dibujar un cuadro"""
def dibujar_cuadro(x, y, lado, color):
    z.penup()
    z.goto(x, y)
    z.pendown()
    z.color(color)
    for _ in range(4):
        z.forward(lado)
        z.right(90)

"""Funcion para dibujar un triangulo"""
def dibujar_triangulo(x, y, lado, color):
    z.penup()
    z.goto(x, y)
    z.pendown()
    z.color(color)
    for _ in range(3):
        z.forward(lado)
        z.right(120)

"""Funcion para dibujar un circulo"""
def dibujar_circulo(x, y, radio, color):
    z.penup()
    z.goto(x, y - radio)
    z.pendown()
    z.color(color)
    z.circle(radio)

"""Funcion para dibujar una linea"""
def dibujar_linea(x1, y1, x2, y2, color):
    z.penup()
    z.goto(x1, y1)
    z.pendown()
    z.color(color)
    z.goto(x2, y2)

"""Posicionamiento y color de cada figura"""
dibujar_cuadro(-150, 180, 80, "blue")
dibujar_triangulo(150, 300, 160, "orange")
dibujar_circulo(80, -60, 100, "white")
dibujar_linea(-330, -250, 320, 100, "crimson")

turtle.done()
