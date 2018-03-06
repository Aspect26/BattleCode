import battlecode
from entities.units.unit import Unit
from states.units.robots.healer.global_state import HealerGlobalState
from states.units.robots.healer.initial_state import HealerInitialState


class Healer(Unit):

    def __init__(self, battlecode_unit):
        assert battlecode_unit.unit_type == battlecode.UnitType.Healer
        super().__init__(HealerInitialState(self), HealerGlobalState(self), battlecode_unit)
