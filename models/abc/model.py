from abc import ABCMeta, abstractmethod
from typing import Type, TypeVar, Dict, List, Union
from db.db import connection

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):

    def save_to_db(self) -> None:
        raise NotImplementedError

    def json(self) -> Dict:
        raise NotImplementedError
