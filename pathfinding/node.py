import battlecode as bc


class Node:

    def __init__(self, x: int, y: int, from_direction: bc.Direction, previous_node):
        self.x = x
        self.y = y
        self.from_direction = from_direction
        self.previous_node = previous_node
