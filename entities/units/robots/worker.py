import battlecode
from entities.units.unit import Unit
from states.units.robots.worker.initial import WorkerInitialState


class Worker(Unit):
    """ This class represents the Worker unit
    STATES:
        It has basically two states: finding a nearest karbonite deposit or harvesting and it is switching between them,
    MESSAGES:
        Harvested - when harvested whole deposit inform the game state about it
    """

    def __init__(self, battlecode_unit):
        # TODO: add global state
        assert battlecode_unit.unit_type == battlecode.UnitType.Worker
        super().__init__(WorkerInitialState(self), WorkerInitialState(self), battlecode_unit)
