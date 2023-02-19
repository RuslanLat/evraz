import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Модель эксгаустеров", page_icon="🔃", layout="wide")

col1, col2 = st.columns([1,3])
col1.write("""<p><img src="https://www.tadviser.ru/images/f/f1/EVRAZ_Logo_2022.png" width="250" height="80" align="middle" /> </p>""", unsafe_allow_html=True)    
col2.write("""<h2 align="center"> Модель эксгаустеров агломашины </h2>""", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: blac;'> ©️ Команда 40+ </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: blac;'> Хакатон ЕВРАЗа 2.0 </h5>", unsafe_allow_html=True)