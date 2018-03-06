from entities.units.robots.worker import Worker
from states.units.robots.worker.idle import WorkerIdleState
from game.game_state import GC
import battlecode as bc
from states.state import State
from states.units.unit_state import UnitState


class BuildingState(UnitState):

    _build_direction : bc.Direction = None

    def __init__(self, unit, build_direction: bc.Direction):
        super().__init__(unit)
        self._build_direction = build_direction
        
    def enter(self):
        GC.get().blueprint(self.unit.id, bc.UnitType.Factory, _build_direction)

    def run(self) -> None:
        
        adjacentUnits = gc.sense_nearby_units(unit.location.map_location(), 2)
        building_something = False
        for adjacent in adjacentUnits:
            if gc.can_build(unit.id, adjacent.id):
                gc.build(unit.id, adjacent.id)
                building_something = True
       
        if not building_something:
            self.unit.get_fsm().change_state(WorkerIdleState(self.unit))
    