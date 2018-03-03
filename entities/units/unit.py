from entities.entity import Entity
from game.game_state import GC
from states.state import State


class Unit(Entity):

    def __init__(self, begin_state: State, global_state: State, battlecode_unit):
        super().__init__(begin_state, global_state)
        self._unit = battlecode_unit

    @property
    def id(self) -> int:
        return self._unit.id

    def get_map_location(self):
        return self._get_unit().location.map_location()

    def is_dead(self):
        return self._get_unit().health <= 0

    def _get_unit(self):
        """
        We need this because the battlecode engine recreates all the units after each round, for some reason
        """
        return GC.get().unit(self._unit.id)
