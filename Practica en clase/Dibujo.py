"""Script para crear un dibujo en un archivo de texto"""

def leer_archivo():
    filename = 'dibujo.txt'
    for line in open(filename):
        seq = line.split() 
        for w in seq[0]:
            print(f"{w}", end=' ') 

leer_archivo()