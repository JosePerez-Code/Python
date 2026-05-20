import os
import shutil
import time

carpeta = r"C:\Users\kelli\Downloads"

destinos = {
    "Imagenes":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico", ".tiff"],
    "Videos":       [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Musica":       [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma"],
    "Documentos":   [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Instaladores": [".exe", ".msi", ".dmg", ".pkg"],
    "Comprimidos":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Codigo":       [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Fuentes":      [".ttf", ".otf", ".woff"],
        }


while True:
    try:  

        for i in os.listdir(carpeta):
            ruta = os.path.join(carpeta, i)
            nombre, extencion = os.path.splitext(i)
            for carpeta_destino, extenciones in destinos.items():
                if extencion in extenciones:
                    destino = os.path.join(carpeta, carpeta_destino)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(ruta, destino)
                    print(f"✅ {i} → {carpeta_destino}")
    

    except Exception as e:
        print(f"Error {e}")

    time.sleep(60)
   
