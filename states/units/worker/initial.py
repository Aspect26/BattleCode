import random

import battlecode

from game_state import GC
from states.state import State


class WorkerInitialState(State):

    def run(self) -> None:
        # TODO: remove this
        directions = list(battlecode.Direction)
        # TODO: how to make the compiler know it is Unit type not Entity type
        GC.get().move_robot(self.entity.get_id(), random.choice(directions))

    def enter(self) -> None:
        pass

    def exit(self) -> None:
        pass
