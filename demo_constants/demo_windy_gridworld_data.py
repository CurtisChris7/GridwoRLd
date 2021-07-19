from demo_constants.demo_racetrack_data import DISCOUNT, REWARD
from gridworld_constants import *

# All possible actions
ACTIONS = [(-1, -1), (-1, 0), (0, -1), (-1, 1),
           (0, 0), (1, -1), (0, 1), (1, 0), (1, 1)]

# Constant step penalty
REWARD = -1

DISCOUNT = 1
ALPHA = 0.05

# Schema used for creating a gridlworld
GRIDWORLD_SCHEMA = [
    [(OPEN, 10)],
    [(OPEN, 10)],
    [(OPEN, 10)],
    [(START, 1), (OPEN, 6), (GOAL, 1), (OPEN, 2)],
    [(OPEN, 10)],
    [(OPEN, 10)],
    [(OPEN, 10)],
]

# Maps the displacement due to wind by column
COL_TO_WIND = {
    0: 0,
    1: 0,
    2: 0,
    3: 1,
    4: 1,
    5: 1,
    6: 2,
    7: 2,
    8: 1,
    9: 0
}
