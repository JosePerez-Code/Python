with open("archivos\\Archivo.txt", "r") as Archivo:
    contenido = Archivo.readlines()
    for linea in contenido:
        print(linea.strip())
    