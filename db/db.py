from db.queries import (sqlite3, CREATE_USERS_TABLE, CREATE_PASSWORDS_TABLE,
                        BLOCK_USER, INSERT_PASSWORD, INSERT_USER,
                        SELECT_ALL_PASSWORDS, SELECT_ALL_USERS, SELECT_PASSWORD,
                        SELECT_USER, UPDATE_PASSWORD)
from typing import List

connection = sqlite3.connect("login.db", check_same_thread=False)


def create_tables() -> None:
    with connection:
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_PASSWORDS_TABLE)


# def add_user(username: str, email: str, password: dict) -> None:
#     with connection:
#         connection.execute(INSERT_USER, (username, email))
#         add_password(password)

def add_user(username: str, email: str, password: str, blocked: int) -> None:
    with connection:
        connection.execute(INSERT_USER, (username, email, password, blocked))


def add_password(password: dict) -> None:
    with connection:
        connection.execute(INSERT_PASSWORD,
                           (password['username'], password['password_current'], password['password_1'],
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


def get_password(username: str) -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_PASSWORD, (username,))
        return cursor.fetchone()


def get_all_passwords() -> connection.cursor():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_PASSWORDS)
        return cursor.fetchall()


def update_password(password: dict) -> None:
    with connection:
        connection.execute(UPDATE_PASSWORD,
                           (password['password_current'], password['password_1'], password['password_2'],
                            password['password_3'], password['password_4'], password['password_5'],
                            password['password_6'], password['password_7'], password['password_8'],
                            password['password_9'], password['password_10'], password['username']))
        connection.commit()


def get_headers(database: str) -> List:
    with connection:
        cursor = connection.execute(f"select * from {database};")
        return list(map(lambda x: x[0], cursor.description))
