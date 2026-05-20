def lista(num):
    num.sort()
    return f"el numero menor de la lista es {num[0]}, y el numero mayor de la lista es {num[-1]}"

mostrar = lista([50, 35, 33, 90, 105])
print(mostrar)

def multi(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

multi(4)

def vocal(palabra):
    vocales = "aeiou"
    contador = 0
    for i in (palabra):
        if i in vocales:
            contador += 1
    return contador

ver1 = vocal("como estan todos")
print(ver1)
            