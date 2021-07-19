from gridworld_constants import *

# All legal actions
ACTIONS = [(-1, -1), (-1, 0), (0, -1), (-1, 1),
           (0, 0), (1, -1), (0, 1), (1, 0), (1, 1)]

MAX_VELOCITY = 5  # Top speed in any direction
DISCOUNT = 1  # No discounting will occur

# Constant Rewards
REWARD = -1
FAIL_REWARD = -100  # Chosen to more strongly prune away from starting over

# Schema used for a demo racetrack
DEMO_RACETRACK_SCHEMA = [
    [(UNUSED, 3), (OPEN, 13), (GOAL, 1)],
    [(UNUSED, 2), (OPEN, 14), (GOAL, 1)],
    [(UNUSED, 2), (OPEN, 14), (GOAL, 1)],
    [(UNUSED, 1), (OPEN, 15), (GOAL, 1)],
    [(OPEN, 16), (GOAL, 1)],
    [(OPEN, 10), (UNUSED, 7)],

    [(OPEN, 9), (UNUSED, 8)],
    [(OPEN, 9), (UNUSED, 8)],
    [(OPEN, 9), (UNUSED, 8)],
    [(OPEN, 9), (UNUSED, 8)],
    [(OPEN, 9), (UNUSED, 8)],
    [(OPEN, 9), (UNUSED, 8)],
    [(OPEN, 9), (UNUSED, 8)],

    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],
    [(UNUSED, 1), (OPEN, 8), (UNUSED, 8)],

    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],
    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],
    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],
    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],
    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],
    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],
    [(UNUSED, 2), (OPEN, 7), (UNUSED, 8)],

    [(UNUSED, 3), (OPEN, 6), (UNUSED, 8)],
    [(UNUSED, 3), (OPEN, 6), (UNUSED, 8)],

    [(UNUSED, 3), (START, 6), (UNUSED, 8)]
]
