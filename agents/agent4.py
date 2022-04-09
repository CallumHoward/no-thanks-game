class Agent:
    def __init__(self) -> None:
        self.name = "David"

    def should_take(self, me, card, pot, other_players, deck_size) -> bool:
        if (me.must_take()):
            return True
        return False

