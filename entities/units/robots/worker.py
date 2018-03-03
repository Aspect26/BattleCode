import battlecode
from entities.units.unit import Unit
from states.units.robots.worker.initial import WorkerInitialState


class Worker(Unit):

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Worker
        super().__init__(WorkerInitialState(self), WorkerInitialState(self), battlecode_unit)
