import os
from datetime import datetime


# ======================================
# CLASE BASE
# ======================================

class Cuenta:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.historial = f"{self.titular}_historial.txt"

        self.registrar_movimiento(
            f"Cuenta creada con saldo inicial de ${self.saldo}"
        )

    def depositar(self, monto):

        if monto > 0:
            self.saldo += monto

            self.registrar_movimiento(
                f"Depósito: +${monto}"
            )

            print("Depósito realizado correctamente")

        else:
            print("Monto inválido")

    def retirar(self, monto):

        if monto <= 0:
            print("Monto inválido")
            return

        if monto > self.saldo:
            print("Fondos insuficientes")
            return

        self.saldo -= monto

        self.registrar_movimiento(
            f"Retiro: -${monto}"
        )

        print("Retiro realizado correctamente")

    def ver_saldo(self):
        print(f"Saldo actual: ${self.saldo}")

    def registrar_movimiento(self, mensaje):

        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.historial, "a", encoding="utf-8") as archivo:

            archivo.write(f"[{fecha}] {mensaje}\n")


# ======================================
# HERENCIA
# ======================================

class CuentaAhorros(Cuenta):

    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)
        self.tipo = "Ahorros"


class CuentaCorriente(Cuenta):

    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)
        self.tipo = "Corriente"


# ======================================
# BANCO
# ======================================

class Banco:

    def __init__(self):
        self.cuentas = []

    def crear_cuenta(self):

        titular = input("Nombre del titular: ")

        print("\n1. Cuenta Ahorros")
        print("2. Cuenta Corriente")

        opcion = input("Seleccione tipo de cuenta: ")

        saldo_inicial = float(input("Saldo inicial: "))

        if opcion == "1":

            cuenta = CuentaAhorros(titular, saldo_inicial)

        elif opcion == "2":

            cuenta = CuentaCorriente(titular, saldo_inicial)

        else:
            print("Opción inválida")
            return

        self.cuentas.append(cuenta)

        print("Cuenta creada exitosamente")

    def buscar_cuenta(self, titular):

        for cuenta in self.cuentas:

            if cuenta.titular.lower() == titular.lower():
                return cuenta

        return None

    def operar_cuenta(self):

        titular = input("Ingrese nombre del titular: ")

        cuenta = self.buscar_cuenta(titular)

        if not cuenta:
            print("Cuenta no encontrada")
            return

        while True:

            print("\n===== OPERACIONES =====")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Ver saldo")
            print("4. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":

                monto = float(input("Monto a depositar: "))
                cuenta.depositar(monto)

            elif opcion == "2":

                monto = float(input("Monto a retirar: "))
                cuenta.retirar(monto)

            elif opcion == "3":

                cuenta.ver_saldo()

            elif opcion == "4":

                break

            else:
                print("Opción inválida")


# ======================================
# PROGRAMA PRINCIPAL
# ======================================

def menu():

    banco = Banco()

    while True:

        print("\n===== SISTEMA BANCARIO =====")
        print("1. Crear cuenta")
        print("2. Operar cuenta")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            banco.crear_cuenta()

        elif opcion == "2":

            banco.operar_cuenta()

        elif opcion == "3":

            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()