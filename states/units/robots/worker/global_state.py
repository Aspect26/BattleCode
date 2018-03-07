from messages.enemy_unit_encountered import EnemyUnitEncounteredMessage
from messages.message import Message
from states.state import State


class WorkerGlobalState(State):

    def run(self) -> None:
        pass

    def process_message(self, message: Message):
        if message is EnemyUnitEncounteredMessage:
            # TODO: Dont go there!
            pass