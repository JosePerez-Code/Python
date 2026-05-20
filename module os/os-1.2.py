import os

for elemento in os.listdir(r"C:\Users\kelli\Desktop"):
    nombre, extencion = os.path.splitext(elemento)

    if extencion == ".txt":
        print(elemento)
