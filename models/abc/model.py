from abc import ABCMeta
from typing import TypeVar, Type, List, Dict
from db.db import get_user, get_all_users

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    def save_to_db(self) -> None:
        raise NotImplementedError

    @classmethod
    def find_one_by(cls: Type[T], name_email: str) -> T:
        user = get_user(name_email)
        return cls(**cls.strip_tup(user))

    @classmethod
    def find_many_by(cls: Type[T]) -> List[T]:
        users = get_all_users()
        return [cls(**cls.strip_tup(user)) for user in users]

    @classmethod
    def strip_tup(cls: Type[T], tup: tuple) -> Dict:
        return {"_name": tup[0], "_email": tup[1], "_password": tup[2], "_blocked": tup[3]}
