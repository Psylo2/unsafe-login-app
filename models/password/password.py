from dataclasses import dataclass, field
import re


@dataclass
class Password:
    _password: str  # = field(repr=False)
    _length_of_password: int = field(default=10)
    _password_regex: str = field(default="[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]")
    _number_of_history: int = field(default=3)
    _number_of_try: int = field(default=3)
    _dict_password: bool = field(default=False)

    def __complex_and_len(self) -> bool:
        pattern = f"^[{self._password_regex}" + "{" + f"{self._length_of_password}" + ",}]+$"
        matcher = r"{a}".format(a=pattern)
        print(matcher)
        username_matcher = re.compile(matcher)
        return True if username_matcher.match(self._password) else False


    def __password_history(self, num_check: int) -> bool:
        return True if num_check == self._number_of_history else False

    def __password_dict(self) -> bool:
        return self._dict_password

    def __check_try(self, num_try: int) -> bool:
        return True if num_try == self._number_of_try else False

    def __change_complexity(self, new_regex: str) -> None:
        new_matcher = re.compile(r"^\[+[A-Za-z0-9\!\@\#\$\%\^\&\*\_\+\.\,]+\]$")
        if new_matcher.match(new_regex):
            self._password_regex = new_regex

    def _set_config(self, length: int, regex: str, history: int, tries: int, dictionary: bool) -> None:
        self._length_of_password = length
        self.__change_complexity(regex)
        self._number_of_history = history
        self._number_of_try = tries
        self._dict_password = dictionary




