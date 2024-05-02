import csv

with open("archivos/Catalogo_Estaciones_IDEAM (1).csv", encoding="utf-8") as archivo:
    reader = csv.reader(archivo)
    print(reader)
    for linea in reader:
        print(linea)