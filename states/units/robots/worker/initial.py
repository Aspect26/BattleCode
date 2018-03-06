from states.units.unit_state import UnitState
from states.units.robots.worker.idle import WorkerIdleState
from states.units.robots.worker.going_to_nearest_karbonite import GoingToNearestKarboniteDepositState


class WorkerInitialState(UnitState):

    def run(self) -> None:
        self.entity.get_fsm().change_state(WorkerIdleState(self.entity))
