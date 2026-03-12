import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Análisis de vehículos")

df = pd.read_csv('vehicles_us (1).csv')
st.write(df.head())


st.header("Histograma del precio")

hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Histograma del precio")
    fig = px.histogram(df, x="price")
    st.plotly_chart(fig)

scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Gráfico de dispersión: odómetro vs precio")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)
    