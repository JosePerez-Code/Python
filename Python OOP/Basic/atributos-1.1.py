class Coche:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

auto1 = Coche("Ferrari", "Verde", "100KM/h")
auto2 = Coche("Porche", "Rojo", "110KM/h")

print(auto1.marca)
print(auto2.marca)
