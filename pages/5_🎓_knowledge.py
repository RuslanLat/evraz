import streamlit as st
from PIL import Image
import psycopg2
import pandas as pd
import numpy as np

st.set_page_config(page_title="База знаний", page_icon="🎓", layout="wide")

# загрузка конфигурации доступа к базе данных в облаке
with open('DATABASE_URL.txt', 'r') as f:
    DATABASE_URL = f.read()
# создание подключения к базе данны
connect = psycopg2.connect(DATABASE_URL)
# создание объекта курсора подключения к базе данных
cursor = connect.cursor()

cursor.execute("SELECT exhauster_name FROM blm.exhausters;")
exhauster_names = cursor.fetchall()

cursor.execute("SELECT mechanism_name, signal_name, mark_name, measuring_name, \
                       exhauster_name, place, type, comment, active\
                FROM blm.mapping_signals \
                INNER JOIN blm.mechanisms USING(mechanism_id) \
                INNER JOIN blm.signals USING(signal_id) \
                INNER JOIN blm.marks USING(mark_id) \
                INNER JOIN blm.measurings USING(measuring_id) \
                INNER JOIN blm.signal_settings AS sig USING(signal_settings_id) \
                INNER JOIN blm.exhausters AS ex ON sig.exhauster =  ex.exhauster_id;")
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=[_.name for _ in cursor.description])

col1, col2 = st.columns(2)
col1.write("""<p><img src="https://www.tadviser.ru/images/f/f1/EVRAZ_Logo_2022.png" width="250" height="80" align="middle" /> </p>""", unsafe_allow_html=True)    
col2.write("""<h1> База знаний </h1>""", unsafe_allow_html=True)

st.write("## Что такое эксгаустер! ⚙️")

# Контекст

st.markdown("""Агломерационная машина предназначена для окускования железных руд и концентратов для доменной плавки путем их спекания на аглоленте под разрежением создаваемым эксгаустерами.

В промежутке между верхними и нижними направляющими агломашины смонтированы пирамидальной формы вакуум-камеры, соединённые при помощи газохода с дымососом (**эксгаустером**). Эксгаустер создает область пониженного давления в вакуум-камерах, под действием которого через всю площадь палет, находящихся на верхнем горизонтальном участке, в агломерируемый слой засасывается вначале горячий газ (из зажигательного горна), а затем на остальной части машины — воздух . Далее газ выбрасывается через дымовую трубу в атмосферу. Таким образом агломерат пропекается внутри и становится пригодным для дальнейшей обработки в доменной печи. Эксгаустер состоит из двигателя, редуктора и ротора.""")

st.image(Image.open('images/sinter_machine.png'), caption='Упрощенное устройство агломашины')

st.video("https://www.youtube.com/watch?v=Y8iTNMh0pNE")
st.caption("<center> Что такое эксгаустер агломашины? </center>", unsafe_allow_html=True)

st.write("Маппинг сигналов эксгаустеров")
col1, col2, col3, col4 = st.columns(4)
exhauster_names = col1.radio("Эксгаустер", options=df['exhauster_name'].unique(), index=0)
if exhauster_names: 
    index_exhauster_names = np.where(df['exhauster_name'] == exhauster_names)
    index_filter = set(index_exhauster_names[0])
    df_plot = df.iloc[list(index_filter)]
    st.write(df_plot)

# закрытие подключения к базе данных 'postgres'
connect.close()

st.markdown("<h5 style='text-align: center; color: blac;'> ©️ Команда 40+ </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: blac;'> Хакатон ЕВРАЗа 2.0 </h5>", unsafe_allow_html=True)