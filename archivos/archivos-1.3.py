with open("archivos\\Archivos.txt", "a") as escribir:
        escribir.write(input("Ingrese su nombre: ") + "\n") 

with open("archivos\\Archivos.txt", "r") as leer:
        contenido = leer.readlines()
        print(f"En la base de datos hay  {len(contenido)} usuarios guardados")
        