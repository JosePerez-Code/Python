# Mostrar menú: opción 1 agregar gasto, opción 2 ver gastos, opción 3 salir
# Si elige 1 → pedir nombre del gasto y monto, guardar en archivo con append
# Si elige 2 → leer el archivo y mostrar todo con el total sumado
# Si elige 3 → salir
# Todo dentro de while True para que el menú se repita
# try/except ValueError para los números

print("Bienvenido al menu de opciones, cual le gustaria elegir")
while True:
    try:
        
        print("Opcion 1: Agregar gastos")
        print("Opcion 2: ver gastos")
        print("Opcion 3: Salir del Programa")

        opcion = int(input("Ingrese la opcion que usted quiere: "))

        if opcion == 1:
            

            nombre = input("Ingrese su nombre: ")
            gasto = input("Cual fue su gasto: ")
            monto = float(input("Ingrese el valor del Gasto: "))

            with open("Exception_exercises\\base_datos.txt", "a") as guardar:
                guardar.write(f"{nombre} - {gasto} - {monto}\n")
            
            
        elif opcion == 2:
            
            with open("Exception_exercises\\base_datos.txt", "r") as leer:
                contenido = leer.readlines()
                total = 0

                for i in contenido:
                    print(i)
                    partes = i.split()
                    monto = float(partes[-1])
                    total += monto
                print(f"Total: ${total}")

        elif opcion == 3:
            print("Haz salido con exito, nos vemos luego")
            break

        else:
            print("Error, esa opcion no existe")
    except ValueError:
        print("Error, use numeros porfavor")
