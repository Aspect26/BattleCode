from game.karbonite_deposits import KarboniteDeposits
import battlecode as bc


class GC:

    # TODO: rework this
    def __init__(self, game_state):
        if GC._game_state is not None:
            # TODO: throw better exception
            raise Exception("State already set")

        GC._game_state = game_state
        GC._karbonite_deposits = KarboniteDeposits(game_state)
        GC._earth_map = game_state.starting_map(bc.Planet.Earth)

    _game_state = None
    _karbonite_deposits = None
    _earth_map = None

    @staticmethod
    def get() -> bc.GameController:
        assert GC._game_state is not None
        return GC._game_state

    @staticmethod
    def get_nearest_karbonite_deposit(location):
        return GC._karbonite_deposits.get_nearest(location)

    @staticmethod
    def get_earth_map() -> bc.PlanetMap:
        return GC._earth_map
