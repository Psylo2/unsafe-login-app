# from flask_sqlalchemy import SQLAlchemy
# 
# 
# db = SQLAlchemy()

import sqlite3

connection = sqlite3.connect("login.db", check_same_thread=False)

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    email TEXT
);"""

INSERT_USER = "INSERT INTO users (username, email, password) VALUES (?, ?, ?);"

SELECT_ALL_USERS = "SELECT * FROM users;"

SELECT_USER = "SELECT * FROM users WHERE username = (?) OR email = (?);"


def create_table() -> None:
    with connection:
        connection.execute(CREATE_USERS_TABLE)


def add_user(username: str, email: str, password: str) -> None:
    with connection:
        connection.execute(INSERT_USER, (username, email, password))


def get_user(name_email: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (name_email,))
        return cursor.fetchone()
