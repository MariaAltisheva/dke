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


try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
