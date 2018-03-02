from entities.entity import Entity
from states.state import State


class Unit(Entity):

    def __init__(self, begin_state: State, global_state: State, identifier: int):
        super().__init__(begin_state, global_state)
        self._id = identifier

    def get_id(self) -> int:
        return self._id
