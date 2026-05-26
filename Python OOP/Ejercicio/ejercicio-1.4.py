# Crea una clase Playlist con nombre y una lista de canciones. Con dos métodos:

# agregar_cancion(cancion) — agrega una canción a la lista
# mostrar_canciones() — imprime todas las canciones

class Playlist:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista = []

    def agregar_cancion(self, cancion):
        self.lista.append(cancion)
        print(f"Agregaste: {cancion}")

    def mostrar_canciones(self):
        for cancion in self.lista:
            print(cancion)

play = Playlist("Mi playlist")
play.agregar_cancion("Cancion 1")
play.agregar_cancion("Cancion 2")
play.mostrar_canciones()
    


    
