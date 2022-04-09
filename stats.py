import numpy as np
import matplotlib.pyplot as plt
import logging
from game import play
from agents.agent1 import Agent as Agent1
from agents.agent2 import Agent as Agent2
from agents.agent3 import Agent as Agent3
from agents.agent4 import Agent as Agent4

NUM_SAMPLES = 1000


def run():
    agents = [Agent1(), Agent2(), Agent3(), Agent4()]
    agent_names = [agent.name for agent in agents]

    agent_wins = {name: 0 for name in agent_names}
    for _ in range(NUM_SAMPLES):
        winner = play(agents, logging.WARNING)
        agent_wins[winner] += 1

    print(agent_wins)

    y_pos = np.arange(len(agent_wins))

    plt.rcdefaults()
    fig, ax = plt.subplots()

    ax.barh(y_pos, agent_wins.values(), align="center")
    ax.set_yticks(y_pos, labels=agent_wins.keys())
    ax.set_xlabel("Wins")
    ax.set_title(f"Game Results ({NUM_SAMPLES} samples)")

    plt.show()


if __name__ == "__main__":
    run()
