from entities.units.structures.factory import Factory
from messages.block_karbonite_usage import BlockKarboniteMessage
from messages.message import Message
from messages.unblock_karbonite_usage import UnblockKarboniteMessage
from states.state import State


class GlobalFactoryState(State):

    def __init__(self, factory_entity: Factory):
        super().__init__(factory_entity)
        self._blocked_state: State = None

    def run(self) -> None:
        pass

    def process_message(self, message: Message) -> bool:
        if message is BlockKarboniteMessage:
            self._block_unit_creation()
            return True
        elif message is UnblockKarboniteMessage():
            self._unblock_unit_creation()
            return True

    def _block_unit_creation(self):
        self.entity.get_fsm().pause()

    def _unblock_unit_creation(self):
        self.entity.get_fsm().unpause()
