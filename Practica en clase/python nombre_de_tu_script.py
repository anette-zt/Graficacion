import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo de texto
with open("bts_binary_600x600.txt", "r") as f:
    data = f.read()

# Convertir a lista de enteros
binary_values = list(map(int, data.split()))

# Ajustar a un arreglo 2D de 600x600
image_array = np.array(binary_values).reshape((600, 600))

# Mostrar la imagen en blanco y negro
plt.imshow(image_array, cmap="gray")
plt.axis("off")
plt.show()