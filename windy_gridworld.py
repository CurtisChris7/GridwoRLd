from absgridworld import AbsGridworld


class WindyGridworld(AbsGridworld):
    """Class representing a windy girdworld"""

    def __init__(self, schema: list, actions: list, stepPenalty: float, columnToWindMap: dict) -> None:
        """
        Description
        ----------
        Constructor used for processing the schema into the internal gridworld
        representation that all concrete gridworld implementations would use.

        Parameters
        ----------
        schema : list
            The schema used

        actions : list
            A list of all possible actions that can be taken

        stepPenalty : float
            The penalty for taking an action

        columnToWindMap : dict
            Maps the column to the wind value to be experienced
        """
        super().__init__(schema, actions)
        self.stepPenalty = stepPenalty
        self.columnToWindMap = columnToWindMap

    """OVERLOADED METHODS"""

    def getStates(self) -> list:
        return [(row, col) for row in range(self.rowCount) for col in range(self.colCount)]

    def getAvailableActions(self, state) -> list:
        row = state[0]
        col = state[1]

        actions = []
        for a in self.getActions():
            new_row = row + a[0]
            new_col = col + a[1]
            if new_row < 0 or new_row >= self.rowCount or new_col < 0 or new_col >= self.colCount:
                pass
            else:
                actions.append(a)
        return actions

    def step(self, state, action):
        row = state[0]
        col = state[1]
        new_row = max(row + action[0] - self.columnToWindMap[col], 0)
        new_col = col + action[1]

        return (new_row, new_col)

    def getRewardFromAction(self, state, action) -> float:
        return self.stepPenalty
