# СУБД - Система Управления Базой Данных
# БД - База Данных

# import sqlite3

# def create_connection(db_name):
#     connectio = sqlite3.connect(db_name)
#     return connectio

# def create_table(connection, sql): # sql - входящий параметр для sql запроса
#     cursor = connection.cursor() # cursor - это некий посредник базы данных
#     cursor.execute(sql) # execute - отправляет запрос в базу данных


# sql_create_table = """
# CREATE TABLE IF NOT EXISTS students (
# id INTEGER PRIMERY KEY,
# full_name VARCHAR (100) NOT NULL,
# mark DOUBLE (5,2) NOT NULL DEFAULT 0.0,
# hobby TEXT DEFAULT NULL,
# birth_date DATE NOT NULL,
# is_passed BOOLEAN DEFAULT FALSE
# );
# """

# # INTEGER - int
# # VARCHAR - str (текст с ограничением)
# # TEXT - str (текст без ограничения)
# # DOUBLE - float
# # DATE - Дата
# # BOOLEAN - bool

# connection = create_connection("Geeks.db")

# create_table(connection, sql_create_table)