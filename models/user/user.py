from typing import Dict
from dataclasses import dataclass
from werkzeug.security import hmac
from db.db import add_user, get_user
from models.abc.model import Model


@dataclass
class UserModel:
    _name: str
    _email: str
    _password: str


class User(UserModel, Model):

    def save_to_db(self) -> None:
        add_user(self._name, self._email, self._password)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        user, password = get_user(name)
        return User(user, password)

    @classmethod
    def valid_login(cls, name_email: str, password: str):

        user = cls.find_from_db(name_email)

        if hmac.compare_digest(user._password, password):
            return True
        else:
            return False


