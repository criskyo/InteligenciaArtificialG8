from sodapy import Socrata
import pandas as pd


cliente = Socrata("www.datos.gov.co", None)
resultados = cliente.get("sbwg-7ju4", limit= 10000)

df = pd.DataFrame.from_records(resultados)
print(df.info())

print("fin de programa")