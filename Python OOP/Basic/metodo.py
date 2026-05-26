# Crea una clase Perro con:

# nombre y raza como atributos
# Un método ladrar() que imprima "[nombre] dice: Guau!"
# Un método presentarse() que imprima "Hola soy [nombre] y soy un [raza]"

# Crea 2 perros y usa los dos métodos 💪

class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: Guau")
    
    def presentarse(self):
        print(f"Hola soy {self.nombre} y soy un {self.raza}")

perro1 = Perro("Firulais", "Pitbull")

perro1.ladrar()
perro1.presentarse()
