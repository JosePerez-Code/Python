# Ejercicio 1
# Crea una clase Persona con nombre, edad y ciudad. Crea 3 personas diferentes e imprime todos sus datos.

class Persona:
    def __init__(self, nombre, edad, ciudad):
        
        self.todos = nombre, edad, ciudad

persona1 = Persona("Juan",17 ,"New york")
persona2 = Persona("Josh", 19, "utah")
persona3 = Persona("Josue", 18, "California")

print(persona1.todos)