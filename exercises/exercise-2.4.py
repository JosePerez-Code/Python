def lista_num(num):
    lista = []
    for i in (num):
        if i % 2 == 0:
            lista.append(i)
    return sum(lista)

ver = lista_num([1, 2, 4, 5])
print(ver)

def nombres_A(nombre):
    lista = []
    for i in (nombre):
        if i[0] == "A":
            lista.append(i)
    return lista

ver1 = nombres_A(["Angel", "Jessica", "Manuel", "Angela"])
print(ver1)
