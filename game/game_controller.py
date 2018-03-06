import battlecode as bc
from game.karbonite_deposits import KarboniteDepositInfo


class GC:

    # TODO: rework this
    def __init__(self, game_controller: bc.GameController):
        if GC._game_controller is not None:
            # TODO: throw better exception
            raise Exception("State already set")

        GC._game_controller = game_controller
        from game.karbonite_deposits import KarboniteDeposits
        GC._karbonite_deposits = KarboniteDeposits(game_controller)
        GC._planet_map = game_controller.starting_map(game_controller.planet())

    _game_controller = None
    _karbonite_deposits = None
    _planet_map = None

    @staticmethod
    def get() -> bc.GameController:
        assert GC._game_controller is not None
        return GC._game_controller

    @staticmethod
    def get_nearest_karbonite_deposit(location) -> KarboniteDepositInfo:
        return GC._karbonite_deposits.get_nearest(location)

    @staticmethod
    def get_planet_map() -> bc.PlanetMap:
        return GC._planet_map
