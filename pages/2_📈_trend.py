import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import psycopg2
import urllib.parse as up
import base64
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb
import altair as alt

eksgauster = ' 🟢 Эксгаустер У-171'

st.set_page_config(page_title="Тренд сигналов", page_icon="⚙️", layout="wide")

col1, col2 = st.columns([1,3])
col1.write("""<p><img src="https://www.tadviser.ru/images/f/f1/EVRAZ_Logo_2022.png" width="200" height="50" align="middle" /> </p>""", unsafe_allow_html=True)    
col2.write(f"""<h3>Мониторинг состояния {eksgauster}</h3>""", unsafe_allow_html=True)

@st.cache
def to_excel(df):
    
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='SQL Query')
    workbook = writer.book
    worksheet = writer.sheets['SQL Query']
    format1 = workbook.add_format({'num_format': '0.00'}) 
    worksheet.set_column('A:A', None, format1)  
    writer.save()
    processed_data = output.getvalue()
    
    return processed_data

def to_csv(df):

    return df.to_csv(index=False).encode('utf-8')

with open('DATABASE_URL_3.txt', 'r') as f:
    DATABASE_URL = f.read()

# создание подключения к базе данны
connect = psycopg2.connect(DATABASE_URL)

# создание объекта курсора подключения к базе данных
cursor = connect.cursor()

cursor.execute("""SELECT moment, sm_exgauster_0_169, sm_exgauster_0_170, sm_exgauster_0_171
                FROM blm.moment_signals;""")
rows = cursor.fetchall()

# преобразование в DataFrame
#st.markdown("<h3 style='text-align: left; color: blac;'> Результат запроса </h3>", unsafe_allow_html=True)
df = pd.DataFrame(rows, columns=[_.name for _ in cursor.description])
#st.write(df, height=200)
df_xlsx = to_excel(df)
df_csv = to_excel(df)

st.markdown("<h6 style='text-align: right; color: blac;'> Экспорт данных </h6>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([21, 1, 1])
col2.download_button(label='XLSX', data=df_xlsx, file_name='sql_query.xlsx')
col3.download_button(label='CSV', data=df_csv, file_name='large_df.csv', mime='text/csv')

col1, col2= st.columns([1,7])

col1.selectbox('Эксгаустер',
('Эксгаустер У-171', 'Эксгаустер У-172', 'Эксгаустер У-173', 'Эксгаустер У-174', 'Эксгаустер У-175', 'Эксгаустер У-176'), index=3, key='selectbox3')

min_date = datetime.date(2023,1,1)
max_date = datetime.date(2023,1,2)

col1.date_input("Временной диапазон", (min_date, max_date))

with col1:
    st.write("Выбор параметров")
    with st.expander("Adjust test parameters"):
        st.markdown("### Parameters")
        st.radio(
                "Hypothesis type",
                options=["One-sided", "Two-sided"],
                index=0,
                key="hypothesis",
                help="TBD",
            )
    with st.expander("Adjust test parameters"):
        st.markdown("### Parameters")
        st.radio(
                "Hypothesis type",
                options=["One-sided", "Two-sided"],
                index=0,
                key="hypothesis",
                help="TdBD",
            )
#if param:
#index_ship_modes = np.where(df['ship_mode_id'].isin(ship_modes))
#index_geos = np.where(df['geo_id'].isin(geos))
#index_filter = set(index_ship_modes[0]) & set(index_geos[0])
#df_plot = df.iloc[list(index_filter)]

chart_data = pd.melt(df, id_vars=['moment'], value_vars=['sm_exgauster_0_169', 'sm_exgauster_0_170', 'sm_exgauster_0_171'])
chart_data = chart_data.groupby(['moment', 'variable'], as_index=False)['value'].sum()
chart_data['value'] = chart_data['value'].astype('float') 
#chart_data[['sm_exgauster_0_169', 'sm_exgauster_0_170', 'sm_exgauster_0_171']] = chart_data[['sm_exgauster_0_169', 'sm_exgauster_0_170', 'sm_exgauster_0_171']].astype('float')
st.write(chart_data)
#col2.line_chart(chart_data)
c = alt.Chart(chart_data).mark_line().encode(
x='moment:T',
y='value:Q',
color='variable:N')



col2.altair_chart(c, use_container_width=True)