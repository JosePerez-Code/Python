# Tenga una lista vacía de estudiantes
# Pida al usuario cuántos estudiantes quiere agregar
# Por cada estudiante pida nombre, edad y nota (0-100)
# Guarde cada estudiante como un diccionario con esas 3 claves
# Al final muestre:

# El estudiante con la nota más alta
# El estudiante con la nota más baja
# El promedio de notas de la clase
# Todos los estudiantes que aprobaron (nota >= 60)

def escuela(cantidad):
    estudiantes = []

    for i in range(cantidad):

        nombre = input("Ingrese su nombre: ") 
        edad = int(input("Ingrese su edad: ")) 
        nota =int(input("Ingrese su nota(0-100): "))

        estudiante = {"nombre": nombre, "edad": edad, "nota": nota}
        estudiantes.append(estudiante)
    estudiantes.sort(key=lambda x : x["nota"])
    estudiantes.reverse()
    estudiantes[0]
    estudiantes[-1]
    promedio = sum(e["nota"] for e in estudiantes) / cantidad
    
    for i in (estudiantes):
        if i["nota"] >= 60:
            print(f"Aprobados: {i['nombre']}")

escuela(5)