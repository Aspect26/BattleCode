from game.game_state import GC
from states.units.unit_state import UnitState
from states.units.robots.worker.going_to_nearest_karbonite import GoingToNearestKarboniteDepositState


class WorkerIdleState(UnitState):

    def run(self) -> None:
        nearest_karbonite = GC.get_nearest_karbonite_deposit(self.unit.get_map_location())
        
        if (nearest_karbonite.observed_karbonite > 0 and not nearest_karbonite.observed_owned_by_enemy):
            self.entity.get_fsm().change_state(GoingToNearestKarboniteDepositState(self.entity))
        