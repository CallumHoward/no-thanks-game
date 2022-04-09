import logging
from utilities import lowest_consecutive


class Player:
    def __init__(self, player_number: int, agent):
        self.id = player_number  # Starting from 0
        self.name = agent.name
        self.coins = 11
        self.played_cards: list[int] = []
        self.agent = agent

    def must_take(self) -> bool:
        return self.coins <= 0

    def should_take(
        self, card: int, pot: int, other_players: list["Player"], deck_size: int
    ) -> bool:
        agent_play = self.agent.should_take(self, card, pot, other_players, deck_size)

        if self.must_take() and agent_play != True:
            logging.warning(f"{self.identify()} attempted to skip with no coins")

        return self.must_take() or agent_play

    def take_card(self, card, pot) -> None:
        self.played_cards.append(card)
        self.played_cards.sort()
        logging.info(f"Player {self.id} has {self.played_cards} cards")
        self.coins += pot
        logging.info(f"Player {self.id} has {self.coins} coins")

    def not_take_card(self) -> None:
        logging.info(f"Player {self.id} has {self.coins} coins")
        self.coins -= 1

    def score(self) -> int:
        return sum(lowest_consecutive(self.played_cards)) - self.coins

    def identify(self) -> str:
        return f"Player {self.id} ({self.name})"
