# загрузка библиотек
import streamlit as st
import pandas as pd
import psycopg2
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
from PIL import Image

st.set_page_config(page_title='SQL Query', page_icon="🔍", layout="wide")

col1, col2 = st.columns([1,3])
col1.write("""<p><img src="https://www.tadviser.ru/images/f/f1/EVRAZ_Logo_2022.png" width="250" height="80" align="middle" /> </p>""", unsafe_allow_html=True)    
col2.write("""<h2 align="center"> Интерфейс доступа к данным состояния эксгаустеров агломашины </h2>""", unsafe_allow_html=True)

@st.cache
#def to_excel(df):
    
#    output = BytesIO()
#    writer = pd.ExcelWriter(output, engine='xlsxwriter')
#    df.to_excel(writer, index=False, sheet_name='SQL Query')
#    workbook = writer.book
#    worksheet = writer.sheets['SQL Query']
#    format1 = workbook.add_format({'num_format': '0.00'}) 
#    worksheet.set_column('A:A', None, format1)  
#    writer.save()
#    processed_data = output.getvalue()
    
#    return processed_data

def to_csv(df):

    return df.to_csv(index=False).encode('utf-8')

with open('DATABASE_URL.txt', 'r') as f:
    DATABASE_URL = f.read()

# создание подключения к базе данны
connect = psycopg2.connect(DATABASE_URL)

# создание объекта курсора подключения к базе данных
cursor = connect.cursor()

col1, col2 = st.columns(2)
col1.markdown("<h4 style='text-align: left; color: blac;'> SQL терминал </h4>", unsafe_allow_html=True) 
query = col1.text_area('', value="""SELECT mechanism_name, signal_name, mark_name, measuring_name, 
                       exhauster_name, place, type, comment, active
                FROM blm.mapping_signals 
                INNER JOIN blm.mechanisms USING(mechanism_id) 
                INNER JOIN blm.signals USING(signal_id) 
                INNER JOIN blm.marks USING(mark_id) 
                INNER JOIN blm.measurings USING(measuring_id) 
                INNER JOIN blm.signal_settings AS sig USING(signal_settings_id) 
                INNER JOIN blm.exhausters AS ex ON sig.exhauster =  ex.exhauster_id;""", height=300, help='введите SQL запрос, допустима операция только SELECT')
col2.write("""<h4>Логическая модель данных </h4>""", unsafe_allow_html=True)
col2.image(Image.open('images/data_model.png'))

#st.markdown("<h3 style='text-align: left; color: blac;'> SQL терминал </h3>", unsafe_allow_html=True)
#query = st.text_area('', value='SELECT * FROM blm.orders LIMIT 50;', height=200, help='введите SQL запрос, допустима операция только SELECT')

if query.split()[0].lower() == 'select':
                  
    st.success('Запрос принят')
    cursor.execute(query)
    rows = cursor.fetchall()

    # преобразование в DataFrame
    #st.markdown("<h3 style='text-align: left; color: blac;'> Результат запроса </h3>", unsafe_allow_html=True)
    df = pd.DataFrame(rows, columns=[_.name for _ in cursor.description])
    #st.write(df, height=200)
    #df_xlsx = to_excel(df)
    df_csv = to_excel(df)
    
    col1, col2 = st.columns([5,1])
    col1.markdown("<h4 style='text-align: left; color: blac;'> Результат запроса </h4>", unsafe_allow_html=True)
    col1.write(df, height=200)
    col2.markdown("<h4 style='text-align: left; color: blac;'> Экспорт данных </h4>", unsafe_allow_html=True)
    #col2.download_button(label='XLSX', data=df_xlsx, file_name='sql_query.xlsx')
    col2.download_button(label='CSV', data=df_csv, file_name='large_df.csv', mime='text/csv')

else:
    st.error('Допустима операция только SELECT')

# закрытие подключения к базе данных 'postgres'
#connect.close()

st.markdown("<h5 style='text-align: center; color: blac;'> ©️ Команда 40+ </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: blac;'> Хакатон ЕВРАЗа 2.0 </h5>", unsafe_allow_html=True)