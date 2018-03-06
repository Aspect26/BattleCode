from entities.entities_map import Entities
from entities.team import Team
from game.game_controller import GC


class AI:

    def __init__(self):
        self._team = Team()
        Entities.TEAM = self._team

    def play_round(self):
        self._team.perform_unit_actions()
        print(str(GC.get().round()) + ": Current karbonite: " + str(GC.get().karbonite()))
