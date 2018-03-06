from entities.units.robots.worker import Worker
from game.game_state import GC
import battlecode as bc
from pathfinding.pathfinder import PathFinder
from states.team.team_state import TeamState
from states.units.robots.worker.building import BuildingState


class TeamEarlyState(TeamState):

    _num_of_sent_builders: int = 0

    def __init__(self, team):
        super().__init__(team)
        
    def run(self) -> None:
        
        if GC.get().karbonite() > 200 and self.team.factories == [] and self._num_of_sent_builders < 1:
            # Todo, should also find "best" build spot and build direction
            
            (builder, build_direction) = self._choose_best_builder(bc.UnitType.Factory)
            self._num_of_sent_builders += 1
            builder.get_fsm().change_state(BuildingState(builder, build_direction))
        
        
    def _choose_best_builder(self, build_structure_type: bc.UnitType) -> (Worker, bc.Direction):
        # choose worker that is the furthest from the deposit for building
        builder = self.team.workers[0]
        max_dist = 0
        for worker in self.team.workers:

            worker_loc = worker.get_map_location()
            nearest_dep = GC.get_nearest_karbonite_deposit(worker_loc)
            path = PathFinder.get_shortest_path(worker_loc, nearest_dep.location, False)

            if path is None:
                return builder

            if len(path) > max_dist:
                builder = worker
                max_dist = len(path)

            

