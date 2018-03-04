import battlecode as bc
from game.game_state import GC
import random


class SimplePathFinder:

    def __init__(self):
        SimplePathFinder.directions = [bc.Direction.North, bc.Direction.Northeast, bc.Direction.East, bc.Direction.Southeast,
                  bc.Direction.South, bc.Direction.Southwest, bc.Direction.West, bc.Direction.Northwest]
        SimplePathFinder.tryRotate = [0, -1, 1, -2, 2]
        
    @staticmethod
    def rotate(dir, amount) -> bc.Direction:
        ind = SimplePathFinder.directions.index(dir)
        return SimplePathFinder.directions[(ind + amount) % 8]
    
    @staticmethod
    def get_next_direction(from_location : bc.MapLocation, to_location : bc.MapLocation):
        
        if from_location == to_location: 
            return bc.Direction.Center
        
        toward = from_location.direction_to(to_location)
        
        for tilt in SimplePathFinder.tryRotate:
            
            d = SimplePathFinder.rotate(toward, tilt)
            loc = bc.MapLocation(from_location.planet, from_location.x + d.dx(), from_location.y + d.dy())
          
            if GC.get_earth_map().on_map(loc) and GC.get().is_occupiable(loc):
                return d
        
        return bc.Direction.Center