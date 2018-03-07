from states.state import State
from states.units.robots.ranger.sensing_enemies import SensingEnemies


class StandByAndSenseEnemyState(State):

    # TODO: move around
    def run(self) -> None:
        if SensingEnemies.sense_and_attack(self.entity):
            return
