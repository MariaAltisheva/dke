import io
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as lite

def read_sqlite_table_clients():

    conn = lite.connect('db.sqlite3')
    cur = conn.cursor()

    def get_posts():
        cur.execute("SELECT count(*) as client_count from Клиент")
        print(cur.fetchall())
        # df = pd.read_sql_query("SELECT count(*) as client_count from Клиент", conn)
        # st.table(data=df)

    get_posts()

st.button('Клиенты', on_click=read_sqlite_table_clients())
st.button('Заказы клиентов')
st.button('Склад')
st.button('Поставщики')
st.button('Заказы поставщикам')
st.button('Назад')
