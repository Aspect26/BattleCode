import battlecode as bc
from game.game_controller import GC
from states.state import State
from states.units.structures.factory.unload_when_possible import UnloadingWhenPossibleState


class GlobalFactoryState(State):

    def __init__(self, factory_entity):
        super().__init__(factory_entity)
        self._produced_units = 0

    def run(self) -> None:
        unit_type = self._get_unit_type_to_produce()
        if GC.get().can_produce_robot(self.entity.id, unit_type):
            GC.get().produce_robot(self.entity.id, unit_type)
            self.entity.get_fsm().change_state(UnloadingWhenPossibleState(self.entity))

    def _get_unit_type_to_produce(self) -> bc.UnitType:
        # TODO: it would be better to redirect call to Team which will decide who to create next based on proportion of living rangers and healers since we will be creating only them for now
        return bc.UnitType.Ranger
