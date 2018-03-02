import battlecode as bc
import random

from ai import AI
from game_state import GC

random.seed(6137)
GC(bc.GameController())
ai = AI()

while True:
    ai.play_round()
    GC.get().next_turn()
