import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import matplotlib.pyplot as plt
#from datetime import datetime
#import time

st.set_page_config(page_title="Мониторинг состояния", page_icon="📈", layout="wide")

col1, col2 = st.columns([1,3])
col1.write("""<p><img src="https://www.tadviser.ru/images/f/f1/EVRAZ_Logo_2022.png" width="250" height="80" align="middle" /> </p>""", unsafe_allow_html=True)    
col2.write("""<h1>Мониторинг состояния эксгаустеров агломашины</h1>""", unsafe_allow_html=True)

#t = st.empty()
#while True:
#    t.write(datetime.now().time())
#    time.sleep(1)
#st.write(datetime.now().time())

st.write("""<h6 align="right">🌡 - Температура 🎚 - Уровень масла 💤- Вибрация 🟢 - Норма 🟡 - Предупреждение 🔴 - Опасность</h6>""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.write('<h4 align="center">Агломашина №1</h4>', unsafe_allow_html=True)
col2.write('<h4 align="center">Агломашина №2</h4>', unsafe_allow_html=True)
col3.write('<h4 align="center">Агломашина №3</h4>', unsafe_allow_html=True)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #535353;color:white;font-size:15px;width:100%;
}
</style>""", unsafe_allow_html=True)


# функция задания цвета ячейки
def color_cell(data):
    """
    Получение цвета ячейки в зависимости от значения
    """
    if data > 10:
        return 'background-color: red'
    elif data > 5:
        return 'background-color: yellow'
    return "background-color: white"


df = pd.DataFrame([[0, 2, 8], [0, 15, 8], [3, 2, 7], [0, 5, 8], [4, 20, 8], [1, 2, 0]], \
                   index=['№1 п-к', '№2 п-к', '№3 п-к', '№4 п-к', '№5 п-к', 'Уровень масла'], \
                   columns=['🌡', '🎚', '💤']).style.applymap(color_cell)

df1 = pd.DataFrame([[0, 2, 80], [0, 6, 8], [3, 2, 7], [0, 5, 8], [4, 2, 8], [1, 2, 0]], \
                   index=['№1 п-к', '№2 п-к', '№3 п-к', '№4 п-к', '№5 п-к', 'Уровень масла'], \
                   columns=['🌡', '🎚', '💤']).style.applymap(color_cell)


col1, col2, col3, col4, col5, col6 = st.columns(6)
eksgauster1 = col1.button(' 🟢 Эксгаустер У-171')
col1.date_input('Ротор №35К', help='выберите дату') 
col1.metric(label='Последняя замена ротора', value="5 Суток", delta=None)
col1.metric(label='Плановая замена ротора', value="15 Суток", delta=None)
col1.metric(label="Прогноз замены ротора", value="70 Суток", delta="2 Суток", delta_color="inverse")
col1.image(Image.open('images/machine.png'))
option1 = col1.selectbox(
    'Мониторинг состояния',
    ('Предупреждения', 'Все подключения'), key='selectbox1')
if option1 == 'Предупреждения':
    col1.table(df)
else:
    col1.table(df1)
col1.button('Отправить заявку в SAP', key='button1')
col2.button(' 🟢 Эксгаустер У-172')
col2.date_input('Ротор №47', help='выберите дату')
col2.metric(label='Последняя замена ротора', value="10 Суток", delta=None)
col2.metric(label='Плановая замена ротора', value="15 Суток", delta=None)
col2.metric(label="Прогноз замены ротора", value="50 Суток", delta="2 Суток", delta_color="inverse")
col2.image(Image.open('images/machine.png'))
option2 = col2.selectbox(
    'Мониторинг состояния',
    ('Предупреждения', 'Все подключения'), key='selectbox2')
if option2 == 'Предупреждения':
    col2.table(df)
else:
    col2.table(df1)
col2.button('Отправить заявку в SAP', key='button2')
col3.button(' 🔴 Эксгаустер У-173')
col3.date_input('Ротор №37', help='выберите дату')
col3.metric(label='Последняя замена ротора', value="13 Суток", delta=None)
col3.metric(label='Плановая замена ротора', value="15 Суток", delta=None)
col3.metric(label="Прогноз замены ротора", value="10 Суток", delta="10 Суток", delta_color="inverse")
col3.image(Image.open('images/machine.png'))
option3 = col3.selectbox(
    'Мониторинг состояния',
    ('Предупреждения', 'Все подключения'), key='selectbox3')
if option3 == 'Предупреждения':
    col3.table(df)
else:
    col3.table(df1)
col3.button('Отправить заявку в SAP', key='button3')
col4.button(' 🔴 Эксгаустер У-174')
col4.date_input('Ротор №32', help='выберите дату')
col4.metric(label='Последняя замена ротора', value="1 Суток", delta=None)
col4.metric(label='Плановая замена ротора', value="15 Суток", delta=None)
col4.metric(label="Прогноз замены ротора", value="41 Суток", delta="7 Суток", delta_color="inverse")
col4.image(Image.open('images/machine.png'))
option4 = col4.selectbox(
    'Мониторинг состояния',
    ('Предупреждения', 'Все подключения'), key='selectbox4')
if option4 == 'Предупреждения':
    col4.table(df)
else:
    col4.table(df1)
col4.button('Отправить заявку в SAP', key='button4')
col5.button(' 🟢 Эксгаустер У-175')
col5.date_input('Ротор №24', help='выберите дату')
col5.metric(label='Последняя замена ротора', value="55 Суток", delta=None)
col5.metric(label='Плановая замена ротора', value="15 Суток", delta=None)
col5.metric(label="Прогноз замены ротора", value="0 Суток", delta="7 Суток", delta_color="inverse")
col5.image(Image.open('images/machine.png'))
option5 = col5.selectbox(
    'Мониторинг состояния',
    ('Предупреждения', 'Все подключения'), key='selectbox5')
if option5 == 'Предупреждения':
    col5.table(df)
else:
    col5.table(df1)
col5.button('Отправить заявку в SAP', key='button5')
col6.button(' 🔴 Эксгаустер У-176')
col6.date_input('Ротор №22 К', help='выберите дату')
col6.metric(label='Последняя замена ротора', value="15 Суток", delta=None)
col6.metric(label='Плановая замена ротора', value="15 Суток", delta=None)
col6.metric(label="Прогноз замены ротора", value="10 Суток", delta="17 Суток", delta_color="inverse")
col6.image(Image.open('images/machine.png'))
option6 = col6.selectbox(
    'Мониторинг состояния',
    ('Предупреждения', 'Все подключения'), key='selectbox6')
if option6 == 'Предупреждения':
    col6.table(df)
else:
    col6.table(df1)
col6.button('Отправить заявку в SAP', key='button6')

st.markdown("<h5 style='text-align: center; color: blac;'> ©️ Команда 40+ </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: blac;'> Хакатон ЕВРАЗа 2.0 </h5>", unsafe_allow_html=True)