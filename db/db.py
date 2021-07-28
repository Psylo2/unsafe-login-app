# from flask_sqlalchemy import SQLAlchemy
# 
# 
# db = SQLAlchemy()

import sqlite3

connection = sqlite3.connect("login.db", check_same_thread=False)

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    email TEXT,
    blocked INTEGER
);"""

INSERT_USER = "INSERT INTO users (username, email, password, blocked) VALUES (?, ?, ?, ?);"

SELECT_ALL_USERS = "SELECT * FROM users;"

SELECT_USER = "SELECT * FROM users WHERE (?) IN (username, email);"

UPDATE_PASSWORD = "UPDATE users SET password=(?)  WHERE (?) IN (username, email);"

BLOCK_USER = "UPDATE users SET blocked=(?) WHERE username=(?);"


def create_table() -> None:
    with connection:
        connection.execute(CREATE_USERS_TABLE)


def add_user(username: str, email: str, password: str) -> None:
    with connection:
        connection.execute(INSERT_USER, (username, email, password))


def block_user(name_email: str, block_mode: int) -> None:
    with connection:
        connection.execute(BLOCK_USER, (block_mode, name_email))


def get_user(name_email: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_USER, (name_email,))
        return cursor.fetchone()


def get_all_users() -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_USERS)
        return cursor.fetchall()


def update_user(name_email: str, password: str) -> None:
    with connection:
        connection.execute(UPDATE_PASSWORD, (name_email, password))
        connection.commit()
