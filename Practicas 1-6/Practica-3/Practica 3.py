import pygame
import sys  # Esto es necesario para cargar el archivo de sonido
pygame.init()
pygame.mixer.init() # Inicia el mezclador de sonido

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 3 - Disparos")

# Cargar sonido de disparo
try:
    sonido_disparo = pygame.mixer.Sound('disparo.ogg')
except pygame.error:
    print("No se pudo cargar el archivo de sonido 'disparo.ogg'")
    sys.exit(1)

x, y = 50, 300 
balas = []
velocidad_balas = 1  # Aquí se define la velocidad de las balas
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Reproducir sonido al disparar
            sonido_disparo.play()
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            balas.append(pygame.Rect(x + 40, y + 15, 10, 5))
            balas.append(pygame.Rect(x + 50, y + 20, 10, 5)) # Bala adicional
            balas.append(pygame.Rect(x + 20, y + 40, 10, 5)) # Bala adicional
            balas.append(pygame.Rect(x + 30, y + 30, 10, 5)) # Bala adicional

    for bala in balas:
        bala.x += velocidad_balas # Usar la variable de velocidad para mover las balas

    balas = [b for b in balas if b.x < 600]

    pantalla.fill((20, 20, 20))
    pygame.draw.rect(pantalla, (0, 255, 0), (x, y, 40, 40))
    for b in balas:
        pygame.draw.rect(pantalla, (255, 0, 0), b)
    pygame.display.update()

pygame.quit()