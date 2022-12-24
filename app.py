import io
import sqlite3
import streamlit as st

st.title('Интернет-магазин продуктов')

st.sidebar.title('Выберите нужную опцию')

st.button('Просмотр баз данных')
st.button('Создать заказ клиента')
st.button('Редактировать заказ клиента')
st.button('Создать отчет по продажам')
st.button('Создать запрос на поставку')
st.button('Создать отчет по закупкам')
st.button('Выход')
