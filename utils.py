#!/usr/bin/env python
# coding: utf-8

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




