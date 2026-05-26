# Ejercicio 2 — Medio
# Crea tres clases:

# Programador — método programar()
# Diseñador — método diseñar()
# Persona — atributos nombre y edad

# Luego crea FullStack que herede de las tres 💪

class Programador:
    def programar(self):
        print("estoy programando")
    
class Diseñador:
    def diseñar(self):
        print("estoy diseñando")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Fullstack(Programador, Diseñador, Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)


persona = Fullstack("Jose", 17)
persona.programar()
persona.diseñar()
