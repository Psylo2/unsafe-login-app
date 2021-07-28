from abc import ABCMeta
from typing import TypeVar, Type, List, Dict
from db.db import (get_user, get_all_users, get_password,
                   get_all_passwords, get_headers)

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    def save_to_db(self) -> None:
        raise NotImplementedError

    @classmethod
    def find_one_by(cls: Type[T], one: str, header: str) -> T:
        if header == "users":
            database = get_user(one)
        else:
            database = get_password(one)
        headers = get_headers(header) #"passwords" or "users"
        return cls(**cls.strip_tup(headers, database))

    @classmethod
    def find_many_by(cls: Type[T], header: str) -> List[T]:
        if header == "users":
            database = get_all_users()
        else:
            database = get_all_passwords()
        headers = get_headers(header) #"passwords" or "users"
        return [cls(**cls.strip_tup(headers, database))]

    @classmethod
    def strip_tup(cls: Type[T], headers: List, database: List) -> Dict:
        ret = {}

        if type(database) is list:
            for i in range(len(database)):
                for j in range(len(database[i])):
                    ret.update({headers[j]: database[i][j]})

        if type(database) is tuple:
            for i in range(len(database)):
                print(headers[i], database[i])
                ret.update({headers[i]: database[i]})

        return ret
