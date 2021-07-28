from dataclasses import dataclass, field
from typing import List

from werkzeug.security import hmac
from db.db import add_user, block_user, update_user
from models.abc.model import Model


@dataclass
class UserModel:
    _name: str
    _email: str
    _password: str = field(repr=False)
    _blocked: int = field(default=0)
        
    def __post_init__(self):
        from models.password import Password
        _password = Passwword(_password=_password)
        
        



class User(UserModel, Model):
    DATABASE = "users"
    
    # TODO: How to call password and save him aswell each time
    def save_to_db(self) -> None:
            add_user(self._name, self._email, self._blocked)
    
    # TODO: Check if works
    def block_user_model(self) -> None:
        block_user(self._name, 1)

    # TODO: Check if works        
    def unblock_user_model(self) -> None:
        block_user(self._name, 0)

    @classmethod
    def find_from_db(cls, name: str) -> "User":
        return cls.find_one_by(name, DATABASE)

    @classmethod
    def find_all_from_db(cls) -> List["User"]:
        return cls.find_many_by(DATABASE)

    # TODO: Implement on password_ model & password_logic
    @classmethod
    def update_password(cls) -> None:
        update_user(cls._name, cls._password)
    
    #TODO: Implement on login_utils 
    @classmethod
    def valid_login(cls, name_email: str, password: str) -> bool:
        user = cls.find_from_db(name_email)
        return hmac.compare_digest(user._password, password)

