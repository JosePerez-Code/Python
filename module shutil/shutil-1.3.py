import os
import shutil


# os.chdir(r"c:\Users\kelli\Desktop")
# os.mkdir("Backup")

for i in os.listdir(r"c:\Users\kelli\Desktop"):
    ruta = os.path.join(r"c:\Users\kelli\Desktop", i)
    nombre, extencion = os.path.splitext(i)
    if extencion == ".txt":
        shutil.move(ruta, r"C:\Users\kelli\Desktop\Backup")