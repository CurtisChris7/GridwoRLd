from demo_constants.demo_racetrack_data import DISCOUNT
from gridworld_constants import *

ACTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

DISCOUNT = 0.95
STEP_REWARD = 0
FINISH_REWARD = 1

DEMO_MAZE_SCHEMA = [
    [(UNUSED, 7), (WALL, 1), (GOAL, 1)],
    [(UNUSED, 2), (WALL, 1), (UNUSED, 4), (WALL, 1), (UNUSED, 1)],
    [(START, 1), (UNUSED, 1), (WALL, 1), (UNUSED, 4), (WALL, 1), (UNUSED, 1)],
    [(UNUSED, 2), (WALL, 1), (UNUSED, 6)],
    [(UNUSED, 5), (WALL, 1), (UNUSED, 3)],
    [(UNUSED, 9)],
]
