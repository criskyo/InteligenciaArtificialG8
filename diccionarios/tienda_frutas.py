
db = {}

print("Bienvenidos a la tienda de frutas")

while True:
    print("Que quieres hacer")
    print("Digite P para ingresar datos")
    print("Digite L para ver la base de datos")
    print("Digite Q para salir")

    action = input()

    if action == "P":
        k = input("Ingrese la llave: ")
        nombre, precio, cantidad = input("Ingrese los datos: ").split()
        lista = [nombre, precio, cantidad]
        db[k] = lista #se crean los datos en el diccionario
    elif action == "L":
        print("Contenido de la base de datos")
        print(db)
    elif action == "Q":
        print("Bye")
        break