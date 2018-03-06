from entities.entity import Entity
from game.game_controller import GC
from states.state import State
import battlecode as bc


class Unit(Entity):

    def __init__(self, begin_state: State, global_state: State, battlecode_unit):
        super().__init__(begin_state, global_state)
        self._unit = battlecode_unit

    @property
    def id(self) -> int:
        return self._unit.id

    def get_map_location(self) -> bc.MapLocation:
        return self.get_unit().location.map_location()

    def is_dead(self):
        return self.get_unit().health <= 0

    def get_unit(self) -> bc.Unit:
        """
        We need this because the battlecode engine recreates all the units after each round, for some reason
        """
        return GC.get().unit(self._unit.id)
