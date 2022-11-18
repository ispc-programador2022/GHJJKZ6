import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as html
#Se importaron las librerias a utilizar.

#link para extraer data
url1 = "https://www.liderempresarial.com/las-10-empresas-que-mas-contaminan-el-mundo/"
#Se definen Headers para realizar el request de la url, en algunas paginas es necesario.
headers = {'User-Agent':'Mozilla/5.0'}
#usamos request para enviar solicitudes a la pagina, para obtener como resultado codigo HTML de dicha pagina web.
page = requests.get(url1, headers=headers)

#creamos variable soup para localizar elementos en la pagina web con BeautifulSoup (donde asignamos la variable para obtener texto y definimos el parser lxml).
soup = BeautifulSoup(page.text, 'lxml')

count = 0
n = 4

#creamos variables lista
emp = list ()
descripT = list ()
#buscamos datos desde una etiqueta espcifica y la asignamos a una variable de soup
lista_emp = soup.find_all('h4')

#obtenemos el texto de las empresas y la agregamos en la lista
for i in lista_emp:
    emp.append(i.text)
    
s_item= BeautifulSoup(page.text, 'lxml')
#ubicamos etiquetas para obtener texto de la descripcion de las empresas
ext=s_item.find('div', class_="content-inner jeg_link_underline")
i=4
while i < 23:
    p=[x.get_text() for x in ext.select('[class="content-inner jeg_link_underline"] p')]
    desc=p[i]
    descripT.append(desc)
    i += 2
    
#print (emp)
#print (descripT)
#Creamos un dataframe y agregamos a ambas listas.
df_emp = pd.DataFrame({'NOMBRE': emp,'DESCRIPCION': descripT})
df_emp["DESCRIPCION"] = df_emp["DESCRIPCION"].str.replace(",", "")
print (df_emp)
#exportamos a csv
df_emp.to_csv('Datos_EmpresasPlasticos.csv', index=False) 
