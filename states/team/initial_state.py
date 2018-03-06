from states.team.early import TeamEarlyState
from states.team.team_state import TeamState


class TeamInitialState(TeamState):

    def __init__(self, team):
        super().__init__(team)
        
    def run(self):
        self.team.get_fsm().change_state(TeamEarlyState())
