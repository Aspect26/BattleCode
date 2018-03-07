import traceback
import sys

import battlecode as bc
import random

from ai import AI
from game.game_controller import GC
from pathfinding.pathfinder import PathFinder

random.seed(6137)
GC(bc.GameController())
PathFinder()
ai = AI()

while True:
    try:
        ai.play_round()
    except Exception as e:
        print(traceback.format_exc())
    GC.get().next_turn()

    # these lines are not strictly necessary, but it helps make the logs make more sense
    # it forces everything we've written this turn to be written to the manager
    sys.stdout.flush()
    sys.stderr.flush()
