#Punto 6
#Usando Socrata, Cargue un dataset que se encuentre en el portal de datos públicos
#de Colombia
#se usa un data set del paruqe automotor del departamento de Boyaca
#https://www.datos.gov.co/Transporte/Parque-Automotor-activo-de-servicio-particular-DEP/874t-i57z/about_data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sodapy import Socrata

cliente2=Socrata('www.datos.gov.co', None)
result=cliente2.get("874t-i57z")
df_auto=pd.DataFrame.from_records(result)
print(df_auto.head())
print(df_auto.info())

#Eliminar filas con dato nulos
df_auto=df_auto.dropna(axis=0, how='any')
print(df_auto.info())

print(df_auto.describe())

print(df_auto.head())

#Revisar si hay registros duplicados
print(df_auto.duplicated())

df_auto.drop_duplicates(inplace = True)

print(df_auto.info())

#Punto 8
#Presentar el dataset, mostrando datos estadísticos y gráficas
print(df_auto.head())

var=list((df_auto['modelo']))
modelo=[]
for i in range(len(var)):
  modelo.append(int(var[i]))

modelo_a=np.array(modelo)
print('La media de los modelos es: ', np.mean(modelo_a))

#Grafica del histograma de modelos
plt.hist(modelo_a, bins=10)
plt.axvline(np.mean(modelo_a), ymin=0.0, ymax=0.9,color='r')
plt.title('Histograma de los modelos del parque automotor')
plt.grid()
plt.show()

#Graficas el diagrama de caja de los modelos
plt.boxplot(modelo_a)
plt.title('Diagram de caja para el modelo')
plt.ylabel('Años')
plt.grid()
plt.show()

#Analisis de las clases del parque automotor
df_clase=df_auto[['clase']]
df_clase.head()

df_clase.info()

df_clase.tail()

lista_clase=list(df_clase['clase'])
for i in lista_clase:
  print(i)

def contar(n, vec):
  '''Para esta funcion n es el numero a contar y vec es la lista donde contar '''
  count=0
  for i in vec:
    if i==n:
      count+=1
  return count


print('AUTOMOVIL aparece: ',contar('AUTOMOVIL', lista_clase))
print('CAMPERO aparece: ',contar('CAMPERO', lista_clase))
print('CAMIONETA aparece: ',contar('CAMIONETA', lista_clase))
print('CAMION aparece: ',contar('CAMION', lista_clase))
print('MOTOCICLETA aparece: ',contar('MOTOCICLETA', lista_clase))
print('VOLQUETA aparece: ',contar('VOLQUETA', lista_clase))
print('BUSETA aparece: ',contar('BUSETA', lista_clase))
print('MICRO BUS aparece: ',contar('MICRO BUS', lista_clase))

aux=[contar('AUTOMOVIL', lista_clase), contar('CAMPERO', lista_clase),contar('CAMIONETA', lista_clase),
     contar('CAMION', lista_clase),contar('MOTOCICLETA', lista_clase), contar('VOLQUETA', lista_clase),
     contar('BUSETA', lista_clase) , contar('MICRO BUS', lista_clase)]
print('La suma total es de: ', sum(aux))

num_clase=[]
for i in range(len(lista_clase)):
  num_clase.append(contar(lista_clase[i],lista_clase))

print(num_clase)
print(len(num_clase))

#Diagrama de Barras
categoria=['AUTO','CAM','CAMI','CAMIO', 'MOTO','VOL','BUS','MICRO']
plt.bar(categoria,aux,width=0.8, color='lime')
plt.xlabel('Clases')
plt.ylabel('Veces que se repiten')
plt.title('Análisi sobre las clases de automotores')
plt.grid()
plt.show()





