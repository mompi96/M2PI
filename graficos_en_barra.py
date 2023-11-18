import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Función para cargar el archivo CSV
def cargar_archivo_csv(ruta):
    try:
        datos = pd.read_csv(ruta)
        return datos
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Ruta del archivo CSV
ruta_archivo = 'hurtotransporte.csv'  # Reemplaza con la ruta de tu archivo CSV

# Cargar el archivo CSV
datos = cargar_archivo_csv(ruta_archivo)

# Tomar una muestra de 200 datos de cada fila y columna
if datos is not None:
    datos_muestra = datos.apply(lambda x: x.sample(n=200))

    st.title("Visualización de muestra de 200 datos por fila y columna desde un archivo CSV")
    st.write(datos_muestra.head())

    st.subheader("Visualización de datos")
    
    # Gráfico de barras con Seaborn
    st.write("Gráfico de barras:")
    columna_barplot = st.selectbox("Selecciona la columna para el gráfico de barras", datos_muestra.columns)
    fig_barplot, ax_barplot = plt.subplots()
    barplot = sns.countplot(x=columna_barplot, data=datos_muestra, ax=ax_barplot)
    st.pyplot(fig_barplot)

    # Gráfico de dispersión con Seaborn
    st.write("Gráfico de dispersión:")
    scatter_x = st.selectbox("Selecciona la columna para el eje X", datos_muestra.columns)
    scatter_y = st.selectbox("Selecciona la columna para el eje Y", datos_muestra.columns)
    fig_scatter, ax_scatter = plt.subplots()
    scatter_plot = sns.scatterplot(x=scatter_x, y=scatter_y, data=datos_muestra, ax=ax_scatter)
    st.pyplot(fig_scatter)
