from fsm import FiniteStateMachine
from states.state import State


class Entity:

    def __init__(self, begin_state: State, global_state: State):
        self._fsm = FiniteStateMachine(self, begin_state, global_state)

    def get_fsm(self) -> FiniteStateMachine:
        return self._fsm
