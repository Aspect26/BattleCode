import battlecode as bc


class GC:

    # TODO: rework this
    def __init__(self, game_state: bc.GameController):
        if GC._game_state is not None:
            # TODO: throw better exception
            raise Exception("State already set")

        GC._game_state = game_state
        from game.karbonite_deposits import KarboniteDeposits
        GC._karbonite_deposits = KarboniteDeposits(game_state)
        GC._planet_map = game_state.starting_map(game_state.planet())

    _game_state = None
    _karbonite_deposits = None
    _planet_map = None

    @staticmethod
    def get() -> bc.GameController:
        assert GC._game_state is not None
        return GC._game_state

    @staticmethod
    def get_nearest_karbonite_deposit(location):
        return GC._karbonite_deposits.get_nearest(location)

    @staticmethod
    def get_planet_map() -> bc.PlanetMap:
        return GC._planet_map
