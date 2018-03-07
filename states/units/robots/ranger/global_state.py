import battlecode as bc
from messages.enemy_unit_encountered import EnemyUnitEncounteredMessage
from messages.message import Message
from states.state import State
from states.units.robots.ranger.attack_unit_state import AttackUnitState
from states.units.robots.ranger.sensing_enemies import SensingEnemies


class RangerGlobalState(State):

    _NEAR_THRESHOLD = 50

    def run(self) -> None:
        pass

    def process_message(self, message: Message) -> bool:
        if isinstance(message, EnemyUnitEncounteredMessage):
            self._process_enemy_encounter_message(message)
            return True

        return False

    def _process_enemy_encounter_message(self, message: EnemyUnitEncounteredMessage):
        # TODO: god has forsaken me...
        # TODO: this if should be here but it is somehow better without it
        # if not isinstance(self.entity.get_fsm().get_current_state(), AttackUnitState):
            if self._get_distance(message.enemy_unit) < RangerGlobalState._NEAR_THRESHOLD:
                enemy_in_range = SensingEnemies.get_any_enemy_in_range(self.entity)
                if enemy_in_range is not None:
                    self.entity.get_fsm().change_state(AttackUnitState(self.entity, enemy_in_range.id))
                else:
                    self.entity.get_fsm().change_state(AttackUnitState(self.entity, message.enemy_unit.id))
            else:
                self.entity.get_fsm().change_state(AttackUnitState(self.entity, message.enemy_unit.id))

    def _get_distance(self, enemy_unit: bc.MapLocation) -> int:
        enemy_location = enemy_unit.location.map_location()
        my_location = self.entity.get_map_location()
        return abs(enemy_location.x - my_location.x) + abs(enemy_location.y - my_location.y)
