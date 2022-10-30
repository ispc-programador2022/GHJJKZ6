import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import lxml.html as html

url_padre='https://books.toscrape.com/index.html'
root_url='https://books.toscrape.com'

#Listado de expresiones xpath

links_categorias='//ul[@class="nav nav-list"]/li//ul/li/a/@href'
titulo='//article[@class="producto_pod"]//h3/a/text()'

r=requests.get(url_padre)

home=r.content.decode('utf-8')
parser=html.fromstring(home)
categorias_url=parser.xpath(links_categorias)
categorias_url=[root_url+x for x in categorias_url]
#print(categorias_url)

r=requests.get(categorias_url[1])
home=r.content.decode('utf-8')
parser=html.fromstring(home)
titulos_book=parser.xpath(titulo)
print(titulos_book)


