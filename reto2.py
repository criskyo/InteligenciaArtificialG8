distancia, velocidad_max, tiempo = input().split()

distancia = float(distancia)
velocidad_max = float(velocidad_max)
tiempo = float(tiempo)

distancia_1 = distancia / 1000
tiempo_1 = tiempo / 3600

velocidad_media = distancia_1 / tiempo_1

velocidad_multa = velocidad_max * 1.2

if(distancia < 0 or velocidad_max < 0 or tiempo < 0):
    print("ERROR")
elif(velocidad_media <= velocidad_max):
    print("OK")
elif(velocidad_media > velocidad_max and velocidad_media < velocidad_multa):
    print("MULTA")
else:
    print("CURSO SENSIBILIZACION")
