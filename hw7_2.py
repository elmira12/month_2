# import sqlite3

# def create_connection(db_name):
#     connection = sqlite3.connect(db_name)
#     return connection


# def create_table(conn, sql):
#     cursor = conn.cursor()
#     cursor.execute(sql)



# sql_create_table = """
# CREATE TABLE IF NOT EXISTS product(
# id INTEGER PRIMARY KEY,
# product_title VARCHAR (200),
# price DOUBLE (6,3) NOT NULL DEFAULT 0.0,
# quantity INTEGER NOT NULL DEFAULT 0
# );
# """

# conn = create_connection("hw.db")
# create_table(conn, sql_create_table)