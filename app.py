import streamlit as st
import pandas as pd
import plotly.express as px

# Estabelcimiento de encabezados
st.title('Bienvenido a mi Aplicación de Análisis de Vehículos')
st.header('Histograma de Odómetro de Vehículos en USA')
st.subheader('A continuación por favor selecciona lo que deseas visualizar')

#Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para el histograma
hist_checkbox = st.checkbox('Mostrar histograma')
        
if hist_checkbox:  # Si se selecciona la casilla del histograma
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Casilla de verificación para el gráfico de dispersión
scatter_checkbox = st.checkbox('Mostrar gráfico de dispersión')

if scatter_checkbox:  # Si se selecciona la casilla del gráfico de dispersión
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para la relación entre el precio y el odómetro')

    # Crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") 

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
