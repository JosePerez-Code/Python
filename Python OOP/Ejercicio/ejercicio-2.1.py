# Ejercicio 4
# Crea una clase Estudiante con nombre y notas (lista vacía). Con métodos:

# agregar_nota(nota) — agrega una nota a la lista
# promedio() — imprime el promedio de todas las notas
# aprobo() — imprime si aprobó o reprobó (promedio >= 60)

class Estudiante:

    def __init__(self, nombre):
        
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        
        self.notas.append(nota)
        print(f"Agregaste: {nota}")

    def promedios(self):

        promedio = sum(self.notas) / len(self.notas)
        print(round(promedio))
    
    def aprobo(self):

        promedio = sum(self.notas) / len(self.notas)
        
        if promedio >= 60:
            print("Aprobo")

        else:
            print("reprobo")
            
def estudiante1(nombre):
    resultado = Estudiante(nombre)
    resultado.agregar_nota(70)
    resultado.agregar_nota(50)
    resultado.agregar_nota(60)
    resultado.promedios()
    resultado.aprobo()

estudiante1("juan")
