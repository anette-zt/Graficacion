import pygame
import sys  # Importamos sys para cerrar el programa correctamente

# Inicializar Pygame
pygame.init()

# --- Configuracion Inicial ---
ANCHO = 1200
ALTO = 900
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Practica 5 - Salto y Desplazamiento")
clock = pygame.time.Clock()

# --- Carga de Recursos ---
try:
    fondo = pygame.image.load("fondo.png").convert()
    sprite = pygame.image.load("personaje.png").convert_alpha()
    NUEVO_ANCHO_PJ, NUEVO_ALTO_PJ = 60, 90 # Definimos el nuevo tamano del personaje

except pygame.error as e:
    print(f"Error: No se encuentran los archivos. {e}")
    print("Asegurate de que 'fondo.png' y 'personaje.png' esten en la misma carpeta que este codigo.")
    pygame.quit()
    sys.exit()

# --- Variables del Juego ---

# Personaje
x = 100
# Define la altura del suelo. Ajusta este valor si tu personaje flota o se hunde.
EN_SUELO = 300 
y = EN_SUELO 

# Movimiento Vertical (Salto)
velocidad_y = 0
gravedad = 1
esta_saltando = False

# Fondo (Scroll infinito)
velocidad_mundo = 5
fondo_x = 0

running = True
juego_activo = True

# --- Bucle Principal del Juego ---
while running:
    # 60 FPS para que vaya mas fluido (30 puede verse lento)
    clock.tick(60) 
    
    # 1. Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if juego_activo:
        # --- 2. Entrada del Usuario (Teclado) ---
        keys = pygame.key.get_pressed()
        
        # Salto
        if keys[pygame.K_SPACE] and not esta_saltando:
            esta_saltando = True
            velocidad_y = -15  # Fuerza del salto
        
        # Movimiento del Fondo (Simula caminar)
        # Nota: Si pulsas DERECHA, el fondo se mueve a la IZQUIERDA
        if keys[pygame.K_RIGHT]:
            fondo_x -= velocidad_mundo
        if keys[pygame.K_LEFT]:
            fondo_x += velocidad_mundo

        # --- 3. Logica de Fisica (Gravedad) ---
        y += velocidad_y
        velocidad_y += gravedad
        
        # Colision con el suelo
        if y >= EN_SUELO:
            y = EN_SUELO
            velocidad_y = 0
            esta_saltando = False

        # --- 4. Logica del Fondo Infinito ---
        ancho_fondo = fondo.get_width()
        
        # Si el fondo se ha movido completamente a la izquierda
        if fondo_x <= -ancho_fondo:
            fondo_x = 0
        # Si el fondo se mueve mucho a la derecha
        elif fondo_x > 0:
            fondo_x = -ancho_fondo + ANCHO

        # --- 5. Dibujo en Pantalla ---
        
        # Dibujamos el fondo dos veces para crear el efecto de bucle
        pantalla.blit(fondo, (fondo_x, 0))
        pantalla.blit(fondo, (fondo_x + ancho_fondo, 0))
        
        # Dibujamos al personaje
        pantalla.blit(sprite, (x, y))
        
        # Actualizamos la ventana
        pygame.display.update()

# Salir 
pygame.quit()
sys.exit()