# Crea una clase Calculadora con dos métodos:Crea una clase Calculadora con dos métodos:

# sumar(a, b) — retorna la suma
# restar(a, b) — retorna la resta

class Calculadora:

    def restar(self, a, b):
        self.a = a
        self.b = b
        restar = self.a - self.b
        print(f"{self.a} - {self.b} = {restar}")

    def sumar(self, a, b):
        self.a = a
        self.b = b
        sumar = self.a + self.b
        print(f"{self.a} + {self.b} = {sumar}")


resultado = Calculadora()
resultado.restar(8, 8)
resultado.sumar(9, 9)


