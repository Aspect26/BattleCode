from states.units.robots.worker.idle import WorkerIdleState
from game.game_controller import GC
import battlecode as bc
from states.units.unit_state import UnitState
from entities.units.structures.factory import Factory


class BuildingState(UnitState):

    _build_direction: bc.Direction = None
    _build_location: bc.MapLocation = None
    _build_structure_type: bc.UnitType = None

    def __init__(self, unit, build_structure_type: bc.UnitType, build_direction: bc.Direction):
        super().__init__(unit)
        self._build_direction = build_direction
        self._build_structure_type = build_structure_type
        
    def enter(self):
        GC.get().blueprint(self.unit.id, self._build_structure_type, self._build_direction)
        self._build_location = bc.MapLocation(GC.get().planet(),
                                              self.unit.get_map_location().x + self._build_direction.dx(),
                                              self.unit.get_map_location().y + self._build_direction.dy())

    def run(self) -> None:
        
        #adjacent_units = GC.get().sense_nearby_units(self.unit.get_map_location(), 2)
        # building_something = False
        # for adjacent in adjacent_units:
        #    if GC.get().can_build(self.unit.id, adjacent.id):
        #        GC.get().build(self.unit.id, adjacent.id)
        #        
        #        building_something = True
        #
        # if not building_something:
        #    self.unit.get_fsm().change_state(WorkerIdleState(self.unit))
        
        unit_at_building_location = GC.get().sense_unit_at_location(self._build_location)
        if unit_at_building_location.structure_is_built():
            print(f"Worker at {self.unit.get_map_location()} is successfully done with building "
                  f"{self._build_structure_type} at {self._build_location}.")
            from entities.team import Team
            Team.instance.add_unit(unit_at_building_location)
            self.unit.get_fsm().change_state(WorkerIdleState(self.unit))

        # if self.unit.get_unit().ability_heat() == 0 and not GC.get().can_build(self.unit.id, unit_at_building_location.id):
        #    print(f"Worker at {self.unit.get_map_location()} cannot continue building {self._build_structure_type} at"
        #          f"{self._build_location}.")
        #   self.unit.get_fsm().change_state(WorkerIdleState(self.unit))
        
        try:
            GC.get().build(self.unit.id, unit_at_building_location.id)
        except Exception as e:
            pass
            # ignore for now, heat & not enough karbonite

