import csv

while True:
    try:        

        print("Opcion 1: Agregar contactos.")
        print("Opcion 2: Ver contactos.")
        print("Opcion 3: salir")

        opcion = int(input("Elije una opcion."))

        if opcion == 1:

            nombre = input("Ingresa el nombre del contacto")
            telefono = int(input("Ingresa el telefono del contacto"))
            correo = input("Ingresa el correo del contacto")


            with open("archivos\\contactos.csv", "a", newline="") as agregar:
                guardar = csv.writer(agregar)
                guardar.writerow([nombre, telefono, correo])
            
            


        elif opcion == 2:
            with open("archivos\\contactos.csv", "r") as leer:
                reader = csv.reader(leer)
                for i in reader:
                    print(f"{i[0]} - {i[1]} - {i[2]}")



        elif opcion == 3:
            print("Haz salido del programa con exito.")

            break
        else:
            print("Error esa opcion no existe")
    
    except ValueError:
        print("Error, Ingrese un numero correcto")
