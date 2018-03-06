from typing import List

import battlecode as bc
from game.game_controller import GC
from messages.message import Message
from messages.queue_research_message import QueueResearchMessage
from states.state import State


class GlobalResearcherState(State):
    """
    Very simple researching. When we hit some fixed round number, we start some research.
    This does not support planning two researches on the same time, but we shouldn't do that because it would use too
    many resources at one time or stop units production for long time.
    """

    def __init__(self, entity):
        super().__init__(entity)
        self._research_timeline = {
            10: bc.UnitType.Ranger,
            500: bc.UnitType.Rocket
        }
        self._blocking_spending_karbonite = False

    def run(self) -> None:
        current_round = GC.get().round()
        if current_round in self._research_timeline:
            self._enqueue_research(self._research_timeline[current_round])

    def process_message(self, message: Message) -> bool:
        if message is QueueResearchMessage:
            casted_message: QueueResearchMessage = message
            self._enqueue_research_to_level(casted_message.unit_type, casted_message.level)
            return True

        return False

    def _enqueue_research_to_level(self, unit_type: bc.UnitType, level: int):
        current_level = self._get_current_research_level(unit_type)
        missing_levels = level - current_level
        if missing_levels <= 0:
            return
        else:
            self._enqueue_researches([unit_type] * missing_levels)

    def _enqueue_researches(self, unit_types: List[bc.UnitType]) -> None:
        for unit_type in unit_types:
            self._enqueue_research(unit_type)

    def _enqueue_research(self, unit_type: bc.UnitType):
        GC.get().queue_research(unit_type)

    def _get_current_research_level(self, unit_type: bc.UnitType) -> int:
        return GC.get().research_info().get_level(unit_type)
