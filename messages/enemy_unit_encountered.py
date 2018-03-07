from messages.message import Message


class EnemyUnitEncounteredMessage(Message):

    def __init__(self, enemy_unit):
        self.enemy_unit = enemy_unit
