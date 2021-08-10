from absgridworld import AbsGridworld
from gridworld_constants import WALL


class MazeGridWorld(AbsGridworld):
    """Class representing a mazelike gridworld"""

    def __init__(self, schema: list, actions: list, endReward: float) -> None:
        """

        """
        super().__init__(schema, actions)
        self.endReward = endReward
        self._goals = super().getGoalStates()  # Cached due to repeated checking

    """OVERLOADED METHODS"""

    def getStates(self) -> list:
        return [(row, col) for row in range(self.rowCount) for col in range(self.colCount)]

    def step(self, state, action):
        row = state[0]
        col = state[1]
        newRow = row + action[0]
        newCol = col + action[1]

        if newRow < 0 or newRow >= self.rowCount or newCol < 0 or newCol >= self.colCount or self.gridworld[newRow][newCol] == WALL:
            return (row, col)

        return (newRow, newCol)

    def getAvailableActions(self, state) -> list:
        return self.getActions()

    def getRewardFromAction(self, state, action) -> float:
        return self.endReward if self.step(state, action) in self._goals else 0

    def getGoalStates(self) -> list:
        return self._goals()
