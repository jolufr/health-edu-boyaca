#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Librerias machine learning
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Molulos metricas machine learning
from sklearn.metrics import r2_score, mean_absolute_percentage_error

import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


def entrenamiento_validacion_prediciones_poblacion(df):
  # Seleccion de las variables predictoras poblacion total municipio
  features = df[['porcentaje_poblacion_rural', 'porcentaje_poblacion_urbana', 'veredas_municipio', 'total_afiliados']]
  target = df['total_poblacion_municipio']

  # Escalado de caracteristicas
  standar_r_poblacion = StandardScaler()
  features_escaladas = standar_r_poblacion.fit_transform(features)

  X_train_poblacion, X_test_poblacion, y_train_poblacion, y_test_poblacion = train_test_split(
                                                                                            features_escaladas,
                                                                                            target,
                                                                                            test_size=0.2,
                                                                                            random_state=21
                                                                                            )

  # Entrenamiento del modelo y predicciones
  modelo_poblacion = LinearRegression()
  modelo_poblacion.fit(X_train_poblacion, y_train_poblacion)
  target_predicciones = modelo_poblacion.predict(X_test_poblacion)

  # Evaluacion del modelo
  print('R2 -- >', round(r2_score(y_test_poblacion, target_predicciones) * 100, 2), '%') # Porcentaje de predicciones correctas
  print('MAPE -->', round(mean_absolute_percentage_error(y_test_poblacion, target_predicciones) * 100, 2), '%') # Error porcentual medio absoluto
  return y_test_poblacion, target_predicciones, modelo_poblacion, features_escaladas, y_test_poblacion, target_predicciones


# In[ ]:


def visualizacion_poblacion_real_vs_predicha(y_test_poblacion, target_predicciones):
  # Visualizacion real vs prediccion
  # Poblacion total
  plt.figure(figsize=(6, 4))
  sns.scatterplot(x = y_test_poblacion, y = target_predicciones)
  plt.xlabel('Poblacion Real')
  plt.ylabel('Poblacion Predicha')
  plt.title('Poblacion Total: Real Vs Predicha')
  plt.grid()
  plt.show()


# In[ ]:


def entrenamiento_validacion_prediciones_cobertura_salud(df):
  # Seleccion de las variables predictoras para cobertura en salud
  features_salud = df[['porcentaje_poblacion_rural', 'porcentaje_poblacion_urbana',
                                'total_afiliados', 'porcentaje_r_subsidiado', 'porcentaje_r_contributivo',
                                'total_poblacion_municipio', 'ano', 'edad_promedio', 'porcentaje_e_ae',
                                'porcentaje_mujeres_afiliadas', 'porcentaje_hombres_afiliados',
                                'instituciones_municipio', 'veredas_municipio', 'promedio_ie_por_vereda',
                                'porcentaje_r_especial', 'porcentaje_r_excepcion', 'porcentaje_e_ac']]

  target_salud = df['cobertura_salud']

  # Escalado de caracteristicas
  standar_r_salud = StandardScaler()
  features_escaladas_salud = standar_r_salud.fit_transform(features_salud)

  X_train_salud, X_test_salud, y_train_salud, y_test_salud = train_test_split(
                                                                              features_escaladas_salud,
                                                                              target_salud,
                                                                              test_size=0.2,
                                                                              random_state=21
                                                                              )

  # Entrenamiento del modelo y predicciones
  modelo_salud = LinearRegression()
  modelo_salud.fit(X_train_salud, y_train_salud)
  target_predicciones_salud = modelo_salud.predict(X_test_salud)

  # Evaluacion del modelo
  print('R2 -- >', round(r2_score(y_test_salud, target_predicciones_salud) * 100, 2), '%')
  print('MAPE -->', round(mean_absolute_percentage_error(y_test_salud, target_predicciones_salud) * 100, 2), '%')
  return y_test_salud, target_predicciones_salud, modelo_salud, features_escaladas_salud, y_test_salud, target_predicciones_salud


# In[ ]:


def visualizacion_cobertura_salud_real_vs_predicha(y_test_salud, target_predicciones_salud):
  # Visualizacion real vs prediccion
  # Cobertura salud
  plt.figure(figsize=(6, 4))
  sns.scatterplot(x = y_test_salud, y = target_predicciones_salud)
  plt.xlabel('Cobertura Real')
  plt.ylabel('Cobertura Predicha')
  plt.title('Cobertura Salud: Real Vs Predicha')
  plt.grid()
  plt.show()


# In[ ]:


def proyecciones_poblacion_cobertura_salud(df, modelo_salud, features_escaladas_salud, modelo_poblacion, features_escaladas):
  # Se asignas las predicciones a cada fila del conjunto de datos unificado
  df['proyeccion_poblacion_municipio'] = modelo_poblacion.predict(features_escaladas)
  df['proyeccion_cobertura_salud'] = modelo_salud.predict(features_escaladas_salud)

  resultados_proyecciones = df.groupby('ano').agg({
                                      'total_poblacion_municipio':'sum',
                                      'proyeccion_poblacion_municipio':'sum',
                                      'porcentaje_poblacion_rural':'mean',
                                      'cobertura_salud':'mean',
                                      'proyeccion_cobertura_salud':'mean'
                                      }).reset_index()
  print(resultados_proyecciones)

