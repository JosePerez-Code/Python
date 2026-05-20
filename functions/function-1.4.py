def letra(texto):
    lista = list([])

    for i in (texto.split()):
        if len(i) > 4:
            lista.append(i)
    return lista
    
ver = letra("Hola como estan todos ustedes")
print(ver)

def primo(num):
    for i in range(2, num):
        if num % i == 0:
            return "No es primo"
    return "Es primo"

ver1 = primo(10)
print(ver1)

def primos_hasta(num):
    for i in range(2, num + 1):
        if primo(i) == "Es primo":
            print(i)

primos_hasta(20)