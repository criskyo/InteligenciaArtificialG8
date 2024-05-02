def obtenerDatos():
    datos = {}
    datos["metros"] = float(input("Valor en metros: "))
    return datos


def metrosAPies(numero):
    return numero * 3.2808399


def piesAMetros(numero):
    return numero * (1 / 3.2808399)


def metrosAPulgadas(numero):
    return numero * 39.3700787


def metrosAYardas(numero):
    return numero * 1.0936133


def metrosAMillas(numero):
    return numero * 0.000621371192


def mostrarResultados(datos):
    dato1 = datos["metros"]
    
    resultados = {}
    resultados["metros"] = dato1
    resultados["pulgadas"] = metrosAPulgadas(dato1)
    resultados["yardas"] = metrosAYardas(dato1)
    resultados["millas"] = metrosAMillas(dato1)
    resultados["pies"] = metrosAPies(dato1)
    for clave in resultados.keys():
        print("El valor en " + clave + " es "+ str(resultados[clave]))



datos = obtenerDatos()
mostrarResultados(datos)