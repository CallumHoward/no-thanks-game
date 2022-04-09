import numpy as np
import matplotlib.pyplot as plt
import logging
from game import play

agent_names = ["Alice", "Bob", "Charlie", "David"]

NUM_SAMPLES = 1000


def run():
    agents = {name: 0 for name in agent_names}
    for _ in range(NUM_SAMPLES):
        winner = play(agent_names, logging.WARNING)
        agents[winner] += 1

    print(agents)

    y_pos = np.arange(len(agents))

    plt.rcdefaults()
    fig, ax = plt.subplots()

    ax.barh(y_pos, agents.values(), align="center")
    ax.set_yticks(y_pos, labels=agents.keys())
    ax.set_xlabel("Wins")
    ax.set_title(f"Game Results ({NUM_SAMPLES} samples)")

    plt.show()


if __name__ == "__main__":
    run()
