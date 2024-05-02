#Punto 1
#Cargue el dataset disponible en
#https://www.datos.gov.co/Econom-a-y- Finanzas/Tasa-de-Cambio-Representativa-del-Mercado-TRM/32sa-8pi3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sodapy import Socrata
cliente=Socrata('www.datos.gov.co', None)
result=cliente.get("32sa-8pi3")
df=pd.DataFrame.from_records(result)
#print(df.head())
print(df.info())

valor=pd.to_numeric(df['valor'],errors='coerce')
print(valor)

#Punto 2
#Calcular
#a. Media
#b. Mediana
#c. Desviación estándar
#d. Máximo
#e. Mínimo
#f. Máximo
#g. Rango
print('El valor de la media es: ',round(np.mean(valor),3))
print('El valor de la mediana es: ',round(np.median(valor),3))
print('El valor de la desviacion estandar es: ',round(np.std(valor),3))
print('El valor del máximo es: ',round(np.max(valor),3))
print('El valor del mínimo es: ',round(np.min(valor),3))
print('El valor del rango es: ',round(np.max(valor),3)-round(np.min(valor),3))

df['Valor_n']=valor
print(df.describe())

#Punto 5
#Hacer dos representaciones graficas que sean acordes a la naturaleza de los datos
df.hist(bins=10)
plt.title('Histograma de la variación del Dolar')
plt.xlabel('Pesos')
plt.show()


df.plot()
plt.title('Grafica de la variación del dolar sin ordenar')
plt.xlabel('Tiempo')
plt.ylabel('Pesos')
plt.grid()
plt.show()


#Ordenar las fechas y valores del data Frame
data_o=df.sort_values(by=['vigenciadesde'])
valores=list(data_o['Valor_n'])
plt.plot(valores,'r--')
plt.title('Variación hitorica del dolar')
plt.xlabel('Tiempo')
plt.ylabel('Pesos')
plt.grid()
plt.show()



print("fin de programa")
