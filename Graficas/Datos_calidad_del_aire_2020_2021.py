import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Datos_Calidad_del_aire.csv')


#Países y regiones más contaminados del mundo 2020
df3=df[['Country/Region','2020']]

#Creamos una nueva columna con los valores ya reemplazados por 0
pd.options.mode.chained_assignment = None
df3['2020']=df3['2020'].replace('-',0) 
df3['2020']=df3['2020'].astype(float)


df3=df3.sort_values(by='2020', ascending=False)
df3=df3.head(10)
print(df3)

#grafica de barras
plt.subplot(1,2,1)

#grafica de barras Países y regiones más contaminados del mundo 2020
plt.bar(df3['Country/Region'],df3['2020']) 
plt.title('Países y regiones más contaminados del mundo')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel('concentración promedio anual de PM2.5 (μg/m³)')

#Países y regiones más contaminados del mundo 2021
df4=df[['Country/Region','2021']]
#Creamos una nueva columna con los valores ya reemplazados por 0
df4['2021']=df4['2021'].replace('-',0) 
df4['2021']=df4['2021'].astype(float)

df4=df4.sort_values(by='2021', ascending=False)
df4=df4.head(10)
print(df4)

#grafica de barras para Países y regiones más contaminados del mundo 2021
plt.subplot(1,2,2)
plt.bar(df4['Country/Region'],df4['2021']) 
plt.title('Países y regiones más contaminados del mundo')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel(' concentración promedio anual de PM2.5 (μg/m³)')
plt.show()