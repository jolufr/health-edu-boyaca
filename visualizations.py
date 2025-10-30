#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Librerias visualizaciones
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


def histograma_col_ano_afiliaciones(df):
  # Visualizacion de frecuencia de la columna año
  plt.figure(figsize=(6, 4))
  sns.histplot(data=df, x='ano', bins=2, kde=False)
  plt.title('Histograma para la columna año del conjunto de datos afiliaciones')
  plt.xlabel('Año')
  plt.ylabel('Frecuencia')
  plt.show()


# In[ ]:


def histograma_col_edad_afiliaciones(df):
  # Visualizacion de frecuencia de la columna edad
  plt.figure(figsize=(6, 4))
  sns.histplot(data=df, x='edad', bins=12, kde=False)
  plt.title('Histograma para la columna edad del conjunto de datos afiliaciones')
  plt.xlabel('Edad')
  plt.ylabel('Frecuencia')
  plt.show()


# In[ ]:


def histograma_col_ano_centros_poblados(df):
  # Visualizacion de frecuencia de la columna edad del conjunto de datos centros poblados
  plt.figure(figsize=(6, 4))
  sns.histplot(data=df, x='ano', bins=2, kde=False)
  plt.title('Histograma para la columna año del conjunto de datos centros poblados')
  plt.xlabel('Año')
  plt.ylabel('Frecuencia')
  plt.show()


# In[ ]:


def distribucion_genero_centros_poblados(df):
  # Se halla el total de hombres y mujeres en el conjunto de datos centros poblados
  mujeres = df['total_mujeres'].sum()
  hombres = df['total_hombres'].sum()

  # Se crean listas con los totales y generos
  valores = [mujeres, hombres]
  etiquetas = ['Mujeres', 'Hombres']

  # Se genera el grafico de generos
  plt.pie(valores, labels=etiquetas, startangle=90, autopct='%1.1f%%')
  plt.title('Distribucion por genero - Centros poblados')
  plt.axis('equal')
  plt.show()


# In[ ]:


def distribucion_genero_afiliaciones(df):
  # Se halla el total de hombres y mujeres en el conjunto de datos afiliaciones
  mujeres = (df['sexo']=='f').sum()
  hombres = (df['sexo']=='m').sum()

  # Se crean listas con los totales y generos
  valores = [mujeres, hombres]
  etiquetas = ['Mujeres', 'Hombres']

  # Se genera el grafico de generos
  plt.pie(valores, labels=etiquetas, startangle=90, autopct='%1.1f%%')
  plt.title('Distribucion por genero - Afiliaciones sistema de salud')
  plt.axis('equal')
  plt.show()


# In[ ]:


def frecuencia_afiliacion_municipio(df):
  # Visualizacion de la frecuencia de afiliaciones por municipio
  df['municipio'].value_counts().head(80).plot(kind='bar', figsize=(18,4))
  plt.title('Frecuencia de afiliaciones al sistema de salud por municipio')
  plt.xlabel('Municipio')
  plt.ylabel('Frecuencia')
  plt.show()


# In[ ]:


def frecuencia_regimen_afiliacion(df):
  # Se obtiene la frecuencia de cada regimen y se grafica
  frecuencia = df['regimen'].value_counts(normalize=True) * 100

  frecuencia.plot(kind='bar', figsize=(8,4), color='skyblue')
  plt.title('Frecuencia por regimen de afiliacion')
  plt.xlabel('Regimen')
  plt.ylabel('Porcentaje (%)')

  for i, v in enumerate(frecuencia):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

  plt.ylim(0, frecuencia.max() + 5)
  plt.show()


# In[ ]:


def frecuencia_estado_afiliacion(df):
  # Se obtiene la frecuencia de cada estado y se grafica
  frecuencia = df['estado'].value_counts(normalize=True) * 100

  frecuencia.plot(kind='bar', figsize=(8,4), color='skyblue')
  plt.title('Frecuencia de estado en afiliaciones al sistema de salud')
  plt.xlabel('Estado')
  plt.ylabel('Porcentaje (%)')

  for i, v in enumerate(frecuencia):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

  plt.ylim(0, frecuencia.max() + 5)
  plt.show()


# In[ ]:


def frecuencia_area_geografica_centros_poblados(df):
  # Se obtiene la frecuencia de cada area geografica y se grafica
  frecuencia = df['area_geografica'].value_counts(normalize=True) * 100

  frecuencia.plot(kind='bar', figsize=(8,4), color='skyblue')
  plt.title('Frecuencia de areas geograficas en centros poblados')
  plt.xlabel('Regimen')
  plt.ylabel('Porcentaje (%)')

  for i, v in enumerate(frecuencia):
    plt.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

  plt.ylim(0, frecuencia.max() + 5)
  plt.show()


# In[ ]:


def frecuencia_ie_municipio(df):
  # Visualizacion frecuencia instituciones educativas por municipio
  df['municipio'].value_counts().head(80).plot(kind='bar', figsize=(18,4))
  plt.title('Frecuencia de instituciones educativas por municipio')
  plt.xlabel('Municipio')
  plt.ylabel('Frecuencia')
  plt.show()


# In[ ]:


def frecuencia_ie_vereda(df):
  # Se obtiene el total de instituciones educativas de dificil acceso
  total_instituciones = df['vereda'].value_counts().sum()
  print('Total instituciones educativas -- > ', total_instituciones)

  # Se obtiene el total de veredas
  total_veredas = df['vereda'].nunique()
  print('Total veredas -- > ', total_veredas)

  # Promedio de instituciones educvativas por veredas
  print(f'Promedio de instituciones educativas por vereda -- > {round(total_instituciones / total_veredas, 2)}')
  df['vereda'].value_counts().head(80).plot(kind='bar', figsize=(18,4))
  plt.title('Frecuencia de instituciones educativas por vereda')
  plt.xlabel('Municipio')
  plt.ylabel('Frecuencia')
  plt.show()


# In[ ]:


def mapacorrelacion_variables(df):
  # Mapa de correlaciones
  df_corr = df.drop(columns=['municipio']).corr()

  plt.figure(figsize=(18, 16))
  sns.heatmap(df_corr,
              annot=True,
              center=0,
              fmt='.1f',
              cmap='coolwarm',
              linewidths=0.5)
  plt.title('Mapa de correlaciones entre variables')
  plt.show()

  print('\n')
  correlaciones_fuertes = df_corr[(df_corr > 0.55) & (df_corr < 1)]
  correlaciones_fuertes = correlaciones_fuertes.stack().reset_index()
  correlaciones_fuertes.columns = ['Columna1', 'Columna2', 'Correlacion']
  print('Correlaciones fuertes')
  print(correlaciones_fuertes)
  return df_corr


# In[ ]:


def ie_rural_vsr_regimen_sudsidiado(df):
  # Visualizacion Instituciones Educativas Rurales vs Regimen Sudsidiado
  plt.figure(figsize=(8,4))
  sns.regplot(data=df, x='promedio_ie_por_vereda', y='porcentaje_r_subsidiado')
  plt.title('Instituciones Educativas Rurales vs Regimen Sudsidiado')
  plt.xlabel('Promedio instituciones por vereda')
  plt.ylabel('Porcentaje de regimen subsidiado por municipio')
  plt.show()


# In[ ]:


def ie_rural_vs_regimen_contributivo(df):
  # Visualizacion Instituciones Educativas Rurales vs Regimen Contributivo
  plt.figure(figsize=(8,4))
  sns.regplot(x='promedio_ie_por_vereda', y='porcentaje_r_contributivo', data=df)
  plt.title('Instituciones Educativas Rurales vs Regimen Contributivo')
  plt.xlabel('Promedio instituciones por vereda')
  plt.ylabel('Porcentaje de regimen contributivo por municipio')
  plt.show()


# In[ ]:


def porcentaje_poblacion_rural_municipio_vs_ie_Vereda(df):
  contar_mayor_2 = (df['promedio_ie_por_vereda']> 2).sum()

  print(contar_mayor_2)

  plt.figure(figsize=(8,4))
  sns.regplot(x='porcentaje_poblacion_rural', y='promedio_ie_por_vereda', data=df)
  plt.title('Porcentaje Poblacion Rural Municipio vs Instituciones Educativas por Vereda')
  plt.xlabel('Porcentaje poblacion rural municipio')
  plt.ylabel('Numero de instituciones por vereda')
  plt.show()


# In[ ]:


def porcentaje_poblacion_rural_municipio_vs_ie_vereda(df):
  # Visualizacion Porcentaje Poblacion Rural Municipio vs Instituciones Educativas por Vereda
  contar_mayor_2 = (df['promedio_ie_por_vereda']> 2).sum()

  print(contar_mayor_2)

  plt.figure(figsize=(8,4))
  sns.regplot(x='porcentaje_poblacion_rural', y='promedio_ie_por_vereda', data=df)
  plt.title('Porcentaje Poblacion Rural Municipio vs Instituciones Educativas por Vereda')
  plt.xlabel('Porcentaje poblacion rural municipio')
  plt.ylabel('Numero de instituciones por vereda')
  plt.show()


# In[ ]:


def porcentaje_poblacion_rural_municipio_vs_porcentaje_afiliados_subsidiado(df):
  # Visualizacion Porcentaje Poblacion Rural Municipio Vs. Porcentaje Afiliados Regimen Subsidiado
  plt.figure(figsize=(8,4))
  sns.regplot(data=df, x='porcentaje_poblacion_rural', y='porcentaje_r_subsidiado')
  plt.title('Porcentaje Poblacion Rural Municipio Vs. Porcentaje Afiliados Regimen Subsidiado')
  plt.xlabel('Porcentaje Poblacion Rural Municipio')
  plt.ylabel('Porcentaje Afiliados Regimen Subsidiado')
  plt.show()


# In[ ]:


def porcentaje_poblacion_urbana_municipio_vs_porcentaje_afiliados_subsidiado(df):
  # Vusualizacion Porcentaje Poblacion Urbana Municipio Vs. Porcentaje Afiliados Regimen Subsidiado
  plt.figure(figsize=(8,4))
  sns.regplot(data=df, x='porcentaje_poblacion_urbana', y='porcentaje_r_subsidiado')
  plt.title('Porcentaje Poblacion Urbana Municipio Vs. Porcentaje Afiliados Regimen Subsidiado')
  plt.xlabel('Porcentaje Poblacion Urbana Municipio')
  plt.ylabel('Porcentaje Afiliados Regimen Subsidiado')
  plt.show()

