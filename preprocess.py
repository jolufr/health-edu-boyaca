#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Librerias para procesamiento de datos
import pandas as pd
import numpy as np

# Libreria para procesar caracteres especiales
import unicodedata


# In[ ]:


# Funcion para pasar a minuscula los nombre de las columnas de los conjunto
# de datos y reemplazar los espacios por guion bajo
def estandarizar_nombres_columnas(df):
  """
  La funcion estandariza los nombres de las columnas de los conjuntos de datos
  Parametros:
  df: conjunto de datos
  """
  df.columns = df.columns.str.lower().str.replace(' ', '_')
  return df.head()


# In[ ]:


# Esta funcion realiza los siguientes cambios en los datos de las columnas tipo object
# Pasar a minuscula
# Retirar las tildes
# Eliminar espacios
def limpiar_texto(df):
  """
  La funcion limpia los datos de las columnas tipo object, pasando a minuscula,
  retirando las tildes y eliminando espacios
  Parametros:
  df: conjunto de datos
  """
  for col in df.columns:
    if df[col].dtype == 'object':
      df[col] = df[col].str.lower()
      df[col] = df[col].apply(quitar_tildes)
      df[col] = df[col].str.strip()
      df[col] = df[col].str.replace(r'\s+', ' ', regex=True)
  return df


# In[ ]:


# Eliminacion de colummnas con informacion no relevenate para el proyecto
def eliminar_columnas_afiliaciones(df):
  df = df.drop(columns=['CODIGO MUNICIPIO', 'CODIGO ADMINISTRADORA', 'ADMINISTRADORA', 'NIVEL', 'ZONA'])
  return df


# In[ ]:


def eliminar_columnas_ie(df):
  df = df.drop(columns=['CODIGO DANE INSTITUCIÓN', 'ESTABLECIMIENTO EDUCATIVO', 'CODIGO DANE SEDE', 'SEDE'])
  return df


# In[ ]:


def eliminar_columnas_centros_poblados(df):
  for col in df.columns:
    if col not in ['AÑO', 'MUNICIPIO', 'ÁREA GEOGRÁFICA', 'Total Hombres', 'Total Mujeres']:
      df = df.drop(columns=[col])
  return df


# In[ ]:


def validar_nulos(df1, df2, df3):
  # Validacion de valores nulos con las columnas que se eligieron
  print('-'*15,'Valores nulos en afiliaciones: ', '\n', df1.isnull().sum(), '\n')
  print('-'*15,'Valores nulos en centros poblados: ', '\n', df2.isnull().sum(), '\n')
  print('-'*15,'Valores nulos en instituciones educativas: ', '\n', df3.isnull().sum(), '\n')


# In[ ]:


def eliminar_nulos_afiliaciones(df):
  # Se eliminan las filas con valores nulos en el conjunto de datos afiliaciones
  df = df.dropna()

  # Verificacion de la eliminacion de los valores nulos
  # en el conjunto de datos afiliaciones
  print('-'*15,'Valores nulos en afiliaciones: ', '\n', df.isnull().sum(), '\n')
  return df


# In[ ]:


def buscar_duplicados(df1, df2, df3):
  # Busqueda y eliminacion de valores duplicados
  print('-'*15,'Valores duplicados en afiliaciones: ', '\n', df1.duplicated().sum(), '\n')
  print('-'*15,'Valores duplicados en centros poblados: ', '\n', df2.duplicated().sum(), '\n')
  print('-'*15,'Valores duplicados en instituciones educativas: ', '\n', df3.duplicated().sum(), '\n')


# In[ ]:


def analisis_afiliaciones_ie(df1, df2):
  # Visualizacion de registros para su analisis
  print('-'*15,'Valores duplicados en afiliaciones: ', '\n', df1[df1.duplicated()].head(7), '\n')
  print('-'*15,'Valores duplicados en instituciones educativas: ', '\n', df2[df2.duplicated()].head(7), '\n')


# In[ ]:


def ver_info_dfs(df1, df2, df3):
  # Revision de los tipos de datos y los valores que estos representan
  print(df1.info(), '\n')
  print(df2.info(), '\n')
  print(df3.info(), '\n')


# In[ ]:


def transformacion_col_area_geografica(df):
  # Se crea una copia del conjunto de datos centros poblados
  df_copia = df.copy()
  print('Tamaño inicial de la copia del conjunto de datos: --> ', df_copia.shape, '\n')
  filas_iniciales = df_copia.shape[0]

  # De la columna area geografica se eliminan las filas que contengan el dato total
  df_copia = df_copia.drop(df_copia[df_copia['area_geografica'] == 'total'].index)
  filas_finales = df_copia.shape[0]

  # De la columna area geografica se reemplazan los siguientes valores
  # centros poblados y rural disperso por rural
  # cabecera municipal por urbana
  df_copia['area_geografica'] = df_copia['area_geografica'].replace('centros poblados y rural disperso', 'rural')
  df_copia['area_geografica'] = df_copia['area_geografica'].replace('cabecera municipal', 'urbana')
  print('Tamaño final de la copia del conjunto de datos: --> ', df_copia.shape, '\n')

  nuevas_filas = filas_iniciales - filas_finales
  print('Cantidad de filas eliminadas: --> ', nuevas_filas)
  return df_copia


# In[ ]:


def cambios_tipo_dato(df1, df2):
  # Cambio del tipo de dato para las columnas total_hombres y total_mujeres
  # en el conjunto de datos centros poblados

  df1['total_hombres'] = df1['total_hombres'].str.replace(',', '', regex=False).astype('int64')
  df1['total_mujeres'] = df1['total_mujeres'].str.replace(',', '', regex=False).astype('int64')
  df1.info()
  print('\n')

  # Cambio del tipo de dato para la columna edad en el conjunto de datos afiliaciones
  df2['edad'] = df2['edad'].astype('int64')
  df2.info()

  return df1, df2


# In[ ]:


def val_unicos_col_ano(df1, df2):
  # Valores unicos en las columnas año
  print('Valores unicos de la columna año en el conjunto de datos afiliaciones')
  print(df1['ano'].unique(), '\n')
  print('Valores unicos de la columna año en el conjunto de datos centros poblados')
  print(df2['ano'].unique(), '\n')


# In[ ]:


def filtrar_col_ano(df1,df2):
  # Se filtran las filas que tengan en la columna ano los mismos valores
  # de la misma columna del conjunto de datos afiliaciones
  df1 = df1[df1['ano'] >= 2022]
  df1 = df1[df1['ano'] <= 2023]


  # Valores unicos en las columnas año
  print('Valores unicos de la columna año en el conjunto de datos afiliaciones')
  print(df2['ano'].unique(), '\n')
  print('Valores unicos de la columna año en el conjunto de datos centros poblados')
  print(df1['ano'].unique(), '\n')

  return df1


# In[ ]:


def val_unicos_col_municipio(df1, df2, df3):
  # Total valores unicos en la columna municipio
  # para cada conjunto de datos

  unicos_afiliaciones = df1['municipio'].unique()
  unicos_centros_poblados = df2['municipio'].unique()
  unicos_instituciones_educativas = df3['municipio'].unique()

  print('Valores unicos en la columna municipio del conjunto de datos afiliaciones --> ', len(unicos_afiliaciones))
  print('Valores unicos en la columna municipio del conjunto de datos centros poblados --> ', len(unicos_centros_poblados))
  print('Valores unicos en la columna municipio del conjunto de datos instituciones educativas --> ', len(unicos_instituciones_educativas))


# In[ ]:


# Funcion para eliminar las tildes de los nombres en las columnas
def quitar_tildes(texto):
  """
  La funcion quita las tildes de los nombres de las columnas
  Parametros:
  texto: nombre de la columna
  """
  return ''.join(c for c in unicodedata.normalize('NFKD', texto)
                 if not unicodedata.combining(c))


# In[ ]:


# Limpieza de los datos
# Quitar tildes de los nombres de las columnas
# Estandarizar nombres de las columnas
def limpieza_datos(df):
  df = limpiar_texto(df)
  df.columns = [quitar_tildes(col) for col in df]
  estandarizar_nombres_columnas(df)
  return df

#df_centros_poblados = limpiar_texto(df_centros_poblados)
#df_centros_poblados.columns = [quitar_tildes(col) for col in df_centros_poblados]
#estandarizar_nombres_columnas(df_centros_poblados)

#df_instituciones_educativas = limpiar_texto(df_instituciones_educativas)
#df_instituciones_educativas.columns = [quitar_tildes(col) for col in df_instituciones_educativas]
#estandarizar_nombres_columnas(df_instituciones_educativas)


# In[ ]:


# Se listan los valores unicos, minimo y maximo de la columna edad
# del conjunto de datos afiliaciones
def listar_val_unicos_edad(df):
  print('Valores unicos')
  print(df['edad'].unique(),'\n')

  print('Valor minimo -- > ', df['edad'].min(),'\n')
  print('Valor maximo -- > ',df['edad'].max(),'\n')

  # Se obtiene el total de filas con edad cero y se calcula su participacion
  # en el total de filas del conjunto de datos

  print('\nTamaño del conjunto de datos afiliaciones con edades iguales a cero-- > ', df.shape)

  filas_edad_cero = df[df['edad'] == 0]
  cero = filas_edad_cero.shape[0]
  total_filas_afiliaciones = df.shape[0]
  print(f'\nParticipacion filas con edad cero -- > {round(cero / total_filas_afiliaciones * 100, 2)}%')

  # Se filtran las edades superiores a cero
  df = df[df['edad'] != 0]
  print('\nTamaño del conjunto de datos afiliaciones sin edades iguales a cero-- > ', df.shape)
  return df


# In[ ]:


# Agrupar los nombres de las columnas categoricas
def columnas_categoricas(df, lista):
  """
  La funcion agrupa los nombres de las columnas categoricas
  Parametros:
  df: conjunto de datos
  lista: lista de nombres de las columnas categoricas
  """
  for col in df.columns:
    if df[col].dtype =='object':
      lista.append(col)


# In[ ]:


# Agrupar los nombres de las columnas numericas
def columnas_numericas(df, lista):
  """
  La funcion agrupa los nombres de las columnas numericas
  Parametros:
  df: conjunto de datos
  lista: lista de nombres de las columnas numericas
  """
  for col in df.columns:
    if df[col].dtype =='int64' or df[col].dtype =='float64':
      lista.append(col)


# In[ ]:


def llenar_listas_nom_col(df1, df2, df3):


  # Listas para columnas numéricas
  col_num_afiliaciones = []
  col_num_copia_centros_poblados = []
  col_num_instituciones_educativas = []

  # Listas para columnas categóricas
  col_cat_afiliaciones = []
  col_cat_copia_centros_poblados = []
  col_cat_instituciones_educativas = []

  # Llamado de la funcion que guarda los nombres de columnas numericas
  columnas_numericas(df1, col_num_afiliaciones)
  columnas_numericas(df2, col_num_copia_centros_poblados)
  columnas_numericas(df3, col_num_instituciones_educativas)

  # Llamado de la funcion que guarda los nombres de columnas categoricas
  columnas_categoricas(df1, col_cat_afiliaciones)
  columnas_categoricas(df2, col_cat_copia_centros_poblados)
  columnas_categoricas(df3, col_cat_instituciones_educativas)

  print('-'*25,'Columnas numericas','-'*25)
  print('Conjunto de datos afiliaciones -- > ', col_num_afiliaciones)
  print('Conjunto de datos centros poblados -- > ', col_num_copia_centros_poblados)
  print('Conjunto de datos instituciones educativas -- > ', col_num_instituciones_educativas,'\n')

  print('-'*25,'Columnas categoricas','-'*25)
  print('Conjunto de datos afiliaciones -- > ',col_cat_afiliaciones)
  print('Conjunto de datos centros poblados -- > ',col_cat_copia_centros_poblados)
  print('Conjunto de datos instituciones educativas -- > ',col_cat_instituciones_educativas)


# In[ ]:


def crear_agregacion_afiliacion(df):
    # Creacion del conjunto de datos afiliaciones agrupado por año y municipio
    df_afiliaciones_agg = df.groupby(['ano', 'municipio']).agg(
                                                                          total_afiliados=('sexo', 'count'),
                                                                          edad_promedio =('edad', 'mean'),
                                                                          mujeres=('sexo', lambda x: (x == 'f').sum()),
                                                                          hombres=('sexo', lambda x: (x == 'm').sum()),
                                                                          regimen_subsidiado=('regimen', lambda x: (x == 'subsidiado').sum()),
                                                                          regimen_contributivo=('regimen', lambda x: (x == 'contributivo').sum()),
                                                                          regimen_especial=('regimen', lambda x: (x == 'especial').sum()),
                                                                          regimen_excepcion=('regimen', lambda x: (x == 'excepcion').sum()),
                                                                          estado_ac=('estado', lambda x: (x == 'ac').sum()),
                                                                          estado_ae=('estado', lambda x: (x == 'ae').sum())
                                                                          ).reset_index()

    # Calculo de porcentajes
    df_afiliaciones_agg['porcentaje_mujeres_afiliadas'] = (df_afiliaciones_agg['mujeres'] / df_afiliaciones_agg['total_afiliados']) * 100
    df_afiliaciones_agg['porcentaje_hombres_afiliados'] = (df_afiliaciones_agg['hombres'] / df_afiliaciones_agg['total_afiliados']) * 100

    df_afiliaciones_agg['porcentaje_r_subsidiado'] = (df_afiliaciones_agg['regimen_subsidiado'] / df_afiliaciones_agg['total_afiliados']) * 100
    df_afiliaciones_agg['porcentaje_r_contributivo'] = (df_afiliaciones_agg['regimen_contributivo'] / df_afiliaciones_agg['total_afiliados']) * 100
    df_afiliaciones_agg['porcentaje_r_especial'] = (df_afiliaciones_agg['regimen_especial'] / df_afiliaciones_agg['total_afiliados']) * 100
    df_afiliaciones_agg['porcentaje_r_excepcion'] = (df_afiliaciones_agg['regimen_excepcion'] / df_afiliaciones_agg['total_afiliados']) * 100

    df_afiliaciones_agg['porcentaje_e_ac'] = (df_afiliaciones_agg['estado_ac'] / df_afiliaciones_agg['total_afiliados']) * 100
    df_afiliaciones_agg['porcentaje_e_ae'] = (df_afiliaciones_agg['estado_ae'] / df_afiliaciones_agg['total_afiliados']) * 100

    df_afiliaciones_agg = df_afiliaciones_agg.round(2)

    print('Tamaño del nuevo conjunto datos afiliaciones -- > ', df_afiliaciones_agg.shape)
    print('\nEstructura del nuevo conjunto de datos afiliaciones')
    print(df_afiliaciones_agg.info())
    return df_afiliaciones_agg


# In[ ]:


def crear_agregacion_centros_poblados(df):
  # Creacion de las columnas con el total de poblacion para cada area geografica
  df['poblacion_rural'] = df.apply(lambda row: row['total_mujeres'] + row['total_hombres']
                                       if row['area_geografica'] == 'rural' else 0, axis=1)


  df['poblacion_urbana'] = df.apply(lambda row: row['total_mujeres'] + row['total_hombres']
                                        if row['area_geografica'] == 'urbana' else 0, axis=1)

  # Creacion del conjunto de datos agrupado por año y municipio
  df_copia_centros_poblados_agg = df.groupby(['ano', 'municipio']).agg(
                                                                       total_poblacion_rural = ('poblacion_rural', 'sum'),
                                                                       total_poblacion_urbana = ('poblacion_urbana', 'sum')
                                                                       ).reset_index()


  # Creacion de los porcentajes
  df_copia_centros_poblados_agg['porcentaje_poblacion_rural'] = (df_copia_centros_poblados_agg['total_poblacion_rural'] /
                                                          (df_copia_centros_poblados_agg['total_poblacion_rural'] + df_copia_centros_poblados_agg['total_poblacion_urbana'])) * 100

  df_copia_centros_poblados_agg['porcentaje_poblacion_urbana'] = (df_copia_centros_poblados_agg['total_poblacion_urbana'] /
                                                          (df_copia_centros_poblados_agg['total_poblacion_rural'] + df_copia_centros_poblados_agg['total_poblacion_urbana'])) * 100

  df_copia_centros_poblados_agg = df_copia_centros_poblados_agg.round(2)

  print('Tamaño del nuevo conjunto datos centros poblados -- > ', df_copia_centros_poblados_agg.shape)
  print('\nEstructura del nuevo conjunto de datos centros poblados')
  print(df_copia_centros_poblados_agg.info())
  return df_copia_centros_poblados_agg


# In[ ]:


def crear_agregacion_ie(df):
  # # Creacion del conjunto de datos agrupado por municipio
  df_instituciones_educativas_agg = df.groupby('municipio').agg(
                                                                instituciones_municipio = ('vereda', 'count'),
                                                                veredas_municipio = ('vereda', 'nunique')
                                                                ).reset_index()
  # Creacion porcentaje cubrimiento servicio de educacion por municipio
  df_instituciones_educativas_agg['promedio_ie_por_vereda'] = (df_instituciones_educativas_agg['instituciones_municipio'] /
                                                                       df_instituciones_educativas_agg['veredas_municipio'])


  df_instituciones_educativas_agg = df_instituciones_educativas_agg.round(2)

  print('Tamaño del nuevo conjunto datos instituciones educativas -- > ', df_instituciones_educativas_agg.shape)
  print('\nEstructura del nuevo conjunto de datos instituciones educativas')
  print(df_instituciones_educativas_agg.info())
  return df_instituciones_educativas_agg


# In[ ]:


def union_afiliacion_centros_poblados(df1, df2):
  # Union de los conjuntos de datos afiliaciones y centros poblados
  # que fueron filtrados por municipio y año
  df_unificado = pd.merge(
                        df1,
                        df2,
                        on = ['municipio', 'ano'],
                        how='left'
                        )

  print('Tamaño del nuevo conjunto de datos -- > ', df_unificado.shape)
  return df_unificado


# In[ ]:


def union_centros_poblados_ie(df1, df2):
  # Union del nuevo conjunto de datos con instituciones educativas filtrado por municipio
  df_unificado = pd.merge(
                        df1,
                        df2,
                        on = ['municipio'],
                        how = 'left'
                        )

  print('Tamaño del nuevo conjunto de datos -- > ', df_unificado.shape)
  print('\nEstructura del nuevo conjunto de datos ')
  print(df_unificado.info())
  return df_unificado


# In[ ]:


def linpieza_df_unificado(df):
  # Se listan las filas con valores nulos
  print(df[df['veredas_municipio'].isnull()])

  df = df.dropna()

  print('Valores nulos en el conjunto de datos unificados')
  print(df.isnull().sum())

  df['total_poblacion_municipio'] = df['total_poblacion_rural'] + df['total_poblacion_urbana']
  df['cobertura_salud'] = (df['total_afiliados'] / df['total_poblacion_municipio']) * 100

  # Eliminacion de columnas redundantes
  df = df.drop(columns=['mujeres', 'hombres', 'regimen_subsidiado', 'regimen_contributivo',
                                            'regimen_especial', 'regimen_excepcion', 'estado_ac', 'estado_ae',
                                            'total_poblacion_rural', 'total_poblacion_urbana'])

  print('Columnas finales del conjunto de datos unificados')
  print(df.isnull().sum())

  print(df.info())
  return df

