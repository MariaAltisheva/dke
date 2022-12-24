# import io
# import streamlit as st
# import pandas as pd
# import numpy as np
# import sqlite3 as lite
#
# def read_sqlite_table_clients():
#
#     conn = lite.connect('db.sqlite3')
#     cur = conn.cursor()
#
#     def get_posts():
#         # cur.execute("SELECT count(*) as client_count from Клиент")
#         # print(cur.fetchall())
#         df = pd.read_sql_query("SELECT count(*) as client_count from Клиент", conn)
#         st.table(data=df)
#
#     get_posts()
#
# st.button('Клиенты', on_click=read_sqlite_table_clients())
# st.button('Заказы клиентов')
# st.button('Склад')
# st.button('Поставщики')
# st.button('Заказы поставщикам')
# st.button('Назад')


import sqlite3
import pandas as pd
import streamlit as st


try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)


def clients():
    sqlite_select_query = "SELECT * from Клиент;"
    query = cursor.execute(sqlite_select_query)
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    st.table(data=results)


def goods():
    sqlite_select_query = "SELECT * from Товар;"
    query = cursor.execute(sqlite_select_query)
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    st.table(data=results)


def storage():
    sqlite_select_query = "SELECT * from Склад;"
    query = cursor.execute(sqlite_select_query)
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    st.table(data=results)


def orders():
    sqlite_select_query = "SELECT * from Заказ_клиента;"
    query = cursor.execute(sqlite_select_query)
    cols = [column[0] for column in query.description]
    results = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    st.table(data=results)


st.button('Просмотр товаров', on_click=goods)
st.button('Просмотр клиентов', on_click=clients)
st.button('Просмотр склада', on_click=storage)
st.button('Просмотр заказов', on_click=orders)
