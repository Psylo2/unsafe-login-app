# from flask_sqlalchemy import SQLAlchemy
# 
# 
# db = SQLAlchemy()

import sqlite3
from typing import List

connection = sqlite3.connect("login.db", check_same_thread=False)

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    email TEXT,
    blocked INTEGER
);"""

CREATE_PASSWORDS_TABLE = """CREATE TABLE IF NOT EXISTS passwords (
    username TEXT,
    password_current TEXT,
    password_1 TEXT,
    password_2 TEXT,
    password_3 TEXT,
    password_4 TEXT,
    password_5 TEXT,
    password_6 TEXT,
    password_7 TEXT,
    password_8 TEXT,
    password_9 TEXT,
    password_10 TEXT,
    FOREIGN KEY(username) REFERENCES users(username)
);"""

INSERT_USER = "INSERT INTO users (username, email, blocked) VALUES (?, ?, ?);"

INSERT_PASSWORD = "INSERT INTO passwords (username, password_current, password_1, password_3, password_4, password_5, password_6, password_7, password_8, password_9, password_10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"

SELECT_ALL_USERS = "SELECT * FROM users;"

SELECT_ALL_PASSWORDS = "SELECT * FROM passwords;"

SELECT_PASSWORD = "SELECT * FROM passwords WHERE username=(?);"

SELECT_USER = "SELECT * FROM users WHERE (?) IN (username, email);"

UPDATE_PASSWORD = "UPDATE passwords SET password_current = (?), password_1 = (?), password_2 = (?), password_3 = (?), password_4 = (?), password_5 = (?), password_6 = (?), password_7 = (?), password_8 = (?), password_9 = (?), password_10 = (?)  WHERE username=(?);"

BLOCK_USER = "UPDATE users SET blocked = (?)  WHERE (?) IN (username, email);"


def create_table() -> None:
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_PASSWORDS_TABLE)


def add_user(username: str, email: str, password: dict) -> None:
    with connection:
        connection.execute(INSERT_USER, (username, email))
        add_password(password)
        
        
 def add_password(password: dict): -> None:
        with connection:
            connection.execute(INSERT_PASSWORD, (password['username'], password['password_current'], password['password_1'],
                                                 password['password_2'], password['password_3'], password['password_4'], 
                                                 password['password_5'], password['password_6'], password['password_7'],
                                                 password['password_8'], password['password_9'], password['password_10']))
            

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

        
def get_password(name_email: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_PASSWORD, (name_email,))
        return cursor.fetchone()       
    
def get_all_passwords() -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_PASSWORDS)
        return cursor.fetchall()   
 
def update_user(password: dict) -> None:
    with connection:
        connection.execute(UPDATE_PASSWORD, ((password['password_current'], password['password_1'], password['password_2'],
                                                 password['password_3'], password['password_4'], password['password_5'],
                                                 password['password_6'], password['password_7'], password['password_8'],
                                                 password['password_9'], password['password_10'], password['username']))
        connection.commit()

        
def get_headers(database: str) -> List:
    with connection:
        cursor = connection.execute(f"select * from {database}")
        return list(map(lambda x: x[0], cursor.description))
