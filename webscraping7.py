from bs4 import BeautifulSoup
import requests
import pandas as pd
from seaborn import load_dataset
#Se importaron las librerias a utilizar

#Se define URL
url3 = "https://www.iqair.com/world-most-polluted-countries"
#Se definen Headers para realizar el request de la url, en algunas paginas es necesario
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(url3, headers=headers)

#response.status_code
#print(response.status_code)

soup = BeautifulSoup(response.text, 'lxml')
#A traves de pandas ubicamos las tablas que contenga la pagina web
tablas = pd.read_html(response.content, encoding = 'utf8')
#Creamos un dataframe filtrando la tabla que contengan la informacion que necesitamos
df=pd.DataFrame(tablas[0])

print (df.head(10)) 
#exportamos a csv
df.to_csv('Datos_Calidad_del_aire.csv', index=False)