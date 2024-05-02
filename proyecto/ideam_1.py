from sodapy import Socrata
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium


cliente = Socrata("www.datos.gov.co", None)

inicio = '2024-01-01'
fin = '2024-12-12'

consulta = f"fechaobservacion between '{inicio}' and '{fin}' ORDER BY fechaobservacion DESC"

resultados = cliente.get("sbwg-7ju4", where=consulta, limit= 100000)

df = pd.DataFrame.from_records(resultados)

df_cundinamarca = df[df['departamento'] == 'CUNDINAMARCA']

municipios_cundinamarca = df_cundinamarca['municipio'].unique()

munucipi_elegido = 'PACHO'
df_municipio = df_cundinamarca[df_cundinamarca['municipio']== munucipi_elegido]


print(df_municipio.info())


print("fin de programa")