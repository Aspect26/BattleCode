from states.state import State


class AttackUnitState(State):

    def __init__(self, entity, unit_to_attack):
        super().__init__(entity)
        self._unit_to_attack = unit_to_attack

    def run(self):
        # TODO: implement me
        pass
