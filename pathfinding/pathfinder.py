import battlecode as bc
from game.game_state import GC
from pathfinding.node import Node
import random

class PathFinder:

    def __init__(self):
        PathFinder.directions = [bc.Direction.North, bc.Direction.Northeast, bc.Direction.East, bc.Direction.Southeast,
                                 bc.Direction.South, bc.Direction.Southwest, bc.Direction.West, bc.Direction.Northwest]
        PathFinder.tryRotate = [0, -1, 1, -2, 2]
        
    @staticmethod
    def rotate(dir, amount) -> bc.Direction:
        ind = PathFinder.directions.index(dir)
        return PathFinder.directions[(ind + amount) % 8]
    
    @staticmethod
    def get_next_direction(from_location : bc.MapLocation, to_location : bc.MapLocation):
        # TODO REMOVE (old simple pathfinder)
        
        if from_location == to_location: 
            return bc.Direction.Center
        toward = from_location.direction_to(to_location)
        
        for tilt in PathFinder.tryRotate:
            
            d = PathFinder.rotate(toward, tilt)
            loc = bc.MapLocation(from_location.planet, from_location.x + d.dx(), from_location.y + d.dy())
          
            if GC.get_planet_map().on_map(loc) and GC.get().is_occupiable(loc):
                return d
        
        return bc.Direction.Center
    
    @staticmethod
    def get_shortest_path(from_location : bc.MapLocation, to_location : bc.MapLocation):
        
        start = Node(from_location.x, from_location.y, bc.Direction.Center, None)
        
        searched_locations = set()
        searched_locations.add((from_location.x, from_location.y))
        
        if (from_location.x == to_location.x and from_location.y == to_location.y) or not GC.get_planet_map().on_map(to_location):
            return []
        
        queue = [start]
        
        while len(queue) > 0:
            first = queue.pop(0)

            if first.x == to_location.x and first.y == to_location.y:
                return PathFinder._build_path_from_node(first)
            
            toward = from_location.direction_to(to_location)
            for tilt in PathFinder.tryRotate:

                d = PathFinder.rotate(toward, tilt)
                
                loc = bc.MapLocation(GC.get().planet(), first.x + d.dx(), first.y + d.dy())

                if (loc.x, loc.y) in searched_locations or not GC.get_planet_map().on_map(loc):
                    continue
                    
                if GC.get_planet_map().is_passable_terrain_at(loc):
                    queue.append(Node(loc.x, loc.y, d, first))
                    searched_locations.add((loc.x, loc.y))
        
        return [] # todo maybe some exception    
                
    @staticmethod
    def _build_path_from_node(first: Node) -> [bc.Direction]:
        res = []
        
        while first.from_direction != bc.Direction.Center:
            res.append(first.from_direction)
            first = first.previous_node
            
        return res[::-1] # reversed
        
    
            
            
            
            
            
            
            
            
            
            
            
            
            