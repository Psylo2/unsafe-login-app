# from flask_sqlalchemy import SQLAlchemy
# 
# 
# db = SQLAlchemy()

import sqlite3

connection = sqlite3.connect("login.db", check_same_thread=False)

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT
);"""

INSERT_USER = "INSERT INTO users (username, password) VALUES (?, ?);"

SELECT_ALL_USERS = "SELECT * FROM users;"

SELECT_USER = "SELECT * FROM users WHERE username = (?);"


def create_table():
    with connection:
        connection.execute(CREATE_USERS_TABLE)


def add_user(username, password):
    with connection:
        connection.execute(INSERT_USER, (username, password))


def get_user_by_name(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (username,))
        return cursor.fetchone()
