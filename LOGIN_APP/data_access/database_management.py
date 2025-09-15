import sqlite3
def create_table_users():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("""create table users(id integer primary key autoincrement,
    username text,
    password text,
    nickname text,
    lock_state integer)""")
    connection.commit()

    connection.close()

