from entities.units.structures.factory import Factory
from states.state import State


class GlobalFactoryState(State):

    def __init__(self, factory_entity: Factory):
        super().__init__(factory_entity)
        self._blocked_state: State = None

    def run(self) -> None:
        pass
