from abc import ABC, abstractmethod


class UserUseCase(ABC):

    @abstractmethod
    def login(self) -> bool:
        ...

    @abstractmethod
    def register(self) -> bool:
        ...

    @abstractmethod
    def change_password(self) -> bool:
        ...

    @abstractmethod
    def logout(self) -> None:
        ...
