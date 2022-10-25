from bs4 import BeautifulSoup
import requests

website = 'https://www.minderoo.org/plastic-waste-makers-index/data/indices/producers/'
respuesta = requests.get(website)
contenido = respuesta.text

soup = BeautifulSoup(contenido, 'lxml')
#print(soup.prettify())


