from abc import ABC, abstractmethod


class AdminUseCase(ABC):

    @abstractmethod
    def users_list(self) -> str:
        ...

    @abstractmethod
    def block_user(self, block) -> None:
        ...

    @abstractmethod
    def unblock_user(self, unblock) -> None:
        ...

    @abstractmethod
    def password_configuration(self) -> None:
        ...
