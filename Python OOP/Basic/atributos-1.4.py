# Ejercicio 3
# Crea una clase Videojuego con nombre, genero y año. Crea 3 videojuegos e imprime su nombre y año.

class VideoJuego:
    def __init__(self, nombre, genero, año):
        self.nombre = nombre
        self.genero = genero
        self.año = año

juego1 = VideoJuego("Resident Evil 1", "Suvival Horror", 1996)
juego2 = VideoJuego("Resident Evil 2", "Survival Horror", 1998)

print(f"{juego1.nombre} - {juego1.año}")
print(f"{juego2.nombre} - {juego2.año}")