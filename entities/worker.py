from entities.unit import Unit
from states.units.worker.initial import WorkerInitialState


class Worker(Unit):

    def __init__(self, id: int):
        # TODO: add global state
        super().__init__(WorkerInitialState(self), WorkerInitialState(self), id)
