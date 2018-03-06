from game.game_state import GC
import battlecode as bc
from pathfinding.pathfinder import PathFinder
from game.karbonite_deposits import KarboniteDepositInfo
from states.units.unit_state import UnitState


class GoingToNearestKarboniteDepositState(UnitState):

    _deposit : KarboniteDepositInfo = None
    _path : [bc.Direction] = []

    def __init__(self, entity):
        super().__init__(entity)

    def run(self) -> None:
        location = self.entity.get_map_location()
        
        direction_to_deposit = location.direction_to(self._deposit.location)
        
        if (location == self._deposit.location or location.is_adjacent_to(self._deposit.location)):
            
            self._deposit.observed_karbonite = GC.get().karbonite_at(self._deposit.location)
            if (self._deposit.observed_karbonite > 0):
                self._start_harvesting(direction_to_deposit)
                return
        
        if (self._deposit.observed_karbonite <= 0):
            self._update_deposit() # todo change to some other state if there isn't avaible deposit
            if (self._deposit.observed_karbonite <= 0):
                from states.units.robots.worker.idle import WorkerIdleState
                self.entity.get_fsm().change_state(WorkerIdleState)

        if self._path == [] or not GC.get().can_move(self.unit.id, self._path[0]):
            # print(f"Stucked trying to get from {location} to {self._deposit.location}, path = {self._path}")
            self._path = PathFinder.get_shortest_path(location, self._deposit.location, False)
        
        if (self.unit.get_unit().movement_heat() < 10 and self._path != []):
            next_dir = self._path.pop(0)
            GC.get().move_robot(self.unit.id, next_dir)


    def enter(self):
        self._update_deposit()
        
    def _update_deposit(self):
        self._deposit = GC.get_nearest_karbonite_deposit(self.entity.get_map_location())

    def _start_harvesting(self, direction):
        from states.units.robots.worker.harvesting import HarvestingState
        self.entity.get_fsm().change_state(HarvestingState(self.entity, self._deposit, direction))

    def _distance(self, location1, location2):
        return "FROM:" + str(location1.x) + ":" + str(location1.y) + \
               ", TO: " + str(location2.x) + ":" + str(location2.y) + \
               ", DISTANCE: " + str(location1.x - location2.x) + ":" + str(location1.y - location2.y)
