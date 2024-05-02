#CRUD

nombres = ["Luis", "Ana", "Ricardo", "Maria"]

#leer la lista
#print(nombres)

print(nombres[0])
print(nombres[3])

#actualizar
nombres[3] = "Ivone"

#agregar

nombres.append("Camilo")

nombres.insert(1, "Sandra")

#borrar

nombres.pop(4)

del nombres[0]

nombres.clear()

numeros = [21, 15, 34, 2, 5, 7, 10]
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

letras = ["a", "b", "c", "d"]
letras.reverse()

print("fin de programa")