# Crea una clase Empleado con nombre y sueldo. Luego crea:

# Programador — hereda de Empleado y tiene método programar()
# Diseñador — hereda de Empleado y tiene método diseñar()

# Crea un objeto de cada uno e imprime su nombre, sueldo y usa su método 💪

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

class Programador(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def programar(self):
        print("Estoy programando")

class Diseñador(Empleado):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre, sueldo)

    def Diseñar(self):
        print("Estoy Diseñando")


programer = Programador("Jose", "500$")
programer.programar()

diseñador = Diseñador("Maria", "400$")
diseñador.Diseñar()

print(f"\n{programer.nombre} gana {programer.sueldo}\n")
print(f"{diseñador.nombre} gana {diseñador.sueldo}")