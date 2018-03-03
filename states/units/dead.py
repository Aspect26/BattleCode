from states.state import State


class DeadState(State):

    def run(self) -> None:
        return

    def enter(self):
        return
        # TODO: send message maybe?
