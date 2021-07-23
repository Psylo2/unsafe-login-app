from typing import Dict
from dataclasses import dataclass
from werkzeug.security import hmac
from db.db import add_user, get_user
from models.abc.model import Model


@dataclass
class UserModel:
    _name: str
    _password: str


class User(UserModel, Model):

    def json(self) -> Dict:
        return {
            "name": self._name,
            "password": self._password
        }

    def save_to_db(self) -> None:
        add_user(self._name, self._password)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        user, password = get_user(name)
        return User(user, password)

    @classmethod
    def valid_login(cls, username: str, password: str):

        user = cls.find_from_db(username)

        if hmac.compare_digest(user._password, password):
            return True
        else:
            return False


