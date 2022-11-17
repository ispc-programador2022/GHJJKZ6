import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import lxml.html as html

url1 = "https://www.liderempresarial.com/las-10-empresas-que-mas-contaminan-el-mundo/"
headers = {'User-Agent':'Mozilla/5.0'}
page = requests.get(url1, headers=headers)

soup = BeautifulSoup(page.text, 'lxml')
count = 0
n = 4
#datos_empresas=[]
#cont_empresas={}
emp = list ()
descripT = list ()
lista_emp = soup.find_all('h4')

for i in lista_emp:
    emp.append(i.text)
    
s_item= BeautifulSoup(page.text, 'lxml')
ext=s_item.find('div', class_="content-inner jeg_link_underline")
i=4
while i < 23:
    p=[x.get_text() for x in ext.select('[class="content-inner jeg_link_underline"] p')]
    desc=p[i]
    descripT.append(desc)
    i += 2
    
#print (emp)
#print (descripT)

df_emp = pd.DataFrame({'NOMBRE': emp,'DESCRIPCION': descripT})
print (df_emp)
df_emp.to_csv('Datos_EmpresasPlastico1.csv', index=False) 
