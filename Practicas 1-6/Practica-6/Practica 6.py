import pygame
import sys

# Inicializar Pygame
pygame.init()

# --- Configuración de la Pantalla ---
ANCHO = 640
ALTO = 480
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Practica: Animacion Direccional")

# --- Constantes del Sprite ---
FRAME_ANCHO = 64   # Ancho de cada frame en pixeles
FRAME_ALTO = 64    # Alto de cada frame en pixeles
FILAS = 6      # 0 Arriba 1 Izquierda 2 Abajo 3 Derecha
COLUMNAS = 6    # Fotogramas por animacion

# --- Cargar Sprite Sheet ---
nombre_archivo = "personaje_direcciones.png"

try:
    sprite_sheet = pygame.image.load(nombre_archivo).convert_alpha()
    print(f"Imagen cargada correctamente")

except FileNotFoundError:
    print(f"Generando sprite sheet temporal")
    # Crear una superficie vacía de 4 columnas x 4 filas
    sprite_sheet = pygame.Surface((FRAME_ANCHO * COLUMNAS, FRAME_ALTO * FILAS))
    sprite_sheet.fill((255, 0, 255)) # Color de fondo magenta 
    
    # Dibujar cuadros de colores 
    colores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)] # Rojo Verde Azul Amarillo
    for f in range(FILAS):
        for c in range(COLUMNAS):
            rect = pygame.Rect(c * FRAME_ANCHO, f * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
            pygame.draw.rect(sprite_sheet, colores[f], rect)
            # Dibujar un pequeño circulo para ver el movimiento
            pygame.draw.circle(sprite_sheet, (0,0,0), (rect.centerx + (c*2), rect.centery), 5)

# --- Funcion para recortar cuadros ---
def obtener_frames(fila):
    """
    Recorta una fila horizontal completa del sprite sheet
    Devuelve una lista de superficies o imágenes pequeñas
    """
    frames = []
    for i in range(COLUMNAS):
        # Definimos el rectangulo donde X varia y Y es constante por fila
        rect = pygame.Rect(i * FRAME_ANCHO, fila * FRAME_ALTO, FRAME_ANCHO, FRAME_ALTO)
        frame = sprite_sheet.subsurface(rect)
        frames.append(frame)
    return frames

# --- Diccionario de Animaciones ---
# Mapeamos los nombres a las filas correspondientes de la imagen
animaciones = {
    "arriba":    obtener_frames(0), # Fila 0
    "izquierda": obtener_frames(1), # Fila 1
    "abajo":     obtener_frames(2), # Fila 2
    "derecha":   obtener_frames(3)  # Fila 3
}

# --- Variables del Jugador ---
x = ANCHO // 2
y = ALTO // 2
velocidad = 4
direccion = "abajo" # Direccion inicial
frame_index = 0     # Que fotograma mostrar

# Variables de tiempo para controlar la velocidad de animación
ultimo_tiempo = pygame.time.get_ticks()
tiempo_animacion = 150  # Milisegundos entre cada cambio de frame
reloj = pygame.time.Clock()

# --- Bucle Principal ---
ejecutando = True
while ejecutando:
    # 1 Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # 2 Leer teclado y mover
    teclas = pygame.key.get_pressed()
    moviendo = False

    # Usamos if y elif para evitar movimiento diagonal simple
    if teclas[pygame.K_UP]:
        y -= velocidad
        direccion = "arriba"
        moviendo = True
    elif teclas[pygame.K_DOWN]:
        y += velocidad
        direccion = "abajo"
        moviendo = True
    elif teclas[pygame.K_LEFT]:
        x -= velocidad
        direccion = "izquierda"
        moviendo = True
    elif teclas[pygame.K_RIGHT]:
        x += velocidad
        direccion = "derecha"
        moviendo = True
    
    # Limites de pantalla para que no se salga
    if x < 0:
        x = 0
    if x > ANCHO - FRAME_ANCHO:
        x = ANCHO - FRAME_ANCHO
    if y < 0:
        y = 0
    if y > ALTO - FRAME_ALTO:
        y = ALTO - FRAME_ALTO

    # 3 Logica de Animacion
    ahora = pygame.time.get_ticks()
    
    if moviendo:
        # Si paso suficiente tiempo cambiamos al siguiente frame
        if ahora - ultimo_tiempo > tiempo_animacion:
            frame_index = (frame_index + 1) % len(animaciones[direccion])
            ultimo_tiempo = ahora
    else:
        # Si esta quieto mostramos el frame 0
        frame_index = 0 

    # 4 Dibujar
    VENTANA.fill((90, 150, 255)) # Fondo azul cielo
    
    # Dibujamos el frame actual basado en la dirección y el índice
    imagen_actual = animaciones[direccion][frame_index]
    VENTANA.blit(imagen_actual, (x, y))

    pygame.display.flip()
    reloj.tick(60) # Limitar a 60 FPS

pygame.quit()
sys.exit()