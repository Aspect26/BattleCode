from game.game_controller import GC
from states.state import State
from states.units.dead_state import DeadState


class HarvestingState(State):

    COULDNT_HARVEST_THRESHOLD = 5

    def __init__(self, entity, deposit, deposit_direction):
        super().__init__(entity)
        self._deposit = deposit
        self._deposit_direction = deposit_direction
        self._couldnt_harvest_count = 0

    def run(self) -> None:
        if self.entity.is_dead():
            self._deposit.being_harvested = False
            self.entity.get_fsm().change_state(DeadState(self.entity))
            return

        self._deposit.observed_karbonite = GC.get().karbonite_at(self._deposit.location)
        if self._deposit.observed_karbonite <= 0 or self._couldnt_harvest_count > HarvestingState.COULDNT_HARVEST_THRESHOLD:
            self._deposit.being_harvested = False

            from states.units.robots.worker.idle import WorkerIdleState
            self.entity.get_fsm().change_state(WorkerIdleState(self.entity))

            return

        if GC.get().can_harvest(self.entity.id, self._deposit_direction):
            self._couldnt_harvest_count = 0
            GC.get().harvest(self.entity.id, self._deposit_direction)
        else:
            self._couldnt_harvest_count += 1

    def enter(self):
        self._deposit.being_harvested = True

    def exit(self):
        self._deposit.being_harvested = False
