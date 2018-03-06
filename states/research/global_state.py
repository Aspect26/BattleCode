from typing import List

import battlecode as bc
from entities.team import Team
from game.game_controller import GC
from messages.block_karbonite_usage import BlockKarboniteMessage
from messages.message import Message
from messages.queue_research_message import QueueResearchMessage
from messages.unblock_karbonite_usage import UnblockKarboniteMessage
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
        self._check_research_timeline()
        if GC.get().research_info().has_next_in_queue():
            if not self._has_enough_karbonite_for_next_research():
                self._start_blocking_karbonite()
        elif self._blocking_spending_karbonite:
            self._stop_blocking_karbonite()

    def process_message(self, message: Message) -> bool:
        if message is QueueResearchMessage:
            casted_message: QueueResearchMessage = message
            self._enqueue_research_to_level(casted_message.unit_type, casted_message.level)
            return True

        return False

    def _check_research_timeline(self):
        current_round = GC.get().round()
        if current_round in self._research_timeline:
            self._enqueue_research(self._research_timeline[current_round])

    def _enqueue_research_to_level(self, unit_type: bc.UnitType, level: int):
        current_level = self._get_current_research_level(unit_type)
        missing_levels = level - current_level
        if missing_levels <= 0:
            return
        else:
            self._enqueue_researches([unit_type] * missing_levels)

    def _enqueue_researches(self, unit_type: List[bc.UnitType]) -> None:
        self._research_queue.extend(unit_type)

    def _enqueue_research(self, unit_type: bc.UnitType):
        GC.get().queue_research(unit_type)

    def _has_enough_karbonite_for_next_research(self) -> bool:
        research_cost = self._get_next_research_cost()
        current_karbonite = GC.get().karbonite()
        return research_cost < current_karbonite

    def _get_next_research_cost(self) -> int:
        research_unit = GC.get().research_info().next_in_queue()
        level_to_research = GC.get().research_info().get_level(research_unit) + 1
        return bc.cost_of(research_unit, level_to_research)

    def _get_current_research_level(self, unit_type: bc.UnitType) -> int:
        return GC.get().research_info().get_level(unit_type)

    def _start_blocking_karbonite(self):
        Team.instance.send_message_to_factories(BlockKarboniteMessage())
        self._blocking_spending_karbonite = True

    def _stop_blocking_karbonite(self):
        Team.instance.send_message_to_factories(UnblockKarboniteMessage())
        self._blocking_spending_karbonite = False
