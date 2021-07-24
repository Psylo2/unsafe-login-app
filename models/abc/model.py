from abc import ABCMeta
from typing import TypeVar, Type, List
from db.db import get_user, get_all_users

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    def save_to_db(self) -> None:
        raise NotImplementedError

    @classmethod
    def find_one_by(cls: Type[T], name_email: str) -> T:
        user = get_user(name_email)
        d = {"_name": user[0], "_email": user[1], "_password": user[2]}
        return cls(**d)

    @classmethod
    def find_many_by(cls: Type[T]) -> List[T]:
        users = get_all_users()
        return [cls(**{"_name": user[0], "_email": user[1], "_password": user[2]}) for user in users]
