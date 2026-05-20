# Pedir nombre
# Pedir dos números
# Preguntar qué operación quiere
# Calcular el resultado
# Manejar ValueError si escribe letras en los números
# Manejar ZeroDivisionError si divide entre cero
# Mostrar el resultado con el nombre del usuario

while True:
    try:
        nombre = input("Ingrese un nombre: ").capitalize()
        a = float(input("Ingrese el primer numero: "))
        b = float(input("Ingrese el segundo numero: "))
        operacion = input("Escoja una operacion(Suma, Resta, Multiplicacion, Division): ").capitalize()

        if operacion == "Suma":
            print(f"{nombre} la suma de {a} y {b} es {a + b}")
            break
        elif operacion == "Resta":
            print(f"{nombre} la resta de {a} y {b} es {a - b}")
            break
        elif operacion == "Multiplicacion":
            print(f"{nombre} la multiplicacion de {a} y {b} es {a * b}")
            break
        elif operacion == "Division":
            print(f"{nombre} la division de {a} y {b} es {a / b}")
            break
        else:
            print("Elija una de las opciones porfavor")
    except ValueError:
        print("Use numeros para la operacion")
    except ZeroDivisionError:
        print("No divida por cero porfavor")