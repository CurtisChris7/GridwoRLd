from absgridworld import AbsGridworld

"""TODO"""

class ComplexGirdworld(AbsGridworld):
    """Gridworld with racetrack-like movement, in a maze with wind"""

    def __init__(self, schema: list, actions: list, maxVelocity: int, stepPenalty: float, failPenalty: float, columnToWindMap: dict, endReward: float) -> None:
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

        columnToWindMap : dict
            Maps the column to the wind value to be experienced
        """
        super().__init__(schema, actions)
        self.maxVelocity = maxVelocity
        self.stepPenalty = stepPenalty
        self.failPenalty = failPenalty
        self.columnToWindMap = columnToWindMap
        self.endReward = endReward
