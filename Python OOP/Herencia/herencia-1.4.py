# Crea una clase Figura con atributo color y método describir(). Luego crea:

# Circulo — hereda de Figura y tiene método area(radio)
# Rectangulo — hereda de Figura y tiene método area(largo, ancho)

class Figura:

    def __init__(self, color):
        
        self.color = color

    def describir(self):

        print("Describiendo la figura")

class Circulo(Figura):

    def __init__(self, color):
        super().__init__(color)

    def area(self, radio):
        
        print(f"Este es el radio de tu circulo: {radio} cm")

class Rectangulo(Figura):

    def __init__(self, color):
        super().__init__(color)

    def area(self, largo, ancho):

        print(f"Tu rectangulo mide {largo} cm de lago y {ancho} cm de ancho")

circulo = Circulo("verde")
circulo.area(60)

rectangulo = Rectangulo("azul")
rectangulo.area(60, 50)