from abc import abstractmethod

from messages.message import Message


class State:

    # TODO: entity type
    def __init__(self, entity):
        self.entity = entity

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
