from entities.entity import Entity
from states.state import State


class Unit(Entity):

    def __init__(self, begin_state: State, global_state: State, battlecode_unit):
        super().__init__(begin_state, global_state)
        self._unit = battlecode_unit

    @property
    def id(self) -> int:
        return self._unit.id
