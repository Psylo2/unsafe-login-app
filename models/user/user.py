from dataclasses import dataclass, field
from typing import List

from werkzeug.security import hmac
from db.db import add_user, block_user, update_user
from models.abc.model import Model
from models.password import Password


@dataclass
class UserModel:
    _name: str
    _email: str
    _password: str = field(repr=False, default_factory=Password(_password="AAaa12@!aA"))
    _blocked: int = field(default=0)



class User(UserModel, Model):

    def save_to_db(self) -> None:
        if _password.confirm_password():
            add_user(self._name, self._email, self._password, self._blocked)

    def block_user_model(self) -> None:
        block_user(self._name, 1)

    def unblock_user_model(self) -> None:
        block_user(self._name, 0)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        return cls.find_one_by(name, "user")

    @classmethod
    def find_all_from_db(cls) -> List["User"]:
        return cls.find_many_by("user")

    @classmethod
    def update_password(cls) -> None:
        update_user(cls._name, cls._password)

    @classmethod
    def valid_login(cls, name_email: str, password: str) -> bool:
        user = cls.find_from_db(name_email)
        return hmac.compare_digest(user._password, password)

