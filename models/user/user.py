import re
from dataclasses import dataclass, field
from typing import List
from flask import current_app


from db.db import add_user, block_user
from models.abc.model import Model


@dataclass(init=False)
class UserModel:
    _name: str
    _email: str
    _blocked: int = field(default=0)

    def __init__(self, username: str, email: str, blocked: int):
        self._name = username
        self._email = email
        self._blocked = blocked

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self.email

    @property
    def blocked(self):
        return self.blocked

class User(UserModel, Model):
    DATABASE = "users"

    def save_to_db(self) -> None:
        add_user(self.name, self.email, self.blocked)

    def block_user_model(self) -> None:
        if self.name != current_app.config["ADMIN"]:
            block_user(self.name, 1)

    def unblock_user_model(self) -> None:
        if self.name != current_app.config["ADMIN"]:
            block_user(self.name, 0)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        return cls.find_one_by(name, cls.DATABASE)

    @classmethod
    def find_all_from_db(cls) -> List["User"]:
        return cls.find_many_by(cls.DATABASE)


class UserValidator:
    def __init__(self):
        self._name_regex = r"^[A-Za-z0-9{2,}]+$"
        self._email_regex = r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$"
        self._password_regex = r"^(?=.{10,15}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[\!\@\#\$\%\^\&\*\-\=\+\_\<\>\{" \
                               r"\}\(\)\[\]\:\;\/\|\~\`\ ]).*$ "

    def is_valid_username(self, username: str) -> bool:
        username_matcher = re.compile(f"{self._name_regex}")
        return True if username_matcher.match(username) else False

    def is_valid_email(self, email: str) -> bool:
        email_matcher = re.compile(f"{self._email_regex}")
        return True if email_matcher.match(email) else False

    def is_valid_password(self, password: str) -> bool:
        email_matcher = re.compile(f"{self._password_regex}")
        return True if email_matcher.match(password) else False
