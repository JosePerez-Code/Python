import os

# renombrar un archivo
# os.rename(r"C:\Users\kelli\Desktop\Viejo.txt", r"C:\Users\kelli\Desktop\Nuevo.txt")

# cuanto pesa un archivo
tamaño = os.path.getsize(r"C:\Users\kelli\Desktop\Nuevo.txt")
tamaño_kb = tamaño / 1024

print(f"{tamaño_kb:.2f} KB")


