# Crea una clase Banco con titular y saldo. Con dos métodos:

# depositar(cantidad) — suma al saldo
# retirar(cantidad) — resta al saldo

class Banco:
    def __init__(self, titular, saldo):

        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Se depositaron {cantidad}$, saldo actual: {self.saldo}$")

    def retirar(self, cantidad):

        self.saldo -= cantidad
        print(f"Se retiro {cantidad}$, saldo actual: {self.saldo}$")
        
cuenta = Banco("kelli", 500)
cuenta.depositar(500)
cuenta.retirar(500)