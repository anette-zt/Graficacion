"""practica1_figura"""

import turtle 

"""Titulo y color de la ventana """
ventana = turtle.Screen()
ventana.title("Practica 1")
ventana.bgcolor("black")

""""Creacion de Maestro Oogway 🐢 """
Z = turtle.Turtle()
Z.speed(3)  

"""Codigo de yn cuadrado"""
def dibujar_cuadro(x, y, lado, color):
    Z.penup()
    Z.goto(x, y)
    Z.pendown()
    Z.color(color)
    for _ in range(4):
        Z.forward(lado)
        Z.right(90)

"""Codigo de una piramide """
def dibujar_triangulo(x, y, lado, color):
    Z.penup()
    Z.goto(x, y)
    Z.pendown()
    Z.color(color)
    for _ in range(3):
        Z.forward(lado)
        Z.right(120)

"""Codigo del dibujo de un circulo y su radio"""
def dibujar_circulo(x, y, radio, color):
    Z.penup()
    Z.goto(x, y - radio)
    Z.pendown()
    Z.color(color)
    Z.circle(radio)

"""Codigo para dibujar una linea recta de punto (a) a punto (b)"""
def dibujar_linea(x1, y1, x2, y2, color):
    Z.penup()
    Z.goto(x1, y1)
    Z.pendown()
    Z.color(color)
    Z.goto(x2, y2)

"""Coordenadas iniciales y finales de las figuras. Tambien tamaño y sus colores"""
dibujar_cuadro(-150, 180, 80, "blue")
dibujar_triangulo(150, 300, 160, "red")
dibujar_circulo(80, -60, 100, "green")
dibujar_linea(-330, -250, 320, 100, "purple")

turtle.done()
