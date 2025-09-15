from re import match
import sqlite3
# usernames validator

def username_validator(username):
    if match(r"^[a-zA-Z\d]{10,20}$", username):
        return username
    else:
        raise ValueError("Invalid Username")

# password validator

def password_validator(password):
    if match(r"^[a-zA-Z\d$#@]{8,14}$", password):
        return  password
    else:
        raise ValueError("Invalid Password")

# nickname validator

def nickname_validator(nickname):
    if match(r"^[a-zA-Z\d\s]{3,30}$", nickname):
        return nickname
    else:
        raise ValueError("Invalid Nickname")

# Save User

def save_user(username, password, nickname, lock_state):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute(""" insert into users (username, password, nickname, lock_state) values (?, ?, ?, ?)""",
    [username, password, nickname ,lock_state])
    connection.commit()
    connection.close()









