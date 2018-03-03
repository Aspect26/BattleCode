from typing import List

from entities.entity import Entity
from entities.units.robots.worker import Worker
from game_state import GC
from states.team.global_state import TeamGlobalState
from states.team.initial_state import TeamInitialState


class Team(Entity):

    def __init__(self):
        super().__init__(TeamInitialState(self), TeamGlobalState(self))
        # TODO: add initial workers
        self._entities: List[Entity] = []
        for unit in GC.get().my_units():
            self._entities.append(Worker(unit.id))

    def perform_entity_actions(self):
        for entity in self._entities:
            entity.get_fsm().update()
