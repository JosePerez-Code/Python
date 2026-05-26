# Crea una clase Animal con atributo nombre y método comer(). Luego crea dos clases:

# Perro — hereda de Animal y tiene método ladrar()
# Gato — hereda de Animal y tiene método maullar()

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        print("Estoy comiendo")

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def ladrar(self):
        print("estoy ladrando")

class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def maullar(self):
        print("Estoy maullando")

perro = Perro("Firulais")
perro.comer()
perro.ladrar()

gato = Gato("tom")
gato.comer()
gato.maullar()