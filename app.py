import io
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as lite

st.title('Интернет-магазин продуктов')

st.sidebar.title('Выберите нужную опцию')

import io
import streamlit as st
import pandas as pd
import numpy as np
import sqlite3 as lite

def read_sqlite_table():

    conn = lite.connect('db.sqlite3')
    cur = conn.cursor()

    def get_posts():
        cur.execute("SELECT * FROM Заказ_клиента")
        print(cur.fetchall())
        df = pd.read_sql_query("SELECT * FROM Заказ_клиента", conn)
        st.table(data=df)

    get_posts()



st.button('Просмотр баз данных', on_click=read_sqlite_table)
st.button('Создать заказ клиента')
st.button('Редактировать заказ клиента')
st.button('Создать отчет по продажам')
st.button('Создать запрос на поставку')
st.button('Создать отчет по закупкам')
st.button('Выход')


