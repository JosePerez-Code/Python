# Mueve todos los archivos de tu Desktop que pesen más de 100 KB a una carpeta llamada Grandes

import os
import shutil

for carpeta, subcarpeta, archivo in os.walk(r"C:\Users\kelli\Desktop"):
    for i in archivo:
        ruta = os.path.join(carpeta, i)

        if os.path.isfile(ruta):
            tamaño = os.path.getsize(ruta)
            tamaño_kb = tamaño / 1024

            if tamaño_kb > 100:
                shutil.move(ruta, r"C:\Users\kelli\Desktop\Grandes")
