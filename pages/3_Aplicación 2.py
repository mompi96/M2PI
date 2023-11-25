import pandas as pd
import streamlit as st
import seaborn as sns
import plotly.express as px

def cargar_archivo_csv(ruta):
    try:
        datos = pd.read_csv(ruta)
        return datos
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

# Ruta del archivo CSV
ruta_archivo = 'hurtotransporte.csv'

# Cargar datos
datos = cargar_archivo_csv(ruta_archivo)

# Verificar si los datos se cargaron correctamente
if datos is not None:
    # Tomar una muestra de 200 datos de cada fila y columna
    datos_muestra = datos.sample(n=200)

    # Visualización de la muestra de datos
    st.title("Visualización de muestra de 200 datos por fila y columna desde un archivo CSV")
    st.write(datos_muestra.head())

    # Visualización de datos exploratorios
    st.subheader("Visualización de datos exploratorios")

    # Verificar nombres de las columnas
    st.write("Nombres de las columnas:", datos.columns)

    # Verifica si 'Tipo_Transporte' está en las columnas
    if 'Tipo_Transporte' in datos.columns:
        # Gráfico de barras para contar la cantidad de hurtos por tipo de transporte
        tipo_transporte_counts = datos['Tipo_Transporte'].value_counts()
        st.bar_chart(tipo_transporte_counts)
    else:
        st.error("La columna 'Tipo_Transporte' no se encuentra en los datos.")

    # Crear datos de ejemplo
    data = {'Categoría': ['A', 'B', 'C', 'D'],
            'Valor': [20, 50, 37, 18]}
    df = pd.DataFrame(data)

    # Gráfico de pastel interactivo con márgenes
    fig_pie = px.pie(df, values='Valor', names='Categoría', hole=0.5,
                     title='Gráfico de Pastel Interactivo con Márgenes')

    # Ajustar márgenes utilizando update_layout
    fig_pie.update_layout(margin=dict(l=20, r=20, t=20, b=20))

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_pie)