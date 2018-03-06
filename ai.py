from entities.team import Team
from game.game_controller import GC


class AI:

    def __init__(self):
        self._team = Team()

    def play_round(self):
        self._team.perform_actions()
        print(str(GC.get().round()) + ": Current karbonite: " + str(GC.get().karbonite()))
