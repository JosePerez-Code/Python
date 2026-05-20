# Recorre tu Desktop con os.walk() y encuentra todos los archivos que pesen más de 100 KB, imprime su nombre y tamaño.

import os

for carpeta, subcarpeta, archivos in os.walk(r"C:\Users\kelli\Desktop"):
    for i in archivos:
        ruta = os.path.join(carpeta, i)

        if os.path.isfile(ruta):
            tamaño = os.path.getsize(ruta)
            tamaño_kb = tamaño / 1024

            if tamaño_kb > 100:
                print(f"{i} - {tamaño_kb:.2f} KB")