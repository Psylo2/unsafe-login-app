from abc import ABCMeta
from typing import TypeVar, Type, List, Dict
from db.db import get_user, get_all_users, get_headers

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    def save_to_db(self) -> None:
        raise NotImplementedError

    @classmethod
    def find_one_by(cls: Type[T], one: str, database: str) -> T:
        if database == "user":
            database = get_user(one)
            headers = get_headers("users")
        else:
            database = get_password(one)
            headers = get_headers("passwords")
        return cls(**cls.strip_tup(headers, database))

    @classmethod
    def find_many_by(cls: Type[T], database: str) -> List[T]:
        if database == "user":
            database = get_all_users()
            headers = get_headers("users")
        else:
            database = get_all_passwords()
            headers = get_headers("passwords")
        return [cls(**cls.strip_tup(headers, ele)) for ele in database]

    @classmethod
    def strip_tup(cls: Type[T], headers: List, database: List) -> Dict:
        return {headers[i]: database[i] for i in range(len(headers))}
