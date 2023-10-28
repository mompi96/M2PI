import streamlit as st
from PIL import Image, ImageDraw

# Agregar un selector de color
color_personalizado = st.color_picker("Selecciona un color personalizado")

# Función para dibujar un rombo de colores
def dibujar_rombo(color):
    # Crear una imagen de 100x100 píxeles con fondo transparente
    image = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
    
    # Dibujar un rombo del color seleccionado en la imagen
    draw = ImageDraw.Draw(image)
    draw.polygon([(50, 0), (100, 50), (50, 100), (0, 50)], fill=color)
    
    # Mostrar la imagen en Streamlit
    st.image(image, caption=f"Rombo personalizado", use_column_width=True)

# Configuración de la aplicación Streamlit
st.title("Generador de Rombo de Colores")
st.write("Selecciona un color personalizado y presiona el botón para generar un rombo del color seleccionado:")

if st.button("Generar Rombo"):
    dibujar_rombo(color_personalizado)
