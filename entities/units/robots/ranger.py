import battlecode
from entities.units.unit import Unit
from states.units.robots.ranger.initial import RangerInitialState


class Ranger(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Ranger
        super().__init__(RangerInitialState(self), RangerInitialState(self), battlecode_unit)
