def calcular2(precio, porcentaje):
    return (precio * porcentaje / 100)


def calcular(precio, porcentaje):
   
    dato1 = calcular2(precio,porcentaje)
    
    dato2 = (precio - dato1)
    
    return dato2



############################################################

precio = int(input("ingrese el precio base del producto: "))
porcentaje = int(input("ingrese el porcentaje de descuento: "))

print("total a pagar: " , calcular(precio, porcentaje))