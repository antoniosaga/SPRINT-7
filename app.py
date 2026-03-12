import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Análisis de vehículos")

df = pd.read_csv('vehicles_us (1).csv')
st.write(df.head())


st.header("Histograma del precio")

fig = px.histogram(df, x="price")

st.plotly_chart(fig)