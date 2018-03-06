from entities.entity import Entity
from states.research.global_state import GlobalResearcherState
from states.research.idle_state import IdleResearcherState


class Researcher(Entity):

    def __init__(self):
        super().__init__(IdleResearcherState(self), GlobalResearcherState(self))
