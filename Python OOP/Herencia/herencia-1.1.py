# Ejercicio 1 — Fácil
# Crea una clase Vehiculo con atributo marca y método arrancar().
# Luego crea una clase Carro que herede de Vehiculo y tenga su propio método bocina().

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arranca(self):
        print("Esta arrancando el vehiculo")

class Carro(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def bocina(self):
        print("estoy tocando la bocina")

coche = Carro("Toyota", "supra")
coche.arranca()
coche.bocina()
