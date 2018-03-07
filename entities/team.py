import battlecode as bc
from entities.entity import Entity
from entities.researcher import Researcher
from entities.units.robots.worker import Worker
from entities.units.robots.mage import Mage
from entities.units.robots.knight import Knight
from entities.units.robots.ranger import Ranger
from entities.units.structures.factory import Factory
from entities.units.structures.rocket import Rocket
from entities.units.unit import Unit
from game.game_controller import GC
from messages.message import Message
from states.team.global_state import TeamGlobalState
from states.team.early import TeamEarlyState


class Team(Entity):

    # TODO: omg this is fucked up, we declare these static properties, but the use the instance and its instance properties
    units: [Unit] = {}

    workers: [Worker] = []
    mages: [Mage] = []
    rangers: [Ranger] = []
    knights: [Knight] = []

    factories: [Factory] = []
    rockets: [Rocket] = []
    instance = None

    def __init__(self):
        super().__init__(TeamEarlyState(self), TeamGlobalState(self))
        Team.instance = self
        
        for bc_unit in GC.get().my_units():
            self.add_unit(bc_unit)

        if GC.get().planet() == bc.Planet.Earth:
            self.units[-1] = Researcher()

    def perform_actions(self):
        self.get_fsm().update()
        
        for unit in GC.get().my_units():
            unit_id = unit.id
            if unit_id not in self.units:
                self.add_unit(unit)

            self.units[unit_id].get_fsm().update()

    # TODO: move this to message dispatcher
    def send_message_to_factories(self, message: Message):
        for factory in self.factories:
            factory.get_fsm().process_message(message)

    def add_unit(self, bc_unit):
        if bc_unit.unit_type == bc.UnitType.Worker:
            unit = Worker(bc_unit)
            self.workers.append(unit)
        elif bc_unit.unit_type == bc.UnitType.Ranger:
            unit = Ranger(bc_unit)
            self.rangers.append(unit)
        elif bc_unit.unit_type == bc.UnitType.Mage:
            unit = Mage(bc_unit)
            self.mages.append(unit)
        elif bc_unit.unit_type == bc.UnitType.Knight:
            unit = Knight(bc_unit)
            self.knights.append(unit)
        elif bc_unit.unit_type == bc.UnitType.Factory:
            unit = Factory(bc_unit)
            self.factories.append(unit)
        elif bc_unit.unit_type == bc.UnitType.Rocket:
            unit = Rocket(bc_unit)
            self.rockets.append(unit)
        else:
            raise Exception("[Team] Creating unit of non unit type: {0}".format(str(bc_unit.UnitType)))

        self.units[bc_unit.id] = unit
