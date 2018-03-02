class GC:

    # TODO: rework this
    def __init__(self, game_state):
        if GC._game_state is not None:
            # TODO: throw better exception
            raise Exception("State already set")

        GC._game_state = game_state

    _game_state = None

    @staticmethod
    def get():
        assert GC._game_state is not None
        return GC._game_state
