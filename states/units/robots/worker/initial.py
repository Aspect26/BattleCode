from states.state import State
from states.units.robots.worker.going_to_nearest_karbonite import GoingToNearestKarboniteDepositState


class WorkerInitialState(State):

    def run(self) -> None:
        self.entity.get_fsm().change_state(GoingToNearestKarboniteDepositState(self.entity))
