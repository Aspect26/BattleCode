from states.state import State

class TeamState(State):
    
    team = None

    def __init__(self, team):
        super().__init__(team)
        self.team = team