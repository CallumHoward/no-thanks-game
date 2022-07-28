# No Thanks Game
The game "No Thanks" written in Python and played by AIs.

## Setup
Make sure you have Git set up and then run
```bash
git clone https://github.com/CallumHoward/no-thanks-game.git
cd no-thanks-game
pip install -r requirements.txt  # To install numpy and matplotlib
```

## Usage
To run a single game:
```bash
python game.py
```

To run many games and see the stats as a graph:
```bash
python stats.py
```

## Developing
To add your own AI, simply replace one of the agent files in `/agents`. An agent is required to have a `name` (string) property and a method: `should_take` which returns a boolean `True` or `False`. See the files within `/agents` for examples.
