import pygame
pygame.init()

pantalla = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Práctica 2 - Saltos")

x, y = 300, 300
vel_y = 0
gravedad = 1
fuerza_salto = -18   # Fuerza de salto aumentada
en_suelo = True
doble_salto = False  # Control para permitir doble salto
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()

    # Saltos
    if teclas[pygame.K_SPACE]:
        # Salto normal
        if en_suelo:
            vel_y = fuerza_salto
            en_suelo = False
            doble_salto = True  # Activa doble salto

        # Doble salto
        elif doble_salto:
            vel_y = fuerza_salto
            doble_salto = False  # Solo permite un salto extra

    y += vel_y
    vel_y += gravedad

    suelo_y = 310
    if y >= 300:
        y = 300
        vel_y = 0
        en_suelo = True

    pantalla.fill((50, 50, 100))
    pygame.draw.rect(pantalla, (0, 255, 0), (0, 380, 600, 20))  # Suelo visible
    pygame.draw.rect(pantalla, (255, 255, 0), (x, y, 40, 40))
    pygame.display.update()

pygame.quit()