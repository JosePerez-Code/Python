# Crea una clase Persona con nombre y edad. Luego crea:

# Estudiante — hereda de Persona, agrega grado y método estudiar()
# Profesor — hereda de Persona, agrega materia y método enseñar()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def estudiar(self):
        print("El estudiante esta estudiando")

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def enseñar(self):
        print("El profesor esta enseñando")

profe = Profesor("Juan", 30, "Matematicas")
profe.enseñar()

alumno = Estudiante("jose", 17, "90")
alumno.estudiar()