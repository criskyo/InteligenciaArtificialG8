n1 = float(input("Introduce un número: "))
n2 = float(input("Introduce otro número: "))

opcion = 0

print("¿Qué quieres hacer? \n1) Sumar los dos numeros \n2) Restar los dos números\n3) Multiplicar los dos numeros" )
opcion = int(input("Introduce un número: "))

if opcion == 1:
    print(" la suma de ", n1, "+" , n2, "es" , n1 + n2)
elif opcion == 2:
    print(" la resta de ", n1, "-" , n2, "es" , n1 - n2)
elif opcion == 3:
    print("el producto de ", n1, "*" , n2, "es" , n1 * n2)
else:
    print("opción incorrecta")

print("fin de programa")

