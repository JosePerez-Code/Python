# Creá un programa que pida el nombre y edad de 4 personas, las
# guarde en una lista, las ordene por edad y muestre quién es el más joven y el más viejo.

def obtener_cantidad_compañeros(cantidad_alumno):
    compas = []

    for i in range(4):
        nombre = input("Ingrese su Nombre: ")
        edad = int(input("Ingrese su edad: "))
        compa = (nombre,edad)
        compas.append(compa)
    compas.sort(key=lambda x : x [1])
    asistente = compas [0][0]
    profesor = compas [-1][0]

    return asistente, profesor

asistente, profesor = obtener_cantidad_compañeros(4)
print(f"El asistente de la classe es: {asistente}, El profesor de la classe es: {profesor}")