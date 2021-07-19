from ienivornment import IEnvironment
from gridworld_constants import UNUSED, START, GOAL
import random


class AbsGridworld(IEnvironment):
    """Abstract class used for gridworld problems."""

    def __init__(self, schema: list, actions: list) -> None:
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
        """
        super().__init__()

        # We construct a gridworld from the schema
        gridworld = []
        for row in schema:
            gridRow = []
            for item in row:
                tileType = item[0]
                count = item[1]

                for i in range(count):
                    gridRow.append(tileType)

            gridworld.append(gridRow)

        # We define our gridworld representation in this assignment
        self.gridworld = gridworld
        self.rowCount = len(gridworld)
        self.colCount = len(gridworld[0])

        self.actions = actions

    def generateGreedyAction(self, state, π: dict, e: float):
        actions = self.getAvailableActions(state)
        action = None
        best_action = π[state]

        if random.uniform(0, 1) > e:
            if best_action in actions:
                action = best_action
                prob = 1 - e + (e / len(actions))
            else:
                action = random.choice(actions)
                prob = (e / len(actions))
        else:
            action = random.choice(actions)
            prob = 1 / len(actions)
        return action, prob

    def generateGreedyActionFromQValues(self, state, q: dict, e: float):
        actions = self.getAvailableActions(state)

        max_val = float('-inf')
        action = actions[0]
        for a in actions:
            val = q[(state, a)]
            if val > max_val:
                max_val = val
                action = a

        if random.uniform(0.0, 1.0) < e:
            action = random.choice(actions)

        return action

    def goalTest(self, state) -> bool:
        return state in self.getGoalStates()

    def getStartState(self):
        states = []
        for row in range(len(self.gridworld)):
            for col in range(len(self.gridworld[row])):
                if self.gridworld[row][col] == START:
                    states.append((row, col))
        return random.choice(states)

    def getGoalStates(self) -> list:
        states = []
        for row in range(len(self.gridworld)):
            for col in range(len(self.gridworld[row])):
                if self.gridworld[row][col] == GOAL:
                    states.append((row, col))
        return states

    def displayEnvironment(self):
        for row in self.gridworld:
            row_str = ""
            for item in row:
                if item == UNUSED:
                    row_str += ' '
                else:
                    row_str += item
            print(row_str)
