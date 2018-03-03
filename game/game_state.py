from game.karbonite_deposits import KarboniteDeposits


class GC:

    # TODO: rework this
    def __init__(self, game_state):
        if GC._game_state is not None:
            # TODO: throw better exception
            raise Exception("State already set")

        GC._game_state = game_state
        GC._karbonite_deposits = KarboniteDeposits(game_state)

    _game_state = None
    _karbonite_deposits = None

    @staticmethod
    def get():
        assert GC._game_state is not None
        return GC._game_state

    @staticmethod
    def get_nearest_karbonite_deposit(location):
        return GC._karbonite_deposits.get_nearest(location)
