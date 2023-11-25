import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Diseño personalizado
df = pd.read_csv('hurtotransporte.csv')

def cargar_archivo_csv(ruta):
    try:
        datos = pd.read_csv(ruta)
        return datos
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

ruta_archivo = 'hurtotransporte.csv'

datos = cargar_archivo_csv(ruta_archivo)

if datos is not None:

    datos_muestra = datos.apply(lambda x: x.sample(n=200))

    st.write("Filtro:")
    columna_barplot = st.selectbox("Selecciona la columna para el filtro:", datos_muestra.columns)


estadoCivil = df.loc[:,"cantidad"].unique()

option = st.selectbox('Fecha Hecho',estadoCivil)

st.header(option)

filtroEstadoCivil = df[df["cantidad"] == option]

st.write(filtroEstadoCivil.describe())