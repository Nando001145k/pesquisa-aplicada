import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Dashboard PRF & INMET - PB", layout="wide"
)

st.title(" Análise Integrada: PRF & INMET (Foco: Paraíba)")


# Função para carregar os dados já limpos e leves
@st.cache_data
def load_data():
    df_prf = pd.read_csv("prf_pb_leve.csv", low_memory=False)
    df_inmet = pd.read_csv("inmet_pb_leve.csv", low_memory=False)
    return df_prf, df_inmet


df_prf, df_inmet = load_data()

st.success(
    f"Dados carregados e prontos para análise! Ocorrências PRF: {len(df_prf)} | Registos INMET: {len(df_inmet)}"
)

st.write("Amostra dos dados da PRF (Paraíba):")
st.dataframe(df_prf.head())

st.write("Amostra dos dados do INMET (Paraíba):")
st.dataframe(df_inmet.head())