import battlecode
from entities.units.unit import Unit
from states.units.robots.knight.global_state import KnightGlobalState
from states.units.robots.knight.initial_state import KnightInitialState


class Knight(Unit):

    def __init__(self, battlecode_unit):
        assert battlecode_unit.unit_type == battlecode.UnitType.Knight
        super().__init__(KnightInitialState(self), KnightGlobalState(self), battlecode_unit)
