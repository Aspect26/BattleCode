from messages.message import Message
from states.state import State


class FiniteStateMachine:

    def __init__(self, entity, begin_state: State, global_state: State):
        self._entity = entity
        self._current_state = begin_state
        self._global_state = global_state

    def change_state(self, to_state: State) -> None:
        assert self._current_state is not None
        self._current_state.exit()
        self._current_state = to_state
        self._current_state.enter()

    def update(self) -> None:
        assert self._global_state is not None
        assert self._current_state is not None
        # self._global_state.run()
        self._current_state.run()

    def process_message(self, message: Message) -> None:
        assert self._global_state is not None
        assert self._current_state is not None

        if self._current_state.process_message(message):
            return

        self._global_state.process_message(message)
