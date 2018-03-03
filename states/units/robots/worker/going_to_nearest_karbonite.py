from game.game_state import GC
from pathfinding.pathfinder import SimplePathFinder
from states.state import State


class GoingToNearestKarboniteDepositState(State):

    def __init__(self, entity):
        super().__init__(entity)
        self._deposit = None

    def run(self) -> None:
        location = self.entity.get_map_location()
        direction = SimplePathFinder.get_next_step(location, self._deposit.location)

        if location.is_adjacent_to(self._deposit.location):
            self._start_harvesting(direction)
            return

        try:
            GC.get().move_robot(self.entity.id, direction)
        except:
            return

        if location.is_adjacent_to(self._deposit.location):
            self._start_harvesting(direction)

    def enter(self):
        self._deposit = GC.get_nearest_karbonite_deposit(self.entity.get_map_location())

    def _start_harvesting(self, direction):
        from states.units.robots.worker.harvesting import HarvestingState
        self.entity.get_fsm().change_state(HarvestingState(self.entity, self._deposit, direction))

    def _distance(self, location1, location2):
        return "FROM:" + str(location1.x) + ":" + str(location1.y) + \
               ", TO: " + str(location2.x) + ":" + str(location2.y) + \
               ", DISTANCE: " + str(location1.x - location2.x) + ":" + str(location1.y - location2.y)
