# Clase Estudiante con atributos nombre, edad, grado
# Método estudiar() que imprima "el estudiante (nombre) está estudiando"
# El usuario escribe los atributos
# Si el usuario escribe "estudiar" se ejecuta el método

class Estudiante:
    def __init__(self, nombre, edad, grado):
        
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando.")


nombre = input("Ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
grado = input("En que grado esta: ")
accion = input("¿Quieres estudiar? (Si/No)").lower()

estudiante1 = Estudiante(nombre, edad, grado)

print(f"""
    Datos del Estudiante: \n\n
    Nombre: {estudiante1.nombre}\n      
    Edad: {estudiante1.edad}\n
    Grado: {estudiante1.grado}\n
      """)


if accion == "si":
    estudiante1.estudiar()   

    