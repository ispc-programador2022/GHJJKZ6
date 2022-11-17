import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Datos_Calidad_del_aire.csv')

#Países y regiones más contaminados del mundo 2018
df1=df[['Country/Region','2018']]

#Creamos una nueva columna con los valores ya reemplazados por 0
pd.options.mode.chained_assignment = None
df1['2018']=df1['2018'].replace('-',0) 
df1['2018']=df1['2018'].astype(float)

df1=df1.sort_values('2018', ascending=False)
df1=df1.head(10)
print(df1)

#grafica de barras
plt.subplot(1,2,1)

#grafica de barras para Países y regiones más contaminados del mundo  2018
plt.bar(df1['Country/Region'],df1['2018']) 
plt.title('Países y regiones más contaminados del mundo')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel(' concentración promedio anual de PM2.5 (μg/m³)')

#Países y regiones más contaminados del mundo  2019
df2=df[['Country/Region','2019']]

#Creamos una nueva columna con los valores ya reemplazados por 0
df2['2019']=df2['2019'].replace('-',0) 
df2['2019']=df2['2019'].astype(float)

df2=df2.sort_values(by='2019', ascending=False)
df2=df2.head(10)
print(df2)

#grafica de barras para Países y regiones más contaminados del mundo  2019
plt.subplot(1,2,2)
plt.bar(df2['Country/Region'],df2['2019']) 
plt.title('Países y regiones más contaminados del mundo ')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel(' concentración promedio anual de PM2.5 (μg/m³)')
plt.show()
