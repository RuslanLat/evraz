import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ЕВРАЗ",
    page_icon="🏭",
    layout="wide")

col1, col2 = st.columns([1,3])
col1.write("""<p><img src="https://www.tadviser.ru/images/f/f1/EVRAZ_Logo_2022.png" width="150" height="50" align="middle" /> </p>""", unsafe_allow_html=True)    
col2.write("""<h3>Welcome to Хакатон ЕВРАЗа 2.0! 👋<h3>""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: left; color: blac;'> Проблема </h4>", unsafe_allow_html=True)

st.markdown("""В составе одной агломашины обычно работает два эксгаустера. Выход из строя хотя бы одного эксгаустера означает остановку агломашины, сокращение производства и вытекающие из этого денежные потери. 

1) За работой всей агломашины круглосуточно посменно следят агломератчики, в обязанности которых входит, например, визуальный контроль, контроль параметров и обслуживание агломашины. Оператор большую часть времени находится в производственном цеху и не может постоянно следить за параметрами агломашины. При достижении предельных значений по одному или нескольким параметрам агломератчик создает заявку на вызов специалиста для обслуживания агломашины. 

Отсюда возникает задача непрерывного мониторинга параметров агломашины, а именно эксгаустеров, для оперативного реагирования, автоматического создания заявок на обслуживание и накопления данных (логирования) для дальнейшей аналитики сбоев.

2) Износ ротора эксгаустера и выход его из строя носит нерегулярный характер, поэтому случаются незапланированные остановки агломашины. Обычно ротор эксгаустера требует замены один или два раза в месяц в зависимости от его изначального состояния. Но иногда срок его непрерывной работы  может быть и больше.

В это же время каждую неделю агломашину планово останавливают для проведения ремонтных работ. В этот момент есть возможность провести ремонт или замену ротора эксгаустера при необходимости.

Отсюда возникает задача определения даты замены ротора.""")

st.markdown("<h4 style='text-align: left; color: blac;'> Сервис для приема и сохранения потока данных с эксгаустера и предоставления интерфейса доступа к этим данным </h4>", unsafe_allow_html=True)

st.image(Image.open('images/solution_architecture.jpg'), caption='Архитектура аналитического решения')

st.image(Image.open('images/Cloud_SQL.png'), caption='База данных в облаке')

st.image(Image.open('images/data_model.png'), caption='Модель данных')

st.image(Image.open('images/sql_query.png'), caption='Интерфейс доступа к данным')

st.markdown("<h4 style='text-align: left; color: blac;'> Веб-интерфейс для рабочего места машиниста эксгаустера </h4>", unsafe_allow_html=True)

st.markdown("<h6 style='text-align: left; color: blac;'> Отображение текущего состояния всех эксгаустеров на одном экране </h6>", unsafe_allow_html=True)

st.image(Image.open('images/main_monitor.png'), caption='Состояние всех эксгаустеров')

st.markdown("<h6 style='text-align: left; color: blac;'> Визуализация детальных данных по конкретному эксгаустеру </h6>", unsafe_allow_html=True)

st.image(Image.open('images/monitor.jpg'), caption='Детальные данные эксгаустера')

st.markdown("<h6 style='text-align: left; color: blac;'> Визуализация потока данных во времени для анализа трендов </h6>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: left; color: blac;'> Разработка алгоритма определения даты замены ротора эксгаустера и отображение результатов его работы в веб-интерфейсе </h4>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: blac;'> ©️ Команда 40+ </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: blac;'> Хакатон ЕВРАЗа 2.0 </h5>", unsafe_allow_html=True)
#https://xn--80aaaairqt2ajzt9a.xn--p1ai/?utm_source=hacklist