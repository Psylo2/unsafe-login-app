import time
from dataclasses import dataclass, field
import re
from flask import flash

from db.db import update_password, get_password, add_password
from models.abc.model import Model


@dataclass(init=False)
class PasswordConfig:
    _length_of_password: int = field(default=10, repr=False)
    _password_regex: str = field(default="A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,", repr=False)
    _number_of_history: int = field(default=3, repr=False)
    _number_of_try: int = field(default=3, repr=False)
    _dict_password: bool = field(default=False, repr=False)

    @classmethod
    def _check_dict(cls, new_password: str) -> bool:
        if cls._dict_password:
            print("dict mode: ON")
            with open("utils\\dictionary.txt", "r") as file:
                print(new_password)
                print("true"if new_password in file.read() else "false")
                return False if new_password in file.read() else True
        return True


    @classmethod
    def _check_complex_and_len(cls, new_password: str) -> bool:
        regex = "^"
        regex += "(?=.*?[A-Z])" if "A-Z" in cls._password_regex else ""
        regex += "(?=.*?[a-z])" if "a-z" in cls._password_regex else ""
        regex += "(?=.*?[0-9])" if "0-9" in cls._password_regex else ""
        regex += "(?=.*?[\!\@\#\$\%\^\&\*\_\+\.\,])" if len(
            list(set("\!\@\#\$\%\^\&\*\_\+\.\,") & set(cls._password_regex))) > 0 else ""
        regex += ".{" + f"{cls._length_of_password}" + ",}$"
        pattern = r"{a}".format(a=regex)
        print(regex)
        username_matcher = re.compile(pattern)
        return True if username_matcher.match(new_password) else False

    @classmethod
    def __password_history(cls, new_password: str, username: str) -> bool:
        return True if new_password not in get_password(username) else False

    @classmethod
    def _set_password_dict(cls, add: bool) -> None:
        cls._dict_password = add
        print("Dict:", cls._dict_password)


    @classmethod
    def _set_password_complex(cls, new_regex: str) -> None:
        new_matcher = re.compile(r"(?:[\w][\-][\w])|(?:[+\!\@\#\$\%\^\&\*\_\+\.\,\\])")
        if new_matcher.match(new_regex):
            cls._password_regex = new_regex
            print("Complex:", cls._password_regex)

    @classmethod
    def _set_config(cls, length: str, regex: str, history: str, dictionary: bool, tries: str) -> None:
        cls._length_of_password = int(length) if len(length) > 0 else cls._length_of_password
        cls._set_password_complex(new_regex=regex)
        cls._number_of_history = int(history) if len(history) > 0 else cls._number_of_history
        cls._set_password_dict(add=dictionary)
        cls._number_of_try = int(tries) if len(tries) > 0 else 0
        print("Length:", cls._length_of_password)
        print("History:", cls._number_of_history)
        print("Tries:", cls._number_of_try)


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

    def __init__(self, username, current_password: str = "", password_1: str = "", password_2: str = "",
                 password_3: str = "", password_4: str = "", password_5: str = "", password_6: str = "",
                 password_7: str = "",
                 password_8: str = "", password_9: str = "", password_10: str = ""):
        self._username = username
        self._current_password = current_password
        self._password_1 = password_1
        self._password_2 = password_2
        self._password_3 = password_3
        self._password_4 = password_4
        self._password_5 = password_5
        self._password_6 = password_6
        self._password_7 = password_7
        self._password_8 = password_8
        self._password_9 = password_9
        self._password_10 = password_10

    @classmethod
    def confirm_password(cls, new_password: str) -> bool:
        ret = ""
        flag = False

        if cls._length_of_password >= len(new_password):
            flag = True
            ret += "[*] Password dont met length.\n"
        print("Length ----> ", ret if ret != "" else "OK")

        if not cls._check_complex_and_len(new_password):
            flag = True
            ret += "[*] Password dont meet complexity.\n"
        print("Complex ----> ", ret if ret != "" else "OK")

        if not cls._check_dict(new_password):
            flag = True
            ret += "[*] Password dont meet dict mode.\n"
        print("Dict ----> ", ret if ret != "" else "OK")

        try:
            if not cls.__password_history(new_password, cls._username):
                flag = True
                ret += "[*] Password dont met dictionary.\n"
            print("History ----> ", ret if ret != "" else "OK")
        except:
            pass
        if flag:
            if 0 < cls._current_try <= cls._number_of_try:
                cls._current_try -= 1
                print("current_try:  ", cls._current_try)
                if cls._current_try == 0:
                    flash("Next bad try will bring time Penalty for 30 sec.", 'danger')
                return False

            cls._current_try = cls._number_of_try
            time.sleep(30)
            return False

        cls._current_try = cls._number_of_try
        return True

    @classmethod
    def order_new_password(cls, username: str, password: str) -> tuple:
        p = get_password(username)
        cls._password_10 = p[10]
        cls._password_9 = p[9]
        cls._password_8 = p[8]
        cls._password_7 = p[7]
        cls._password_6 = p[6]
        cls._password_5 = p[5]
        cls._password_4 = p[4]
        cls._password_3 = p[3]
        cls._password_2 = p[2]
        cls._password_1 = p[1]
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
