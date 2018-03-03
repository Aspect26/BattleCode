import battlecode
from entities.units.unit import Unit
from states.units.robots.mage.initial import MageInitialState


class Mage(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Mage
        super().__init__(MageInitialState(self), MageInitialState(self), battlecode_unit)
