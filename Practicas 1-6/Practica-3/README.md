## 🧩 Práctica 3: Disparos
**Descripcion**

En esta practica se nos pidio que las siguientes cosas:
- Cambia la velocidad del disparo.
Tambien aumente la velocidad de las balas usando una variable (velocidad_balas = 10).

- Dispara en diferentes direcciones.
En esta practica use el modulo pygame para hacer que un jugador (un cuadrado verde) pudiera disparar.
Cuando se dispara, el codigo añade 4 balas (rectangulos rojos pequeños) a una lista. 
Luego, un bucle for hace que todas las balas en la lista se muevan hacia la derecha (bala.x += 10).

- Agrega sonido con pygame.mixer.Sound.
Cargar un archivo de sonido (disparo.ogg) usando pygame.mixer.Sound y a revisar si el archivo existía. 
El sonido se reproduce con .play() cada vez que se presiona la barra del espacio.

Trabajo hecho en Python 3.10.11