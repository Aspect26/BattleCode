from game.game_controller import GC
from states.state import State
from states.units.dead import DeadState
from states.units.robots.worker.going_to_nearest_karbonite import GoingToNearestKarboniteDepositState


class HarvestingState(State):

    COULDNT_HARVEST_THRESHOLD = 5

    def __init__(self, entity, deposit, deposit_direction):
        super().__init__(entity)
        self._deposit = deposit
        self._deposit_direction = deposit_direction
        self._couldnt_harvest_count = 0

    def run(self) -> None:
        print("[harvest] run - D:" + str(self._deposit.location.x) + ":" + str(self._deposit.location.y) + ",E" + str(self.entity.get_map_location().x) + ":" + str(self.entity.get_map_location().y) + " - " + str(GC.get().karbonite_at(self._deposit.location)))
        if self.entity.is_dead():
            print("[harvest] unit dead")
            self._deposit.being_harvested = False
            self.entity.get_fsm().change_state(DeadState(self.entity))
            return

        # print(f"Unit at {self.entity.get_map_location()} trying to harvest from {self._deposit.location}"
        #      f"heading {self._deposit_direction}")

        self._deposit.observed_karbonite = GC.get().karbonite_at(self._deposit.location)
        # print(f"observed carbonite is = {self._deposit.observed_karbonite}")
        if self._deposit.observed_karbonite <= 0 or self._couldnt_harvest_count > HarvestingState.COULDNT_HARVEST_THRESHOLD:
            print("[harvest] zero karbonite")
            self._deposit.being_harvested = False
            self.entity.get_fsm().change_state(GoingToNearestKarboniteDepositState(self.entity))
            return

        #if GC.get().can_harvest(self.entity.id, self._deposit_direction):
        self._couldnt_harvest_count = 0
        print("[harvest] harvest! " + str(self._deposit_direction))
        print(str(GC.get().harvest(self.entity.id, self._deposit_direction)))
        #else:
        #    print("[harvest] couldnt harvest")
        #    self._couldnt_harvest_count += 1

    def enter(self):
        print("[harvest] enter")
        self._deposit.being_harvested = True

    def exit(self):
        print("[harvest] exit")
        self._deposit.being_harvested = False
