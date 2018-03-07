import battlecode as bc
from game.game_controller import GC
from pathfinding.pathfinder import PathFinder
from states.state import State
from states.units.robots.ranger.sensing_enemies import SensingEnemies
from states.units.robots.ranger.stand_by_state import StandByAndSenseEnemyState


class MoveToAndSenseEnemiesState(State):

    _STUCK_THRESHOLD = 5

    def __init__(self, entity, location: bc.MapLocation):
        super().__init__(entity)
        self._moving_to_location = location
        self._route = []
        self._stuck_for = 0

    def run(self) -> None:
        if SensingEnemies.sense_and_attack(self.entity):
            return

        if len(self._route) == 0:
            self.entity.get_fsm().change_state(StandByAndSenseEnemyState(self.entity))
            return

        next_step = self._route[0]
        if GC.get().can_move(self.entity.id, next_step):
            if self.entity.get_unit().movement_heat() < 10:
                GC.get().move_robot(self.entity.id, next_step)
                self._route = self._route[1:]
                self._stuck_for = 0
        else:
            self._stuck_for += 1
            if self._stuck_for > MoveToAndSenseEnemiesState._STUCK_THRESHOLD:
                print("[MoveToAndSenseEnemyState] entity stuck")
                self._recompute_route(False)

    def enter(self):
        self._recompute_route(True)

    def _recompute_route(self, ignore_robots):
        self._route = PathFinder.get_shortest_path(self.entity.get_map_location(), self._moving_to_location, ignore_robots)
