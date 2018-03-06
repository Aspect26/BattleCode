from states.units.unit_state import UnitState
from states.units.robots.worker.idle import WorkerIdleState


class WorkerInitialState(UnitState):

    def run(self) -> None:
        self.entity.get_fsm().change_state(WorkerIdleState(self.entity))
