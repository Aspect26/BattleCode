import battlecode as bc
from game.game_controller import GC
from states.state import State
from states.units.structures.factory.initial_state import FactoryInitialState


class UnloadingWhenPossibleState(State):

    def run(self) -> None:
        for direction in list(bc.Direction):
            if GC.get().can_unload(self.entity.id, direction):
                GC.get().unload(self.entity.id, direction)
                # TODO: idle state... (maybe just change the name of the initial state to idle state :)))
                self.entity.get_fsm().change_state(FactoryInitialState(self.entity))
