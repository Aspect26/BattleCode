from entities.units.unit import Unit
from states.state import State


class UnitState(State):
    
    unit: Unit = None
    
    def __init__(self, unit: Unit):
        super().__init__(unit)
        self.unit = unit