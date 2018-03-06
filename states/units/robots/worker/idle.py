from game.game_controller import GC
from states.units.unit_state import UnitState
from states.units.robots.worker.going_to_nearest_karbonite_state import GoingToNearestKarboniteDepositState


class WorkerIdleState(UnitState):

    def __init__(self, entity):
        super().__init__(entity)

    def enter(self):
        self.run()

    def run(self) -> None:
        nearest_karbonite = GC.get_nearest_karbonite_deposit(self.unit.get_map_location())
        
        if nearest_karbonite is not None:
            self.entity.get_fsm().change_state(GoingToNearestKarboniteDepositState(self.entity))