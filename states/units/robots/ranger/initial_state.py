import random

import battlecode as bc
from game.game_controller import GC
from states.state import State


class RangerInitialState(State):

    def __init__(self, entity):
        super().__init__(entity)
        self._unloaded = False

    def run(self) -> None:
        # TODO: implement me
        d = random.choice(list(bc.Direction))
        if GC.get().can_move(self.entity.id, d):
            GC.get().move_robot(self.entity.id, d)
