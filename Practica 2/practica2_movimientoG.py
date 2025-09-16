"""Practica2_movimientoG.py"""

import turtle

"""Ventana de dibujo"""
ventana = turtle.Screen()
ventana.title("Practica 2 - Movimiento G")
ventana.bgcolor("lightblue")

"""Creacion de figura"""
figura = turtle.Turtle()
figura.shape("circle")
figura.color("Green")
figura.penup()
figura.speed(0)

"""Distancia de que recorre el circulo"""
distancia = 22

"""Funciones de movimiento"""
def mover_derecha():
    x, y = figura.position()
    figura.goto(x + distancia, y)

def mover_izquierda():
    x, y = figura.position()
    figura.goto(x - distancia, y)

def mover_abajo():
    x, y = figura.position()
    figura.goto(x, y - distancia)

def mover_arriba():
    x, y = figura.position()
    figura.goto(x, y + distancia)

"""Definicion de controles"""
ventana.listen()
ventana.onkey(mover_derecha, "Right")
ventana.onkey(mover_izquierda, "Left")
ventana.onkey(mover_abajo, "Down")
ventana.onkey(mover_arriba, "Up")

"""Mantener ventana abierta"""
ventana.mainloop()