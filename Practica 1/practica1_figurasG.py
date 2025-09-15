"""practica1_figura"""

import turtle 

"""Lienzos donde el Maestro Oogway 🐢 dibuja sus figuras"""
ventana = turtle.Screen()
ventana.title("Dibujo de Oogway")
ventana.bgcolor("black")

""""El Maestro Oogway 🐢 queriendo dibujar"""
Oogway = turtle.Turtle()
Oogway.speed(2)  

"""Dibujo de un cuadrado, como el patio de entrenamiento"""
def dibujar_cuadro(x, y, lado, color):
    Oogway.penup()
    Oogway.goto(x, y)
    Oogway.pendown()
    Oogway.color(color)
    for _ in range(4):
        Oogway.forward(lado)
        Oogway.right(90)

"""Dinujo de una piramide"""
def dibujar_triangulo(x, y, lado, color):
    Oogway.penup()
    Oogway.goto(x, y)
    Oogway.pendown()
    Oogway.color(color)
    for _ in range(3):
        Oogway.forward(lado)
        Oogway.right(120)

"""Dibujo de la panza de Po 🐼"""
def dibujar_circulo(x, y, radio, color):
    Oogway.penup()
    Oogway.goto(x, y - radio)
    Oogway.pendown()
    Oogway.color(color)
    Oogway.circle(radio)

"""Dibujo de una linea, como la espada del maestro Shifu 🦊"""
def dibujar_linea(x1, y1, x2, y2, color):
    Oogway.penup()
    Oogway.goto(x1, y1)
    Oogway.pendown()
    Oogway.color(color)
    Oogway.goto(x2, y2)

"""Ya se canso de dibujar"""
dibujar_cuadro(-150, 180, 80, "blue")
dibujar_triangulo(150, 300, 160, "orange")
dibujar_circulo(80, -60, 100, "white")
dibujar_linea(-330, -250, 320, 100, "crimson")

turtle.done()
