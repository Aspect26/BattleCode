from game.game_controller import GC
from messages.enemy_unit_encountered import EnemyUnitEncounteredMessage
from states.units.robots.ranger.attack_unit_state import AttackUnitState
from utils import get_unit_vision_range


# TODO: rename + move to somewhere else
class SensingEnemies:

    @staticmethod
    def sense_and_attack(entity) -> bool:
        vision_range = get_unit_vision_range(entity.get_unit().unit_type)
        from entities.team import Team
        sensed_units = GC.get().sense_nearby_units_by_team(entity.get_map_location(), vision_range, Team.instance.get_opposite_team())
        if len(sensed_units) > 0:
            some_sensed_unit = sensed_units[0]
            Team.instance.dispatch_message_to_all(EnemyUnitEncounteredMessage(some_sensed_unit))
            entity.get_fsm().change_state(AttackUnitState(entity, some_sensed_unit.id))
            return True

        return False

    @staticmethod
    def sense_enemies(entity):
        vision_range = get_unit_vision_range(entity.get_unit().unit_type)
        from entities.team import Team
        return GC.get().sense_nearby_units_by_team(entity.get_map_location(), vision_range, Team.instance.get_opposite_team())

    @staticmethod
    def attack_at_random_enemy(entity):
        if not GC.get().is_attack_ready(entity.id):
            return

        vision_range = get_unit_vision_range(entity.get_unit().unit_type)
        from entities.team import Team
        visible_enemies = GC.get().sense_nearby_units_by_team(entity.get_map_location(), vision_range, Team.instance.get_opposite_team())
        for visible_enemy in visible_enemies:
            if GC.get().can_attack(visible_enemy.id):
                GC.get().attack(entity.id, visible_enemy.id)

    @staticmethod
    def get_any_enemy_in_range(entity):
        vision_range = get_unit_vision_range(entity.get_unit().unit_type)
        from entities.team import Team
        visible_enemies = GC.get().sense_nearby_units_by_team(entity.get_map_location(), vision_range, Team.instance.get_opposite_team())
        for visible_enemy in visible_enemies:
            if GC.get().can_attack(entity.id, visible_enemy.id):
                return visible_enemy

        return None
