from abc import abstractmethod
from messages.message import Message


class State:

    def __init__(self, entity):
        from entities.entity import Entity
        self.entity: Entity = entity

    def process_message(self, message: Message) -> bool:
        return False

    @abstractmethod
    def run(self) -> None:
        pass

    def enter(self) -> None:
        return

    def exit(self) -> None:
        return

    def paused(self) -> None:
        return

    def unpaused(self) -> None:
        return
