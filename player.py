import logging

def lowest_consecutive(list: list[int]) -> list[int]:
    return [item for i, item in enumerate(sorted(list)) if i != len(list) - 1 and item + 1 != list[i + 1]]

class Player:
    def __init__(self, player_number: int, name: str):
        self.id = player_number  # Starting from 0
        self.name = name
        self.coins = 11
        self.played_cards: list[int] = []

    def must_take(self) -> bool:
        return self.coins <= 0

    def should_take(
        self, card: int, pot: int, other_players: list["Player"], deck_size: int
    ) -> bool:
        return self.must_take()

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
