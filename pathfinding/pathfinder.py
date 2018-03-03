import battlecode as bc
import random


class SimplePathFinder:

    @staticmethod
    def get_next_step(from_location, to_location):
        x_diff = from_location.x - to_location.x
        y_diff = from_location.y - to_location.y

        if x_diff == 0 and y_diff == 0:
            return bc.Direction.Center
        elif x_diff > 0 and y_diff == 0:
            return bc.Direction.West
        elif x_diff < 0 and y_diff == 0:
            return bc.Direction.East
        elif x_diff == 0 and y_diff > 0:
            return bc.Direction.South
        elif x_diff > 0 and y_diff > 0:
            return bc.Direction.Southwest
        elif x_diff < 0 and y_diff > 0:
            return bc.Direction.Southeast
        elif x_diff == 0 and y_diff < 0:
            return bc.Direction.North
        elif x_diff > 0 and y_diff < 0:
            return bc.Direction.Northwest
        elif x_diff < 0 and y_diff < 0:
            return bc.Direction.Northeast
