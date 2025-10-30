#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd


# In[ ]:


# Carga de los datos de afiliaciones al sistema de salud
def load_afiliaciones(data_dir):
  path = os.path.join(data_dir, "Afiliaciones.csv")
  if not os.path.exists(path):
    raise(FileNotFoundError(f"El archivo {path} no existe. Asegurate de cargarlo primero"))
  return pd.read_csv(path, low_memory=False, sep=',')


# In[ ]:


# Carga de los datos centros poblados
def load_centros_poblados(data_dir):
  path = os.path.join(data_dir, "CentrosPoblados.csv")
  if not os.path.exists(path):
    raise(FileNotFoundError(f"El archivo {path} no existe. Asegurate de cargarlo primero"))
  return pd.read_csv(path, low_memory=False, sep=',')


# In[ ]:


# Carga de los datos instituciones educativas
def load_instituciones_educativas(data_dir):
  path = os.path.join(data_dir, "InstitucionesEducativas.csv")
  if not os.path.exists(path):
    raise(FileNotFoundError(f"El archivo {path} no existe. Asegurate de cargarlo primero"))
  return pd.read_csv(path, low_memory=False, sep=',')

