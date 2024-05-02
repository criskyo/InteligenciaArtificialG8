import random

def generar_contraseña(longitud):
    caracteres = "abcdefghijklmnopqrstuvwxyz0123456789"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

longitud = int(input("Ingrese la longitud deseada para la contraseña: "))
contraseña_generada = generar_contraseña(longitud)

print("La contraseña generada es:", contraseña_generada)

