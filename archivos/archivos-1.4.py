with open("archivos\\archivos.txt", "r") as base:
    contenido = base.readlines()
    for nombre in contenido:
        if len(nombre.strip()) > 4:
            print(nombre.strip())