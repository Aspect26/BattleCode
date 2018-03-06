import battlecode
from entities.units.unit import Unit
from states.units.robots.mage.global_state import MageGlobalState
from states.units.robots.mage.initial_state import MageInitialState


class Mage(Unit):

    def __init__(self, battlecode_unit):
        assert battlecode_unit.unit_type == battlecode.UnitType.Mage
        super().__init__(MageInitialState(self), MageGlobalState(self), battlecode_unit)
