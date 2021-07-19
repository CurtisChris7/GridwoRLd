from absgridworld import AbsGridworld
import gridworld_constants
import random


class Racetrack(AbsGridworld):
    """Class representing a gridworld style racetrack"""

    def __init__(self, schema: list, maxVelocity: int, actions: list, stepPenalty: float, failPentality: float) -> None:
        """
        Description
        ----------
        Constructor used for processing the schema into the internal gridworld
        representation that all concrete gridworld implementations would use.

        Parameters
        ----------
        schema : list
            The schema used
        """
        super().__init__(schema)
        self.maxVelocity = maxVelocity
        self.actions = actions
        self.stepPenalty = stepPenalty
        self.failPenalty = failPentality

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

    def getActions(self) -> list:
        return self.actions

    def step(self, state, action):
        new_state = self._getNewstate(state, action)

        if not self._isTrajectoryInbounds(new_state, self.gridworld):
            random_pos = self.getStartState()
            return (random_pos[0], random_pos[1], 0, 0)

        if self._hasCrossed(state, action):
            return None

        return new_state

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

    def getRewardFromAction(self, state, action) -> float:
        new_state = self._getNewstate(state, action)

        if not self._isTrajectoryInbounds(new_state, self.gridworld):
            return self.failPenalty

        if self._hasCrossed(state, action):
            return 0

        return self.stepPenalty

    def generateEpisode(self, π: dict, e: float) -> list:
        state_action_pairs = []
        starting_pos = self.getStartState()
        policy_probs = {}

        state = (starting_pos[0], starting_pos[1], 0, 0)

        while (state != None):
            action, prob = self.generateGreedyAction(state, π, e)
            policy_probs[(action, state)] = prob
            state_action_pairs.append((state, action))
            new_state = self.step(state, action)

            # print((state, action), policy_probs[(
            #    action, state)], " -> ", new_state)

            state = new_state

        return state_action_pairs, policy_probs

    def goalTest(self, state) -> bool:
        return state in self.getGoalStates()

    def getStartState(self):
        states = []
        for row in range(len(self.gridworld)):
            for col in range(len(self.gridworld[row])):
                if self.gridworld[row][col] == gridworld_constants.START:
                    states.append((row, col))
        return random.choice(states)

    def getGoalStates(self) -> list:
        states = []
        for row in range(len(self.gridworld)):
            for col in range(len(self.gridworld[row])):
                if self.gridworld[row][col] == gridworld_constants.GOAL:
                    states.append((row, col))
        return states

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

    def _hasCrossed(self, state, action):
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

        intersections = [cell for cell in finish_line if cell in covered_cells]

        return len(intersections) > 0

    def _isTrajectoryInbounds(self, state, racetrack):
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
