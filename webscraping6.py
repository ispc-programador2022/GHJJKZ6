from bs4 import BeautifulSoup
import requests
import pandas as pd
from seaborn import load_dataset
#Se importaron las librerias a utilizar

#Se define URL
url = "https://datosmacro.expansion.com/energia-y-medio-ambiente/emisiones-co2?anio=2021"
#Se definen Headers para realizar el request de la url, en algunas paginas es necesario
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
#A traves de pandas ubicamos las tablas que contenga la pagina web
all_tables = pd.read_html(response.content, encoding = 'utf8')
#Creamos un dataframe filtrando la tabla que contengan la informacion que necesitamos
#En el mismo codigo se elimina la columna que no queremos obtener
df=pd.DataFrame(all_tables[0]).drop(columns = ['CO2 t per capita.1'])
#limpiamos caracteres especificos de la columna Paises
df["Países"] = df["Países"].str.replace("[[+]]", "").str.replace("[", "")
#data_ord = df.sort_values('Var.', ascending=False)

print (df.head(10)) 
#exportamos a csv
df.to_csv('Datos_Emisiones de CO2_v2.csv', index=False)