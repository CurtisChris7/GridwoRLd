from demo_constants.demo_blackjack_data import *
from ienivornment import IEnvironment


class Blackjack(IEnvironment):
    """Class representing a simplified game of Blackjack"""

    def __init__(self, actions) -> None:
        """

        """
        super().__init__()
        self.sum = 0
        self.playerScore = 0
        self.enemyScore = 0
        self.actions = actions
        self._initDeck()

    """OVERLOADED METHODS"""

    def getStates(self) -> list:
        return

    def getAvailableActions(self, state) -> list:
        if sum < 21:
            return ACTIONS
        return [FOLD]

    def getActions(self) -> list:
        return ACTIONS

    def step(self, state, action):
        return

    def generateGreedyAction(self, state, π: dict, e: float):
        return

    def generateGreedyActionFromQValues(self, state, q: dict, e: float):
        return

    def getRewardFromAction(self, state, action) -> float:
        return

    def generateEpisode(self, π: dict, e: float) -> tuple:
        return

    def generateEpisodeFromQValues(self, q: dict, e: float) -> list:
        return

    def goalTest(self, state) -> bool:
        return

    def getStartState(self):
        return

    def getGoalStates(self) -> list:
        return

    def displayEnvironment(self):
        return

    """PRIVATE HELPER METHODS"""

    def _initDeck() -> None:
        """
        """
        return

    def _draw() -> None:
        """
        """
        return
