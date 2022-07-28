import random
import logging


class Agent:
    def __init__(self) -> None:
        self.name = "Alice"

    def should_take(self, me, card, pot, other_players, deck_size) -> bool:
        if me.must_take():
            return True

        if pot > card - 2:
            return True

        if random.randint(0, 8) == 0:
            logging.info(f"{me.identify()} took a card on a whim")
            return True

        return False
