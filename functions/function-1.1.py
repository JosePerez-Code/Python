def suma(a, b):
    return a + b

result = suma(3, 5)
print(result)

def saludo(name):
    saludo = f"Hola {name}, como estas"
    return saludo

resultado = saludo("Jose")
print(resultado)
    
def mayor(a, b):
    if a >= b:
        return f"El numero mayor es {a}"
    else:
        return f"el numero mayor es {b}"

num_mayor = mayor(3, 1)
print(num_mayor)