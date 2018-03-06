from entities.units.robots.worker import Worker
from game.game_controller import GC
import battlecode as bc
from pathfinding.pathfinder import PathFinder
from states.team.team_state import TeamState
from states.units.robots.worker.building import BuildingState


class TeamEarlyState(TeamState):

    _num_of_sent_builders: int = 0

    def __init__(self, team):
        super().__init__(team)
        
    def run(self) -> None:
        
        if GC.get().karbonite() > 200 and self.team.factories == [] and self._num_of_sent_builders < 1\
                and len(self.team.workers) > 0:
            # Todo, should also find "best" build spot
            
            (builder, build_direction) = self._choose_best_builder(bc.UnitType.Factory)
            
            if builder is not None:
                self._num_of_sent_builders += 1
                builder.get_fsm().change_state(BuildingState(builder, bc.UnitType.Factory, build_direction))
        
        
    def _choose_best_builder(self, build_structure_type: bc.UnitType) -> (Worker, bc.Direction):
        # choose worker that is the furthest from the deposit for building
        builder = None
        build_direction = None
        max_dist = 0
        for worker in self.team.workers:

            worker_loc = worker.get_map_location()
            nearest_dep = GC.get_nearest_karbonite_deposit(worker_loc)
            path = PathFinder.get_shortest_path(worker_loc, nearest_dep.location, False)

            for direction in bc.Direction:
                if (path is None or len(path) > max_dist) and GC.get().can_blueprint(worker.id, build_structure_type, 
                                                                                     direction):
                    builder = worker
                    build_direction = direction
                    max_dist = len(path)

        return builder, build_direction

