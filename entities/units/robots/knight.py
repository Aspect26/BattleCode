import battlecode
from entities.units.unit import Unit
from states.units.knight.initial import KnightInitialState


class Knight(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Knight
        super().__init__(KnightInitialState(self), KnightInitialState(self), battlecode_unit)
