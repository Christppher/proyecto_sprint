# Importamos las librerías necesarias
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(layout="wide")

# Título principal de la aplicación
st.title("Análisis de Datos de Vehículos en Venta")

st.write("Esta aplicación interactiva te permite explorar un conjunto de datos de anuncios de venta de coches en EE. UU. Puedes generar visualizaciones para entender mejor las características de los vehículos.")

# Leemos el archivo CSV. 
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encontró. Por favor, asegúrate de que el archivo está en la misma carpeta que la aplicación.")
    st.stop() # Detiene la ejecución si el archivo no se encuentra

# Creamos el encabezado para la sección de visualización
st.header("Visualización de Datos")

# --- Histograma de Odómetro ---
st.subheader("Distribución del Odómetro")
st.write("Haz clic en el botón para generar un histograma que muestra la distribución del kilometraje (odómetro) de los vehículos.")

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creando un histograma para el conjunto de datos de anuncios de venta de coches...')
    
    # Creamos la figura del histograma
    fig_hist = go.Figure(data=[go.Histogram(x=df['odometer'])])
    
    # Actualizamos el diseño del gráfico
    fig_hist.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Frecuencia (número de vehículos)'
    )
    
    # Mostramos el gráfico en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)

# --- Gráfico de Dispersión: Odómetro vs. Precio ---
st.subheader("Relación entre Odómetro y Precio")
st.write("Marca la casilla para generar un gráfico de dispersión y analizar la relación entre el precio y el kilometraje.")

# Checkbox para construir el gráfico de dispersión
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersión')

if scatter_checkbox:
    st.write('Creando un gráfico de dispersión para odómetro vs. precio...')
    
    # Creamos la figura del gráfico de dispersión
    fig_scatter = go.Figure(data=go.Scatter(
        x=df['odometer'],
        y=df['price'],
        mode='markers', # Usamos puntos para el gráfico de dispersión
        marker=dict(
            size=5,
            color=df['price'], # Coloreamos los puntos según el precio
            colorscale='Viridis', # Escala de color
            showscale=True,
            colorbar_title="Precio (USD)"
        )
    ))
    
    # Actualizamos el diseño del gráfico
    fig_scatter.update_layout(
        title='Odómetro vs. Precio',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )
    
    # Mostramos el gráfico en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)