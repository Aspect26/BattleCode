import battlecode as bc
from messages.message import Message


class QueueResearchMessage(Message):

    def __init__(self, unit_type: bc.UnitType, level: int):
        self._unit_type = unit_type
        self._level = level

    @property
    def unit_type(self) -> bc.UnitType:
        return self._unit_type

    @property
    def level(self) -> int:
        return self._level
