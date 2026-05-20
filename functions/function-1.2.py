def par(num):
    
    if num % 2 == 0:
        return f"tu numero es {num} y tu numero es par"
    else:
        return f"tu numero es {num} y es impar"

result = par(4)
print(result)
    
def promedio(num1, num2, num3):

    return (num1 + num2 + num3) / 3

resultado = promedio(100, 90, 70)
print(round(resultado))

def mayusnamecount(name):
    
    return f"tu nombre es {name.upper()} y tiene {len(name)} letras"

name = mayusnamecount("Jose")
print(name)

