#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Librerias para graficar
import matplotlib.pyplot as plt
import seaborn as sns

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


# In[ ]:


def metodo_codo(df):
  # Seleccion de variables para clusterizacion
  var_cluster = df[['porcentaje_poblacion_rural', 'cobertura_salud']].copy()

  # Escalado de variables
  standar_cluster = StandardScaler()
  var_cluster_escaladas = standar_cluster.fit_transform(var_cluster)

  # Seleccion del mejor numero de clusters
  inertia = [] # Suma de las distancias a los centroides
  K_range = range(1, 10)

  for k in K_range:
    km = KMeans(n_clusters=k, random_state=21) # Defincion del modelo
    km.fit(var_cluster_escaladas) # Entrenamiento del modelo
    inertia.append(km.inertia_)


  plt.figure(figsize=(6, 4))
  plt.plot(K_range, inertia, 'o-')
  plt.xlabel('Numero de Clusters')
  plt.ylabel('Inertia')
  plt.title('Metodo del codo')
  plt.show()
  return var_cluster_escaladas


# In[ ]:


def visualizacion_clusters__poblacion_rural_cobertura_salud(df1, df2):
  # Eleccion del numero de clusters y predicciones
  kmeans = KMeans(n_clusters=4, random_state=21) # Creacion del modelo con el numero optimo de cluster
  df1['cluster'] = kmeans.fit_predict(df2) # Asignacion de cluster a cada fila

  # Visualizacion de clusters
  plt.figure(figsize=(8, 4))
  sns.scatterplot(
                x = 'porcentaje_poblacion_rural',
                y = 'cobertura_salud',
                hue = 'cluster',
                data = df1,
                palette = 'Set2',
                s = 100
                )

  plt.title('Clusters Poblacion Rural vs Cobertura Salud')
  plt.xlabel('Poblacion Rural (%)')
  plt.ylabel('Cobertura Salud (%)')
  plt.grid()
  plt.show()


# In[ ]:


#print(cluster_objetivo[['ano', 'municipio', 'porcentaje_poblacion_rural', 'cobertura_salud']].sort_values(by=['municipio']))

