from abc import abstractmethod

from entities.entity import Entity
from messages.message import Message


class State:

    def __init__(self, entity: Entity):
        self.entity: Entity = entity

    def process_message(self, message: Message) -> bool:
        return False

    @abstractmethod
    def run(self) -> None:
        pass

    @abstractmethod
    def enter(self) -> None:
        pass

    @abstractmethod
    def exit(self) -> None:
        pass
