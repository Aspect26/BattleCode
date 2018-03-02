from entities.team import Team


class AI:

    def __init__(self):
        self._team = Team()

    def play_round(self):
        self._team.perform_entity_actions()
