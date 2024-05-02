from pathlib import Path
from time import ctime

archivos = Path("archivos/archivo.txt") 
print(archivos.exists())
print("creacion: ",ctime(archivos.stat().st_ctime))
print("acceso: ",ctime(archivos.stat().st_atime))
print("modificación: ",ctime(archivos.stat().st_mtime))