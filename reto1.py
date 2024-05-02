salario, numero_extras, bonificaciones = input().split()

salario =float(salario)
numero_extras = int(numero_extras)
bonificaciones = int(bonificaciones)

valor_hora_normal = salario / 192
valor_hora_extra = valor_hora_normal * 1.25
valor_bonificacion = salario * 0.05

salario_total = salario + valor_hora_extra * numero_extras + bonificaciones * valor_bonificacion

salario_pagar = salario_total - ((salario_total * 0.035) + (salario_total * 0.04) + (salario_total * 0.01)) 

print(round(salario_pagar , 1))