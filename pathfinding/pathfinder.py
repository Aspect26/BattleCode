import battlecode as bc
from game.game_controller import GC
from pathfinding.node import Node


class PathFinder:

    def __init__(self):
        PathFinder.__directions = [bc.Direction.North, bc.Direction.Northeast, bc.Direction.East, bc.Direction.Southeast,
                                   bc.Direction.South, bc.Direction.Southwest, bc.Direction.West, bc.Direction.Northwest]

    @staticmethod
    def get_shortest_path(from_location: bc.MapLocation, to_location: bc.MapLocation, ignore_robots: bool):

        start = Node(from_location.x, from_location.y, bc.Direction.Center, None)

        searched_locations = set()
        searched_locations.add((from_location.x, from_location.y))

        if (from_location.x == to_location.x and from_location.y == to_location.y) \
                or not GC.get_planet_map().on_map(to_location):
            return []

        queue = [start]

        while len(queue) > 0:
            first = queue.pop(0)

            if first.x == to_location.x and first.y == to_location.y:
                return PathFinder.__build_path_from_node(first)

            for d in PathFinder.__directions:

                loc = bc.MapLocation(GC.get().planet(), first.x + d.dx(), first.y + d.dy())

                if (loc.x, loc.y) in searched_locations or not GC.get_planet_map().on_map(loc):
                    continue

                if not ignore_robots and GC.get().has_unit_at_location(loc):
                    continue

                if GC.get_planet_map().is_passable_terrain_at(loc):
                    queue.append(Node(loc.x, loc.y, d, first))
                    searched_locations.add((loc.x, loc.y))

        return [] # todo maybe some exception

    @staticmethod
    def __build_path_from_node(first: Node) -> [bc.Direction]:
        res = []

        while first.from_direction != bc.Direction.Center:
            res.append(first.from_direction)
            first = first.previous_node

        return res[::-1] # reversed
        
    
            
            
            
            
            
            
            
            
            
            
            
            
            