# Ejercicio 2
# Crea una clase Telefono con marca, modelo y precio. Crea 2 teléfonos e imprime solo el precio de cada uno.

class Telefono:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

telefono1 = Telefono("Samsung", "S24 ultra", "500$")
telefono2 = Telefono("Apple", "Iphone 17", "800$")

print(telefono1.precio)
print(telefono2.precio)