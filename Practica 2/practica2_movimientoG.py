"""Practica2_movimientoG.py"""

import turtle

"""Ventana de dibujo"""
ventana = turtle.Screen()
ventana.title("Practica 2 - Movimiento G")
ventana.bgcolor("lightblue")

"""Creacion de figura"""
figura = turtle.Turtle()
figura.shape("turtle")
figura.color("Green")
figura.shapesize(2, 2, 2)  
figura.penup()
figura.speed(0)

"""Distancia de que recorre la tortuga"""
distancia = 22

"""Funciones de movimiento"""
def mover_derecha():
    figura.setheading(0)
    x, y = figura.position()
    figura.goto(x + distancia, y)

def mover_izquierda():
    figura.setheading(180)
    x, y = figura.position()
    figura.goto(x - distancia, y)

def mover_abajo():
    figura.setheading(270)
    x, y = figura.position()
    figura.goto(x, y - distancia)

def mover_arriba():
    figura.setheading(90)
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