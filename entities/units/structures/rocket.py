import battlecode
from entities.units.unit import Unit
from states.units.structures.rocket.initial_state import RocketInitialState


class Rocket(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Factory
        super().__init__(RocketInitialState(self), RocketInitialState(self), battlecode_unit)
