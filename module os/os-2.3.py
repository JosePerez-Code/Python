import os
    
for carpeta, subcarpetas, archivos in os.walk(r"C:\Users\kelli\Desktop"):
    for i in archivos:
        print(i)
