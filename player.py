import logging


class Player:
    def __init__(self, player_number):
        self.id = player_number  # Starting from 0
        self.coins = 11
        self.played_cards = []

    def must_take(self) -> bool:
        return self.coins <= 0

    def should_take(
        self, card: int, pot: int, other_players: list["Player"], deck_size: int
    ) -> bool:
        return self.must_take()

    def take_card(self, card, pot) -> None:
        self.played_cards.append(card)
        self.coins += pot

    def not_take_card(self) -> None:
        logging.info(f"Player {self.id} has {self.coins} coins")
        self.coins -= 1
