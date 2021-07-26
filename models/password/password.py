from dataclasses import dataclass, field
import re

from flask import flash


@dataclass
class Password:
    _password: str  # = field(repr=False)
    _length_of_password: int = field(default=10)
    _password_regex: str = field(default="[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]")
    _number_of_history: int = field(default=3)
    _number_of_try: int = field(default=3)
    _dict_password: bool = field(default=False)

    def __check_complex_and_len(self) -> bool:
        pattern = f"^[{self._password_regex}" + "{" + f"{self._length_of_password}" + ",}]+$"
        matcher = r"{a}".format(a=pattern)
        print(matcher)
        username_matcher = re.compile(matcher)
        return True if username_matcher.match(self._password) else False

    def __check_dict(self, password: str) -> bool:
        if self._dict_password:
            new_matcher = re.compile(r"^\[+[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]+\]$")
            return True if new_matcher.match(password) else False
        else:
            new_matcher = re.compile(r"^[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]$")
            return True if new_matcher.match(password) else False

    def __password_history(self, num_check: int) -> bool:
        return True if num_check == self._number_of_history else False

    def __check_try(self, num_try: int) -> bool:
        return True if num_try > self._number_of_try else False

    def __set_password_dict(self, add: bool) -> None:
        self._dict_password = add
        self.__check_dict()

    def __set_password_complex(self, new_regex: str) -> None:
        new_matcher = re.compile(r"^\[+[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]+\]$")
        if new_matcher.match(new_regex):
            self._password_regex = new_regex

    def _set_config(self, length: int, regex: str, history: int, dictionary: bool, tries: int) -> None:
        self._length_of_password = length
        self.__set_password_complex(regex)
        self._number_of_history = history
        self.__set_password_dict(dictionary)
        self._number_of_try = tries

    def confirm_password(self, password: str, trie: int) -> bool:
        ret = ""
        flag = False
        if self._length_of_password < len(password):
            flag = True
            ret += "[*] Password dont met length.\n"
        if self.__check_complex_and_len():
            flag = True
            ret += "[*] Password dont met complexity.\n"
        if self.__check_dict(password):
            flag = True
            ret += "[*] Password dont met dictionary.\n"
        if self.__check_try(trie):
            flag = True
            ret += "[*] Too many unsuccessful tries.\n"

        if flag:
            flash("ret", "danger")
            return False
        return True
