import battlecode as bc
import random

from ai import AI
from game.game_state import GC
from pathfinding.pathfinder import SimplePathFinder

random.seed(6137)
GC(bc.GameController())
SimplePathFinder()
ai = AI()

while True:
    try:
        ai.play_round()
    except Exception as e:
        print(e)
    GC.get().next_turn()
