import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import lxml.html as html

url_inicial='https://www.businessinsider.es/india-lidera-10-paises-plastico-tiran-mar-888313'

r=requests.get(url_inicial)
#contenido= requests.text
r.headers

r.status_code
print(r.status_code)

soup = BeautifulSoup(r.text, 'lxml')
#print(s)

#box=soup.find('div', class_='sc-7bd27dd4-0 sc-cc294929-0 ntmro iubAzx article-header')
#title=box.find('h1').get_text()
#box = soup.find('articule', class_="sc-8768f940-0 dFGnvL article-body")
#cuadro = box.find('//div[@class="sc-8768f940-0 dFGnvL article-body]"/ul/li').get_text()
#cuadro1 = '//div[@class="sc-9d7dd242-0 ekEAEi"]/articule//div[@class=""sc-8768f940-0 dFGnvL article-body"]//ul/li/text()'
#cuadro2 = box.find('ul/li').get_text()
#print (cuadro2)
#cuadro3='//div[@class="sc-9d7dd242-0 ekEAEi"]/articule/div[@class=""sc-8768f940-0 dFGnvL article-body"]/ul/li/::marker/text()'
#print (title)

#r=requests.get(url_inicial)
#home=r.content.decode('utf-8')
#parser=html.fromstring(home)
#cuadrot=parser.xpath(cuadro1)
#print (cuadrot)

#box=soup.find('div', class_='sc-8768f940-0 dFGnvL article-body')
#prueba=box.find('p').get_text()
#print (prueba)

#box=soup.find('div', class_='sc-8768f940-0 dFGnvL article-body')
#prueba2=box.find('li').get_text()
#lista1=soup.find_all('div', class_='sc-8768f940-0 dFGnvL article-body')
#prueba3=[x.find('li').get_text() for x in lista1]
#print (prueba3)

prueba4='//div[@class="sc-8768f940-0 dFGnvL article-body"]//ul/li/text()'
r=requests.get(url_inicial)
home=r.content.decode('utf-8')
parser=html.fromstring(home)
cuadrot=parser.xpath(prueba4)
print (cuadrot)

#GENERAR DATFRAME
df=pd.DataFrame(cuadrot)
df.head()
print(df)


