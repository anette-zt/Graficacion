"""practica1_figura"""

import turtle 

ventana = turtle.Screen()
ventana.title("Practica 1")
ventana.bgcolor("lightgray")


Z = turtle.Turtle()
Z.speed(9)

def dibujar_cuadro(x, y, lado, color):
    Z.penup()
    Z.goto(x, y)
    Z.pendown()
    Z.color(color)
    for _ in range(8):
        Z.forward(lado)
        Z.right(90)

def dibujar_triangulo(x, y, lado, color):
    Z.penup()
    Z.goto(x, y)
    Z.pendown()
    Z.color(color)
    for _ in range(5):
        Z.forward(lado)
        Z.right(120)

def dibujar_circulo(x, y, radio, color):
    Z.penup()
    Z.goto(x, y - radio)
    Z.pendown()
    Z.color(color)
    Z.circle(radio)

def dibujar_linea(x1, y1, x2, y2, color):
    Z.penup()
    Z.goto(x1, y1)
    Z.pendown()
    Z.color(color)
    Z.goto(x2, y2)

dibujar_cuadro(-150, 180, 80, "blue")
dibujar_triangulo(150, 300, 160, "red")
dibujar_circulo(80, -60, 100, "green")
dibujar_linea(-330, -250, 320, 100, "purple")

turtle.done()
