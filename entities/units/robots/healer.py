import battlecode
from entities.units.unit import Unit
from states.units.robots.healer.initial import HealerInitialState


class Mage(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Healer
        super().__init__(HealerInitialState(self), HealerInitialState(self), battlecode_unit)
