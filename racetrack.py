from absgridworld import AbsGridworld
import gridworld_constants


class Racetrack(AbsGridworld):
    """Class representing a gridworld style racetrack"""

    def __init__(self, schema: list, maxVelocity: int, actions: list, stepPenalty: float, failPenalty: float) -> None:
        """
        Description
        ----------
        Constructor used for processing the schema into the internal gridworld
        representation that all concrete gridworld implementations would use.

        Parameters
        ----------
        schema : list
            The schema used

        maxVelocity : int
            The maximum velocity in any direction that an agent can move in any direction

        actions : list
            A list of all possible actions that can be taken

        stepPenalty : float
            The penalty for taking an action

        failPenalty : float
            The penalty for taking a failing action
        """
        super().__init__(schema, actions)
        self.maxVelocity = maxVelocity
        self.stepPenalty = stepPenalty
        self.failPenalty = failPenalty

    """OVERLOADED METHODS"""

    def getStates(self) -> list:
        states = []
        for row in range(len(self.gridworld)):
            for col in range(len(self.gridworld[row])):
                if self.gridworld[row][col] != gridworld_constants.UNUSED:
                    # Create all possible states
                    for i in range(self.maxVelocity + 1):
                        for j in range(self.maxVelocity + 1):
                            states.append((row, col, i, j))

        return states

    def getStartState(self):
        state = super().getStartState()
        return (state[0], state[1], 0, 0)

    def getAvailableActions(self, state) -> list:
        x = state[2]
        y = state[3]
        actions = []
        for a in self.actions:
            new_x = x + a[0]
            new_y = y + a[1]
            if new_x > self.maxVelocity or new_y > self.maxVelocity or new_x < 0 or new_y < 0 or (new_x == 0 and new_y == 0):
                pass
            else:
                actions.append(a)
        return actions

    def step(self, state, action):
        newState = self._getNewstate(state, action)

        if not self._isTrajectoryInbounds(newState, self.gridworld):
            #print("STARTING OVER!")
            randomState = self.getStartState()
            return (randomState[0], randomState[1], 0, 0)

        intersections = self._getIntersections(state, action)
        if len(intersections) > 0:
            return intersections[0]

        return newState

    def getRewardFromAction(self, state, action) -> float:
        newState = self._getNewstate(state, action)

        if not self._isTrajectoryInbounds(newState, self.gridworld):
            return self.failPenalty

        if self._hasCrossed(state, action):
            return 0

        return self.stepPenalty

    """PRIVATE HELPER METHODS BELOW"""

    def _getNewstate(self, state, action):
        """
        Description
        ----------
        Gets the resulting state after applying an action from a given state

        Parameters
        ----------
        state : tuple
            Representation of the state

        action : tuple
            Representation of the action

        Returns
        -------
        tuple
            the resulting state
        """
        return (state[0] - state[2], state[1] + state[3], state[2] + action[0], state[3] + action[1])

    def _hasCrossed(self, state, action) -> bool:
        """
        Description
        ----------
        Determines wether or not applying the action at the specified state would cross the finish-line

        Parameters
        ----------
        racetrack : list of lists
            Representation of the racetrack

        state : tuple
            Representation of the state

        action : tuple
            Representation of the action

        Returns
        -------
        bool
            Wether or not applying the action at the specified state would cross the finish-line
        """
        finishLine = self.getGoalStates()

        newState = self._getNewstate(state, action)
        coveredRows = [i for i in range(newState[0], state[0] + 1)]
        coveredCols = [i for i in range(state[1], newState[1] + 1)]
        coveredCells = [(row, col)
                        for row in coveredRows for col in coveredCols]

        intersections = [cell for cell in finishLine if cell in coveredCells]

        return len(intersections) > 0

    def _getIntersections(self, state, action) -> list:
        """
        Description
        ----------
        Determines wether or not applying the action at the specified state would cross the finish-line

        Parameters
        ----------
        racetrack : list of lists
            Representation of the racetrack

        state : tuple
            Representation of the state

        action : tuple
            Representation of the action

        Returns
        -------
        bool
            Wether or not applying the action at the specified state would cross the finish-line
        """
        finish_line = self.getGoalStates()

        new_state = self._getNewstate(state, action)
        covered_rows = [i for i in range(new_state[0], state[0] + 1)]
        covered_cols = [i for i in range(state[1], new_state[1] + 1)]
        covered_cells = [(row, col)
                         for row in covered_rows for col in covered_cols]

        return [cell for cell in finish_line if cell in covered_cells]

    def _isTrajectoryInbounds(self, state, racetrack) -> bool:
        """
        Description
        ----------
        Determines wether or not the given state is within the given racetrack

        Parameters
        ----------
        racetrack : list of lists
            Representation of the racetrack

        state : tuple
            Representation of the state

        Returns
        -------
        bool
            Wether or not the specified state is within bounds of the racetrack
        """
        row = state[0]
        col = state[1]

        if col >= self.colCount or col < 0 or row >= self.rowCount or row < 0 or racetrack[row][col] == gridworld_constants.UNUSED:
            return False

        return True
