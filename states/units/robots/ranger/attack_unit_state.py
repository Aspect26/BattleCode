import battlecode as bc
from game.game_controller import GC
from states.state import State


class AttackUnitState(State):

    def __init__(self, entity, unit_id):
        super().__init__(entity)
        self._target_id = unit_id

    # TODO: move around
    def run(self):
        from states.units.robots.ranger.sensing_enemies import SensingEnemies
        visible_enemies = SensingEnemies.sense_enemies(self.entity)

        if len(visible_enemies) == 0:
            from entities.team import Team
            from states.units.robots.ranger.move_to_state import MoveToAndSenseEnemiesState
            self.entity.get_fsm().change_state(MoveToAndSenseEnemiesState(self.entity, Team.instance.get_next_patrol_location()))
            return

        # if my target is not visible change my target to nearest and try shoot it, if visible but out of range, shoot at nearest but still pursue it, if in range, shoot it
        attackable_enemy = None
        my_target_visible = False
        my_target_unit = None
        for visible_enemy in visible_enemies:
            if visible_enemy.id == self._target_id:
                my_target_visible = True
                my_target_unit = visible_enemy
            if GC.get().can_attack(self.entity.id, visible_enemy.id):
                attackable_enemy = visible_enemy

        if attackable_enemy is None:
            # TODO: it is not attackable but "random" visible then
            attackable_enemy = visible_enemies[0]

        if not my_target_visible:
            self._target_id = attackable_enemy.id
            if not self._try_shoot_at(self._target_id):
                self._move_towards_target(attackable_enemy)
        else:
            if not self._try_shoot_at(self._target_id):
                if not self._try_shoot_at(attackable_enemy.id):
                    self._move_towards_target(my_target_unit)

    def _try_shoot_at(self, enemy_id: int) -> bool:
        if GC.get().can_attack(self.entity.id, enemy_id) and GC.get().is_attack_ready(self.entity.id):
            GC.get().attack(self.entity.id, enemy_id)
            return True
        return False

    def _move_towards_target(self, target: bc.Unit) -> None:
        if GC.get().is_move_ready(self.entity.id):
            enemy_direction = self.entity.get_map_location().direction_to(target.location.map_location())
            if GC.get().can_move(self.entity.id, enemy_direction):
                GC.get().move_robot(self.entity.id, enemy_direction)
            # TODO: else find path to him

    def _get_distance_to_enemy(self, enemy: bc.Unit) -> int:
        enemy_location = enemy.location.map_location()
        my_location = self.entity.get_map_location()
        return abs(enemy_location.x - my_location.x) + abs(enemy_location.y - my_location.y)
