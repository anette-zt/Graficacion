## 🧩 Práctica 4: Colisiones
**Descripcion**

- Haz que los enemigos reaparezcan en posiciones aleatorias.
Use pygame.Rect.colliderect() para detectar cuando una bala choca con un enemigo.
Ya que cuando choquen la bala y el enemigo se eliminan de sus listas. 
Se uso el modulo random para que un nuevo enemigo aparezca en una posicion aleatoria de la pantalla.

- Agrega un contador de puntos.
- Muestra el puntaje en pantalla.
Se añadio un contador de puntaje que aumenta con cada enemigo eliminado, y use pygame.font para dibujar y mostrar el puntaje en la esquina de la pantalla. 

- A lo cual yo por pura curiosidad le agregue sonidos al disparar y que el personaje se movienra arriba y abajo que tome de la practica 3
Use pygame.key.get_pressed() para añadir movimiento completo al jugador con las flechas.
Y use pygame.mixer.soun con un archivo ogg ya que es el que se recomienda ya que es mas sencillo de usar.

Todo se trabajo con Python 3.10.11