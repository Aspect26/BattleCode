import battlecode
from entities.units.unit import Unit
from states.units.structures.factory.global_state import GlobalFactoryState
from states.units.structures.factory.idle_state import FactoryIdleState


class Factory(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Factory
        super().__init__(FactoryIdleState(self), GlobalFactoryState(self), battlecode_unit)
