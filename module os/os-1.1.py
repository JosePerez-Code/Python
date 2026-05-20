import os

for elemento in os.listdir(r"C:\Users\kelli\Desktop"):
    ruta = os.path.join(r"C:\Users\kelli\Desktop", elemento)

    if os.path.isfile(ruta):
        print(f"{elemento} - ARCHIVO")
    else:
        print(f"{elemento} - CARPETA")