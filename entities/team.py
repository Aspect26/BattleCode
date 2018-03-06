import battlecode as bc
from entities.entity import Entity
from entities.units.robots.worker import Worker
from entities.units.robots.mage import Mage
from entities.units.robots.knight import Knight
from entities.units.robots.ranger import Ranger
from entities.units.structures.factory import Factory
from entities.units.unit import Unit
from game.game_controller import GC
from messages.message import Message
from states.team.global_state import TeamGlobalState
from states.team.initial_state import TeamInitialState


class Team(Entity):

    units: [Unit] = []

    workers: [Worker] = []
    mages: [Mage] = []
    rangers: [Ranger] = []
    knights: [Knight] = []
    factories: [Factory] = []
    # Don't kill me please
    instance = None

    def __init__(self):
        super().__init__(TeamInitialState(self), TeamGlobalState(self))
        instance = self
        for bc_unit in GC.get().my_units():
            if (bc_unit.unit_type == bc.UnitType.Worker):
                unit = Worker(bc_unit)
                self.workers.append(unit)
            elif (bc_unit.unit_type == bc.UnitType.Ranger):
                unit = Ranger(bc_unit)
                self.rangers.append(unit)
            elif (bc_unit.unit_type == bc.UnitType.Mage):
                unit = Mage(bc_unit)
                self.mages.append(unit)
            elif (bc_unit.unit_type == bc.UnitType.Knight):
                unit = Knight(bc_unit)
                self.knights.append(unit)

            self.units.append(unit)

    def perform_unit_actions(self):
        for unit in self.units:
            unit.get_fsm().update()

    def send_message_to_factories(self, message: Message):
        for factory in Team.factories:
            factory.get_fsm().process_message(message)
