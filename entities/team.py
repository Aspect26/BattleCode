import battlecode as bc
from entities.entity import Entity
from entities.units.robots.worker import Worker
from entities.units.robots.mage import Mage
from entities.units.robots.knight import Knight
from entities.units.robots.ranger import Ranger
from entities.units.structures.factory import Factory
from entities.units.structures.rocket import Rocket
from entities.units.unit import Unit
from game.game_state import GC
from states.team.global_state import TeamGlobalState
from states.team.early import TeamEarlyState


class Team(Entity):

    units: [Unit] = []

    workers: [Worker] = []
    mages: [Mage] = []
    rangers: [Ranger] = []
    knights: [Knight] = []
    
    factories: [Factory] = []
    rockets: [Rocket] = []

    def __init__(self):

        # todo remove team initial state (not necessary and we want to run TeamEarlyState in the first turn)
        super().__init__(TeamEarlyState(self), TeamGlobalState(self)) 
        
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

    def perform_actions(self):
        
        self.get_fsm().update()
        
        for unit in self.units:
            unit.get_fsm().update()
