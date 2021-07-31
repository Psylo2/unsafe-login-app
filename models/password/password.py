from dataclasses import dataclass, field
import re
from flask import flash

from db.db import (get_password, get_all_passwords,
                   add_password, update_password)
from models.abc.model import Model


@dataclass
class PasswordConfig:
    _current_try: int
    _length_of_password: int = field(default=10, repr=False)
    _password_regex: str = field(default="A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,", repr=False)
    _number_of_history: int = field(default=3, repr=False)
    _number_of_try: int = field(default=3, repr=False)
    _dict_password: bool = field(default=False, repr=False)


class Password(PasswordConfig, Model):
    _username: str
    _current_password: str  # = field(repr=False)
    _password_1: str  # = field(repr=False)
    _password_2: str  # = field(repr=False)
    _password_3: str  # = field(repr=False)
    _password_4: str  # = field(repr=False)
    _password_5: str  # = field(repr=False)
    _password_6: str  # = field(repr=False)
    _password_7: str  # = field(repr=False)
    _password_8: str  # = field(repr=False)
    _password_9: str  # = field(repr=False)
    _password_10: str  # = field(repr=False)

    DATABASE = "passwords"

    def __check_complex_and_len(self, new_password: str) -> bool:
        pattern = f"^[{self._password_regex}" + "{" + f"{self._length_of_password}" + ",}]+$"
        print(pattern)
        matcher = r"{a}".format(a=pattern)
        print(matcher)
        username_matcher = re.compile(matcher)
        return True if username_matcher.match(new_password) else False

    def __check_dict(self, new_password: str) -> bool:
        if self._dict_password:
            new_matcher = re.compile(r"^\[+[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]+\]$")
            return True if new_matcher.match(new_password) else False
        else:
            new_matcher = re.compile(r"^[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]$")
            return True if new_matcher.match(new_password) else False

    def __password_history(self, username: str, new_password: str) -> bool:
        return True if new_password not in get_password(username) else False

    def __check_try(self) -> bool:
        if self._current_try > 0:
            return True
        else:
            # set_panelty = block login for 5 minutes
            self._current_try = self._number_of_try + 1
            return True

    def __set_password_dict(self, add: bool) -> None:
        self._dict_password = add
        # self.__check_dict()

    def __set_password_complex(self, new_regex: str) -> None:
        new_matcher = re.compile(r"(?:[\w][\-][\w])|(?:[+\!\@\#\$\%\^\&\*\_\+\.\,\\])")
        if new_matcher.match(new_regex):
            self._password_regex = new_regex

    def _set_config(self, length: int, regex: str, history: int, dictionary: bool, tries: int) -> None:
        print("before length: --> ", self._length_of_password)
        print("before regex: --> ", self._password_regex)
        print("before history: --> ", self._number_of_history)
        print("before dict: --> ", self._dict_password)
        print("before tries: --> ", self._current_try)

        self._length_of_password = length
        self.__set_password_complex(self=Password, new_regex=regex)
        self._number_of_history = history
        self.__set_password_dict(self=Password, add=dictionary)
        self._current_try = tries

        print("after length: --> ", self._length_of_password)
        print("after regex: --> ", self._password_regex)
        print("after history: --> ", self._number_of_history)
        print("after dict: --> ", self._dict_password)
        print("after tries: --> ", self._current_try)

    def confirm_password(self, new_password: str) -> bool:
        ret = ""
        flag = False
        if self._length_of_password < len(new_password):
            flag = True
            ret += "[*] Password dont met length.\n"
        if self.__check_complex_and_len(new_password):
            flag = True
            ret += "[*] Password dont met complexity.\n"
        if self.__check_dict(new_password):
            flag = True
            ret += "[*] Password dont met dictionary.\n"
        if self.__check_try():
            flag = True
            ret += "[*] Too many unsuccessful tries.\n"
            # TODO: set_panelty = block login for 5 minutes

        if flag:
            flash("ret", "danger")
            print("fail password")
            self._current_try -= 1
            return False

        print("sucsses password")
        return True

    def save_to_db(self) -> None:
        add_password(self._username, self._current_password, self._password_1,
                     self._password_2, self._password_3, self._password_4, self._password_5,
                     self._password_6, self._password_7, self._password_8, self._password_9,
                     self._password_10)

    @classmethod
    def find_from_db(cls, name: str) -> "Password":
        return cls.find_one_by(name, cls.DATABASE)


