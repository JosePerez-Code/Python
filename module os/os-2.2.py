import os

for elemento in os.listdir(r"C:\Users\kelli\Desktop"):

    ruta = os.path.join(r"C:\Users\kelli\Desktop", elemento)
    tamaño = os.path.getsize(ruta)
    tamaño_kb = tamaño / 1024
    

    if os.path.isfile(ruta):
        print(f"{elemento} - {tamaño_kb:.2f} kb")