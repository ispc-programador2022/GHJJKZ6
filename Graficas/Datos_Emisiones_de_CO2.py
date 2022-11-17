import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Datos_Emisiones de CO2_v2.csv')

#paises con mayor emision de CO2 per capita 
df1=df[['Países','CO2 t per capita']]
df1=df1.sort_values('CO2 t per capita', ascending=False)
df1=df1.head(10)
print(df1)

#grafica de pie paises con mayor emision de CO2 per capita
plt.pie(df1['CO2 t per capita'],labels=df1['Países'],autopct='%1.1f%%')
plt.title('Paises con mayor emision de CO2 per capita')
plt.show()

