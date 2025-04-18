import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

df = pd.read_csv("static/datasets/estudiantes_colombia.csv")

st.markdown('<h4 margin-top: 0px;">Primeras 5 filas:</h3>', unsafe_allow_html=True)
st.dataframe(df.head())

st.markdown('<h4 margin-top: 0px;">Últimas 5 filas:</h3>', unsafe_allow_html=True)
st.dataframe(df.tail())

st.markdown('<h4 margin-top: 0px;">Columnas especificas:</h3>', unsafe_allow_html=True)
st.dataframe(df[["nombre", "edad", "promedio"]])

st.markdown('<h4 margin-top: 0px;">Por promedio:</h3>', unsafe_allow_html=True)
min_promedio = float(df["promedio"].min())
max_promedio = float(df["promedio"].max())

# Crear slider
umbral = st.slider(
    "Mostrar estudiantes con promedio mayor a:",
    min_value=min_promedio,
    max_value=max_promedio,
    value=min_promedio,
    step=0.1
)

# Filtrar DataFrame
df_filtrado = df[df["promedio"] > umbral]

# Mostrar resultado
st.write(f"Estudiantes con promedio mayor a {umbral}:")
st.dataframe(df_filtrado)

