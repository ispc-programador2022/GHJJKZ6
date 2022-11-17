import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df=pd.read_csv('Datos_Calidad_del_aire.csv')


#los 10 paises que mas emiten co2 en el mundo en 2020
df3=df[['Country/Region','2020']]
df3=df3.sort_values(by='2020', ascending=False)
df3=df3.head(10)
print(df3)

#grafica de barras
plt.subplot(1,2,1)

#grafica de barras para los 10 paises que mas emiten co2 en el mundo en 2020
plt.bar(df3['Country/Region'],df3['2020']) 
plt.title('Los 10 paises que mas emiten co2 en el mundo en 2020')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel('Emisiones de CO2')

#los 10 paises que mas emiten co2 en el mundo en 2021
df4=df[['Country/Region','2021']]
df4=df4.sort_values(by='2021', ascending=False)
df4=df4.head(10)
print(df4)

#grafica de barras para los 10 paises que mas emiten co2 en el mundo en 2021
plt.subplot(1,2,2)
plt.bar(df4['Country/Region'],df4['2021']) 
plt.title('Los 10 paises que mas emiten co2 en el mundo en 2021')
plt.xticks(rotation=15)
plt.xlabel('Paises')
plt.ylabel('Emisiones de CO2')
plt.show()