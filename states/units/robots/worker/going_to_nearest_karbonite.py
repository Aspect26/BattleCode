from game.game_state import GC
from pathfinding.pathfinder import PathFinder
from states.units.unit_state import UnitState

class GoingToNearestKarboniteDepositState(UnitState):

    def __init__(self, entity):
        super().__init__(entity)
        self._deposit = None
        self._path = []

    def run(self) -> None:
        location = self.entity.get_map_location()
        
        direction_to_deposit = location.direction_to(self._deposit.location)
        
        if (GC.get_planet_map().initial_karbonite_at(location) or location.is_adjacent_to(self._deposit.location))\
                and GC.get().karbonite_at(self._deposit.location) > 0:
            self._start_harvesting(direction_to_deposit)
            return
        
        if self._path == [] or not GC.get().can_move(self.unit.id, self._path[0]): 
            self._path = PathFinder.get_shortest_path(location, self._deposit.location, False)
        
        if (self.unit.get_unit().movement_heat() < 10 and self._path != []):
            next_dir = self._path.pop(0)
            GC.get().move_robot(self.unit.id, next_dir)


    def enter(self):
        self._deposit = GC.get_nearest_karbonite_deposit(self.entity.get_map_location())

    def _start_harvesting(self, direction):
        from states.units.robots.worker.harvesting import HarvestingState
        self.entity.get_fsm().change_state(HarvestingState(self.entity, self._deposit, direction))

    def _distance(self, location1, location2):
        return "FROM:" + str(location1.x) + ":" + str(location1.y) + \
               ", TO: " + str(location2.x) + ":" + str(location2.y) + \
               ", DISTANCE: " + str(location1.x - location2.x) + ":" + str(location1.y - location2.y)
