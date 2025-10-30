# health_education_data - Análisis de datos públicos de salud y educación en Boyacá, Colombia

## Descripción del proyecto
Este proyecto tiene como objetivo buscar correlaciones de la cobertura de salud y educación en zonas rurales de difícil acceso en el departamento de Boyacá. Esto con el fin de poder identificar zonas vulnerables y proponer planes de acción que permitan mejorar la calidad de vida de los habitantes de las zonas identificadas.

El análisis incluye procesos de limpieza de datos, transformación, análisis exploratorio, clustering, dashboard interactivo, y modelos predictivos implementados en Python.

---

## Objetivos
- Integrar bases de datos públicas de salud y educación.
- Identificar características demográficas clave.
- Analizar correlaciones.
- Clasificar poblaciones mediante técnicas de clustering.
- Desarrollar modelos de predicción para variables poblacionales.
- Generar conclusiones accionables.

---

## Fuentes de datos
Los datos utilizados provienen del portal oficial de datos abiertos del Gobierno de Colombia:

| Conjunto de datos                 | Fuente oficial                                                                                                               |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Afiliaciones al Sistema de Salud | https://www.datos.gov.co/Salud-y-Protecci-n-Social/Afiliaci-n-al-Sistema-General-de-Seguridad-Social-/vdtf-vxs4/about_data    |                               |
| Centros poblados                 | https://www.datos.gov.co/Vivienda-Ciudad-y-Territorio/POBLACI-N-DE-LOS-DIFERENTES-CENTROS-POBLADOS-EN-LO/seua-4ze8/about_data |                            |
| Instituciones educativas         | https://www.datos.gov.co/Educaci-n/Sedes-de-Instituciones-Educativas-ubicadas-en-zona/eb5n-rfw8/about_data                    |         |

Los archivos fueron descargados manualmente y ubicados en la carpeta data/, con excepción del archivo Afiliaciones.csv, el cual no fue incluido debido a su tamaño. Este archivo puede descargarse desde el enlace oficial proporcionado en la sección de fuentes de datos.

---

## Tecnologías utilizadas
- **Python 3.x**
- **Pandas, NumPy** (procesamiento de datos)
- **Matplotlib, Seaborn** (visualización)
- **Scikit-learn** (modelos de machine learning)
- **Google Colab** como entorno de ejecución

---

## Estructura del repositorio

```text
health_education_data/
├── data/                                     # Carpeta con los datos del proyecto
│   ├── df_afiliaciones.csv                   # Datos de afiliación al sistema de salud
│   ├── df_centros_poblados.csv               # Datos de población por municipio
│   ├── df_ie.csv                             # Datos de instituciones educativas
│   └── df_unificado.csv                      # Dataset final integrado y listo para análisis/dashboard
├── dashboard/                                # Carpeta para el dashboard de Power BI
│   └── (archivo.pbix)                        # Dashboard interactivo de visualización
├── clustering.py                              # Código para segmentación de datos
├── config.py                                  # Variables globales de configuración
├── data_loader.py                             # Funciones para cargar, validar y mostrar datos
├── preprocess.py                              # Limpieza, estandarización y transformación del dataset
├── predictions.py                             # Modelos predictivos y validación de resultados
├── utils.py                                   # Funciones auxiliares reutilizables
├── visualizations.py                          # Gráficos y reportes visuales generados en Python
├── main.ipynb                                 # Notebook principal donde se ejecuta el flujo del proyecto
├── requirements.txt                           # Dependencias necesarias para reproducir el entorno
├── .gitignore                                 # Archivos y carpetas excluidos del repositorio
└── README.md                                  # Documentación general del proyecto
```

---

## Cómo ejecutar el proyecto

### 1. Descargar archivo faltante (requerido)
El archivo df_afiliaciones.csv no se incluye en el repositorio debido a su tamaño (>100 MB).
Debe ser descargado manualmente desde la fuente oficial y ubicado en la carpeta data/.

**Fuente oficial:**
https://www.datos.gov.co/Salud-y-Protecci-n-Social/Afiliaci-n-al-Sistema-General-de-Seguridad-Social-/vdtf-vxs4/about_data

**Instrucciones**

    1. Descargar el archivo en formato CSV.
    2. Guardarlo con el nombre df_afiliaciones.csv.
    3. Colocarlo dentro de la ruta:health_education_data/data/


### 2. Clonar el repositorio
git clone https://github.com/jolufr/health-education-data.git
cd health-education-data


### 3. Crear entorno virtual (opcional pero recomendado)
\`\`\`bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\\Scripts\\activate      # En Windows
\`\`\`

### 4. Instalar dependencias
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 5. Ejecutar el proyecto
\`\`\`bash
python main.py
\`\`\`

---

## Conclusiones y oportunidades estratégicas

- **Número total de registros analizados**: superior a 2 millón de registros combinados..
    - **Cobertura sistema de salud**: 2.370.000 registros.
    - **Centros poblados**: 1845 registros.
    - **Instituciones educativas**: 1685 registros.
- **Correlaciones encontradas**: no se halló correlación en la cobertura del sistema de salud con y la cobertura de educación.
- **Segmentos identificados mediante clustering**: 4 grupos diferenciados por acceso a servicios de salud y cobertura educativa.
- **Modelo predictivo aplicado**: Regresión lineal con un R² de 0.94 para estimar población y un R² de 0.71 para estimar la cobertura del sistema de salud. 

El análisis evidencia retos estructurales en desarrollo rural, conectividad y acceso a servicios básicos. Para impulsar el crecimiento sostenible del departamento, se identifican las siguientes oportunidades:

- **Turismo sostenible**: potencial para fortalecer el ecoturismo gracias a la baja urbanización y la riqueza natural del territorio.
- **Agricultura tecnificada y agroindustria**: disponibilidad de suelo para cultivos extensivos y para crear cadenas de valor que transformen productos primarios.
- **Energías renovables**: condiciones ideales para proyectos solares, eólicos y de biomasa debido a la baja densidad poblacional.

Estas estrategias podrían mejorar la calidad de vida, generar empleo formal y dinamizar la economía regional de forma sostenible.


---

## Dashboard en Power BI

El dashboard mostrará:

- Población total por municipio
- Niveles de cobertura por municipio.
- Comparativo rural vs urbano.
- Municipios y cobertura de salud y educación.
- Veredas y cobertura de salud y educación.

El archivo .pbix será añadido en la carpeta `/dashboard/` una vez esté desarrollado.

---

## 👨‍💻 Autor
**José Luis Fernández Rubiano**  
Científico de Datos

---

## Licencia
Este proyecto se encuentra bajo la licencia MIT. Puedes usarlo libremente citando la fuente original.
