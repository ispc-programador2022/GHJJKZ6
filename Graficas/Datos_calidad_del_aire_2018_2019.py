import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Datos_Calidad_del_aire.csv')

#los 10 paises que mas emiten co2 en el mundo en 2018
df1=df[['Country/Region','2018']]
df1=df1.sort_values(by='2018', ascending=False)
df1=df1.head(10)
print(df1)

#grafica de barras
plt.subplot(1,2,1)

#grafica de barras para los 10 paises que mas emiten co2 en el mundo en 2018
plt.bar(df1['Country/Region'],df1['2018']) 
plt.title('Los 10 paises que mas emiten co2 en el mundo en 2018')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel('Emisiones de CO2')

#los 10 paises que mas emiten co2 en el mundo en 2019
df2=df[['Country/Region','2019']]
df2=df2.sort_values(by='2019', ascending=False)
df2=df2.head(10)
print(df2)

#grafica de barras para los 10 paises que mas emiten co2 en el mundo en 2019
plt.subplot(1,2,2)
plt.bar(df2['Country/Region'],df2['2019']) 
plt.title('Los 10 paises que mas emiten co2 en el mundo en 2019')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel('Emisiones de CO2')
plt.show()
