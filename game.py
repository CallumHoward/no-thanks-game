import logging
from random import shuffle, choice
from itertools import cycle
from player import Player
from utilities import rotate
from agents.agent1 import Agent as Agent1
from agents.agent2 import Agent as Agent2
from agents.agent3 import Agent as Agent3
from agents.agent4 import Agent as Agent4

root = logging.getLogger()
logging.basicConfig(format="[%(relativeCreated)04d:%(module)s] %(message)s")

agent_instances = [Agent1(), Agent2(), Agent3(), Agent4()]
all_cards = list(range(3, 35))
num_cards_to_remove = 9


def play(agents, log_level = logging.INFO) -> str:
    root.setLevel(log_level)
    logging.info("Setting up")
    deck = all_cards
    shuffle(deck)
    deck = deck[:num_cards_to_remove]
    players = list(Player(i, agent) for i, agent in enumerate(agents))

    current_player = choice(players)
    pot = 0

    logging.info("Starting game")
    while len(deck) != 0:
        dealt_card = deck.pop()
        logging.info(f"Card dealt: {dealt_card}")

        for player in cycle(rotate(players, current_player.id)):
            current_player = player
            logging.info(f"Current player: {current_player.id}, Pot: {pot}, Card: {dealt_card}")
            other_players = [player for player in players if player != current_player]

            if current_player.should_take(dealt_card, pot, other_players, len(deck)):
                logging.info(f"{current_player.identify()} takes {dealt_card}")
                current_player.take_card(dealt_card, pot)
                pot = 0
                break
            else:
                logging.info(f"{current_player.identify()} does not take {dealt_card}")
                current_player.not_take_card()
                pot += 1

    logging.info("Game finished")
    scores = sorted(((player, player.score()) for player in players), key=lambda x: x[1])
    for (player, score) in scores:
        logging.info(f"{player.identify()} scored {score}")

    winner = scores[0][0].name
    logging.info(f"Winner was {winner}")

    return winner

if __name__ == "__main__":
    play(agent_instances)
