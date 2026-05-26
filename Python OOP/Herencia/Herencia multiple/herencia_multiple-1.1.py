# Ejercicio 1 — Fácil
# Crea dos clases:

# Volador — método volar()
# Nadador — método nadar()

# Luego crea Pato que herede de las dos y tenga su propio método graznar()

class Volador:
    def volar(self):
        print("estoy volando")

class Nadador:
    def nadar(self):
        print("estoy nadando")

class Pato(Volador, Nadador):
    def __init__(self):
        super().__init__()

    def graznar(self):
        print("estoy graznando")

pato = Pato()
pato.graznar()
pato.nadar()
pato.volar()