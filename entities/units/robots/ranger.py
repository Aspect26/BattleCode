import battlecode
from entities.units.unit import Unit
from states.units.robots.ranger.global_state import RangerGlobalState
from states.units.robots.ranger.initial_state import RangerInitialState


class Ranger(Unit):

    def __init__(self, battlecode_unit):
        assert battlecode_unit.unit_type == battlecode.UnitType.Ranger
        super().__init__(RangerInitialState(self), RangerGlobalState(self), battlecode_unit)
