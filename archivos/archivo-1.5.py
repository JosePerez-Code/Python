with open("archivos\\Archivos.txt", "r") as escribir:
    contenido = escribir.readlines()
    buscar = input("Busca el nombre: ")
    encontrado = False
    for nombres in contenido:
        if buscar in nombres:
            print(f"El nombre esta aqui {buscar}")
            encontrado = True
            break
    
    if not encontrado:
        print("No tenemos ese nombre en nuestra base de datos")
    
