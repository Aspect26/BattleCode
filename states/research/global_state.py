import battlecode as bc
from entities.team import Team
from game.game_controller import GC
from messages.block_karbonite_usage import BlockKarboniteMessage
from messages.unblock_karbonite_usage import UnblockKarboniteMessage
from states.state import State


class GlobalResearcherState(State):
    """
    Very simple researching. When we hit some fixed round number, we start some research.
    """

    def __init__(self, entity):
        super().__init__(entity)
        self._research_timeline = {
            10: bc.UnitType.Ranger,
            500: bc.UnitType.Rocket
        }
        self._research_queue = []
        self._blocking_spending_karbonite = False

    def run(self) -> None:
        self._check_research_timeline()
        if self._has_queued_research():
            if self._has_enough_karbonite_for_next_research():
                self._queue_next_research()
            else:
                self._start_blocking_karbonite()
        elif self._blocking_spending_karbonite:
            self._stop_blocking_karbonite()

    def _check_research_timeline(self):
        current_round = GC.get().round()
        if current_round in self._research_timeline:
            self._research_queue.append(self._research_timeline[current_round])

    def _has_queued_research(self) -> bool:
        return len(self._research_queue) > 0

    def _has_enough_karbonite_for_next_research(self) -> bool:
        research_cost = self._get_next_research_cost()
        current_karbonite = GC.get().karbonite()
        return research_cost < current_karbonite

    def _queue_next_research(self):
        next_research = self._research_queue[0]
        if not GC.get().queue_research(next_research):
            print("ERROR: Could not research {0}".format(next_research))

    def _start_blocking_karbonite(self):
        Team.instance.send_message_to_factories(BlockKarboniteMessage())
        self._blocking_spending_karbonite = True

    def _stop_blocking_karbonite(self):
        Team.instance.send_message_to_factories(UnblockKarboniteMessage())
        self._blocking_spending_karbonite = False

    def _get_next_research_cost(self) -> int:
        research_unit = self._research_queue[0]
        level_to_research = GC.get().research_info().get_level() + 1
        return bc.cost_of(research_unit, level_to_research)

