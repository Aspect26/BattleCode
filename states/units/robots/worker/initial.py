import random

import battlecode

from game_state import GC
from states.state import State


class WorkerInitialState(State):

    def run(self) -> None:
        # TODO: remove this
        directions = list(battlecode.Direction)
        # TODO: how to make the compiler know it is Unit type not Entity type
        try:
            GC.get().move_robot(self.entity.id, random.choice(directions))
        except:
            return

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass
