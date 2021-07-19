from gridworld_constants import *

ACTIONS = [(-1, -1), (-1, 0), (0, -1), (-1, 1),
           (0, 0), (1, -1), (0, 1), (1, 0), (1, 1)]

GRIDWORLD_SCHEMA = [
    [(UNUSED, 10)],
    [(UNUSED, 10)],
    [(UNUSED, 10)],
    [(START, 1), (UNUSED, 6), (GOAL, 1), (UNUSED, 2)],
    [(UNUSED, 10)],
    [(UNUSED, 10)],
    [(UNUSED, 10)],
]

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
