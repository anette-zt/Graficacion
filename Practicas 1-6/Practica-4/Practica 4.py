import pygame
import random # Para que los enemigos salgan de forma random aleatoria
import sys # Para cargar el sonido

pygame.init()
pygame.font.init() 
pygame.mixer.init() # Inicializar el mezclador de sonido


pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 4 - Colisiones y Movimiento")

# Constantes de ancho y alto 
ANCHO, ALTO = pantalla.get_size()

# Contador de puntos 
puntaje = 0

# Cargar sonido de disparo
try:
    sonido_disparo = pygame.mixer.Sound('disparo.ogg')
except pygame.error:
    print("No se pudo cargar el archivo de sonido 'disparo.ogg'.")
    sys.exit(1)

# Fuente que usamos para mostrar el puntaje
try:
    mi_fuente = pygame.font.SysFont('Arial', 30)
except pygame.error:
    mi_fuente = pygame.font.SysFont(None, 36)

jugador = pygame.Rect(50, 300, 40, 40)
balas = []
enemigos = [pygame.Rect(500, 300, 40, 40)]
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(jugador.x + 40, jugador.y + 15, 10, 5))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Reproducir el sonido de disparo
            sonido_disparo.play()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.y > 0: # Se mueve hacia arriba 
        jugador.y -= 5
    if teclas[pygame.K_DOWN] and jugador.y < ALTO - jugador.height: # Se mueve hacia abajo
        jugador.y += 5

    for b in balas:
        b.x += 10
    balas = [b for b in balas if b.x < 600] 

    for b in balas[:]:
        for e in enemigos[:]:
            if b.colliderect(e):
                balas.remove(b)
                enemigos.remove(e)

                puntaje += 10

                # Modulo donde el enemigo vuelve a aparecer en una posicion random
                nuevo_x = random.randint(ANCHO // 2, ANCHO - 40)
                nuevo_y = random.randint(0, ALTO - 40)
                enemigos.append(pygame.Rect(nuevo_x, nuevo_y, 40, 40))
                
                break

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador) 
    for b in balas:
        pygame.draw.rect(pantalla, (255, 255, 0), b) 
    for e in enemigos:
        pygame.draw.rect(pantalla, (255, 0, 0), e) 

    # Cuadro del puntaje
    texto_puntaje = mi_fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto_puntaje, (10, 10))

    pygame.display.update()

pygame.quit()