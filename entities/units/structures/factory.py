import battlecode
from entities.units.unit import Unit
from states.units.structures.factory.initial_state import FactoryInitialState


class Factory(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Factory
        super().__init__(FactoryInitialState(self), FactoryInitialState(self), battlecode_unit)
