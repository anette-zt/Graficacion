import turtle

# Configuración de la ventana
turtle.setup(width=900, height=900)  # ventana de 900x900
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(False)  # desactiva animación (dibuja rápido)
turtle.penup()

# Asignación de números a colores
colores = {
    0: "white",   # 0 = blanco
    1: "black",   # 1 = negro
}

def cargar_matriz():
    filename = '600.txt'
    matriz = []
    with open(filename) as f:
        for line in f:
            if line.strip():  # ignorar líneas vacías
                fila = [int(num) for num in line.split()]  # separa por espacios
                matriz.append(fila)
    return matriz

matriz = cargar_matriz()

# --- Ajuste automático del tamaño del pixel ---
ancho = len(matriz[0])
alto = len(matriz)
pixel = min(800 // ancho, 800 // alto)  # escala para caber en 800x800

# Coordenadas de inicio (centrado)
inicio_x = -ancho * pixel // 2
inicio_y = alto * pixel // 2

# Función para dibujar un cuadrado
def dibujar_pixel(x, y, color):
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(pixel)
        turtle.right(90)
    turtle.end_fill()

# Dibujar la matriz
for i in range(alto):
    for j in range(ancho):
        numero = matriz[i][j]
        color = colores[numero]  # siempre será 0 o 1
        x = inicio_x + j * pixel
        y = inicio_y - i * pixel
        dibujar_pixel(x, y, color)

turtle.update()
turtle.Screen().exitonclick()

