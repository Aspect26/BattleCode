import battlecode as bc
from game.game_controller import GC
from states.state import State
from states.units.structures.factory.idle_state import FactoryIdleState


class UnloadingWhenPossibleState(State):

    def run(self) -> None:
        for direction in list(bc.Direction):
            if GC.get().can_unload(self.entity.id, direction):
                GC.get().unload(self.entity.id, direction)
                self.entity.get_fsm().change_state(FactoryIdleState(self.entity))
