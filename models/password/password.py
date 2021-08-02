from dataclasses import dataclass, field
import re
from typing import Dict

from flask import flash

from db.db import get_password, add_password, update_password
from models.abc.model import Model


@dataclass(init=False)
class PasswordConfig:
    _length_of_password: int = field(default=10, repr=False)
    _password_regex: str = field(default="A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,", repr=False)
    _number_of_history: int = field(default=3, repr=False)
    _number_of_try: int = field(default=3, repr=False)
    _dict_password: bool = field(default=False, repr=False)


class Password(PasswordConfig, Model):
    _username: str = ""
    _current_password: str = ""
    _password_1: str = ""
    _password_2: str = ""
    _password_3: str = ""
    _password_4: str = ""
    _password_5: str = ""
    _password_6: str = ""
    _password_7: str = ""
    _password_8: str = ""
    _password_9: str = ""
    _password_10: str = ""
    _current_try: int = 3
    DATABASE = "passwords"

    def __init__(self, username):
        user = get_password(username)
        self._username = user[0]#username if username in get_password(username) else None
        self._current_password = user[1]
        self._password_1 = user[2] if user[2] else ""
        self._password_2 = user[3] if user[3] else ""
        self._password_3 = user[4] if user[4] else ""
        self._password_4 = user[5] if user[5] else ""
        self._password_5 = user[6] if user[6] else ""
        self._password_6 = user[7] if user[7] else ""
        self._password_7 = user[8] if user[8] else ""
        self._password_8 = user[9] if user[9] else ""
        self._password_9 = user[10] if user[10] else ""
        self._password_10 = user[11] if user[11] else ""

    @classmethod
    def __check_complex_and_len(cls, new_password: str) -> bool:
        regex = "^"
        regex += "(?=.*?[A-Z])" if "A-Z" in cls._password_regex else ""
        regex += "(?=.*?[a-z])" if "a-z" in cls._password_regex else ""
        regex += "(?=.*?[0-9])" if "0-9" in cls._password_regex else ""
        regex += "(?=.*?[\!\@\#\$\%\^\&\*\_\+\.\,])" if len(
            list(set("\!\@\#\$\%\^\&\*\_\+\.\,") & set(cls._password_regex))) > 0 else ""
        regex += ".{" + f"{cls._length_of_password}" + ",}$"
        pattern = r"{a}".format(a=regex)
        username_matcher = re.compile(pattern)
        return True if username_matcher.match(new_password) else False

    @classmethod
    def __check_dict(cls, new_password: str) -> bool:
        if not cls._dict_password:
            new_matcher = re.compile(r"^[^\[]+[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]+[^\]]$")
            return True if new_matcher.match(new_password) else False
        else:
            new_matcher = re.compile(r"^[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]$")
            return True if new_matcher.match(new_password) else False

    @classmethod
    def __password_history(cls, new_password: str) -> bool:
        return True if new_password not in get_password(cls._username) else False

    @classmethod
    def __check_try(cls) -> bool:
        if cls._current_try > 0:
            return True
        else:
            # set_panelty = block login for 5 minutes
            cls._current_try = cls._number_of_try
            return True

    @classmethod
    def __set_password_dict(cls, add: bool) -> None:
        cls._dict_password = add

    @classmethod
    def __set_password_complex(cls, new_regex: str) -> None:
        new_matcher = re.compile(r"(?:[\w][\-][\w])|(?:[+\!\@\#\$\%\^\&\*\_\+\.\,\\])")
        if new_matcher.match(new_regex):
            cls._password_regex = new_regex

    @classmethod
    def _set_config(cls, length: str, regex: str, history: str, dictionary: bool, tries: str) -> None:
        cls._length_of_password = int(length) if len(length) > 0 else cls._length_of_password
        cls.__set_password_complex(new_regex=regex)
        cls._number_of_history = int(history) if len(history) > 0 else cls._number_of_history
        cls.__set_password_dict(add=dictionary)
        cls._current_try = int(tries) if len(tries) > 0 else cls._current_try

    @classmethod
    def confirm_password(cls, new_password: str) -> bool:
        ret = ""
        flag = False
        if cls._length_of_password > len(new_password):
            flag = True
            ret += "[*] Password dont met length.\n"
        print("Length ----> ", ret if ret != "" else "OK")
        if not cls.__check_complex_and_len(new_password):
            print("here")
            flag = True
            ret += "[*] Password dont met complexity.\n"
        print("Complex ----> ", ret if ret != "" else "OK")
        if not cls.__check_dict(new_password):
            flag = True
            ret += "[*] Password dont met dict mode.\n"
        print("Dict ----> ", ret if ret != "" else "OK")
        if not cls.__password_history(new_password):
            flag = True
            ret += "[*] Password dont met dictionary.\n"
        print("History ----> ", ret if ret != "" else "OK")

        if flag:
            if cls.__check_try():
                print(cls._current_try)
                flag = True
                # TODO: set_panelty = block login for 5 minutes
            cls._current_try -= 1
            return False

        cls._current_try = cls._number_of_try
        cls._current_password = new_password
        return True

    @classmethod
    def order_new_password(cls, username: str, password: str) -> tuple:
        user_passwords = get_password(username)
        
        cls._password_10, cls._password_9, cls._password_8,\
        cls._password_7, cls._password_6,cls._password_5,\
        cls._password_4, cls._password_3, cls._password_2,\
        cls._password_1 = [str(pas) for pas in user_passwords]
        cls._current_password = password
        cls._username = username

        return (cls._current_password,
                cls._password_1, cls._password_2, cls._password_3,
                cls._password_4, cls._password_5, cls._password_6,
                cls._password_7, cls._password_8, cls._password_9,
                cls._password_10, cls._username)

    def save_to_db(self) -> None:
        add_password((
                self._username, self._current_password,
                self._password_1, self._password_2, self._password_3,
                self._password_4, self._password_5, self._password_6,
                self._password_7, self._password_8, self._password_9,
                self._password_10))

    def update_to_db(self, password: tuple) -> None:
        update_password(password)

    @classmethod
    def find_from_db(cls, name: str) -> "Password":
        return cls.find_one_by(name, cls.DATABASE)

    @classmethod
    def password_match(cls, password: str) -> bool:
       return hmac.compare_digest(cls._current_password, password)
