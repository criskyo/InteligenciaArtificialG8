diccionario = {
    "llave1": "Entorno de desarrollo integrado",
    "llave2": "Programación orientada a objetos",
    "llave3": "Sistema de administracion de bases de datos"
}

#leer
#print(diccionario)
#print(len(diccionario))

print(diccionario["llave1"])

print(diccionario.get("llave3"))

#actualizar valores

diccionario["llave2"] = "Algoritmos de Inteligencia Artificial"

#borrar elementos
#diccionario.pop("llave1")

#diccionario.clear()

llaves = list(diccionario.keys())

#agregar elementos en diccionario

diccionario["llave4"] = "Extructuras de datos"

print("fin de programa")
