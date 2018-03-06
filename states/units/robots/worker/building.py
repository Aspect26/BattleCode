from entities.units.robots.worker import Worker
from states.units.robots.worker.idle import WorkerIdleState
from game.game_state import GC
import battlecode as bc
from states.state import State
from states.units.unit_state import UnitState


class BuildingState(UnitState):

    _build_direction : bc.Direction = None
    _build_structure_type: bc.UnitType = None

    def __init__(self, unit, build_structure_type: bc.UnitType, build_direction: bc.Direction):
        super().__init__(unit)
        self._build_direction = build_direction
        self._build_structure_type = build_structure_type
        
    def enter(self):
        GC.get().blueprint(self.unit.id, self._build_structure_type, self._build_direction)

    def run(self) -> None:
        
        adjacentUnits = GC.get().sense_nearby_units(self.unit.get_map_location(), 2)
        building_something = False
        for adjacent in adjacentUnits:
            if GC.get().can_build(self.unit.id, adjacent.id):
                GC.get().build(self.unit.id, adjacent.id)
                building_something = True
       
        if not building_something:
            self.unit.get_fsm().change_state(WorkerIdleState(self.unit))
    