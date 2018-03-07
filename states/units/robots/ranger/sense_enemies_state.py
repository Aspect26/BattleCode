from game.game_controller import GC
from messages.enemy_unit_encountered import EnemyUnitEncounteredMessage
from states.state import State
from states.units.robots.ranger.attack_unit_state import AttackUnitState
from utils import get_unit_vision_range


class SenseEnemyUnitsState(State):

    def run(self) -> None:
        vision_range = get_unit_vision_range(self.entity.get_unit().unit_type)
        from entities.team import Team
        sensed_units = GC.get().sense_nearby_units_by_team(self.entity.get_map_location(), vision_range, Team.instance.get_opposite_team())
        if len(sensed_units) > 0:
            some_sensed_unit = sensed_units[0]
            Team.instance.dispatch_message_to_all(EnemyUnitEncounteredMessage(some_sensed_unit))
            self.entity.get_fsm().change_state(AttackUnitState(self.entity, some_sensed_unit))
