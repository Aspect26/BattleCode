from states.state import State
from states.units.robots.ranger.move_to_state import MoveToAndSenseEnemyState


class RangerInitialState(State):

    def __init__(self, entity):
        super().__init__(entity)
        self._unloaded = False

    def run(self) -> None:
        if not self.entity.get_location().is_in_garrison():
            from entities.team import Team
            self.entity.get_fsm().change_state(MoveToAndSenseEnemyState(self.entity, Team.instance.get_next_pattrol_location()))
