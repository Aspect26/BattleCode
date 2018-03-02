from entities.team import Team
from states.state import State


class TeamInitialState(State):

    def __init__(self, team: Team):
        super().__init__(team)
