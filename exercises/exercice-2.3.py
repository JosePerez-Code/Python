def num_lista(lista):
    nueva_lista = []
    

    for i in (lista):
        if i not in nueva_lista:
            nueva_lista.append(i)
    return nueva_lista
          
ver = num_lista([1, 2, 4, 4, 2, 5])
print(ver)

def palabra_larga(palabra):
    texto = palabra.split()
    palabra_mas_larga = ""
    for i in (texto):
        if len(i) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return i

ver1 = palabra_larga("hola como estas beibi girlds")
print(ver1)

def sum_lista(texto):
    letra = str(texto)
    total = 0
    for i in (letra):
        total += int(i)
    return total

ver2 = sum_lista(12345)
print(ver2)

            
        
    
