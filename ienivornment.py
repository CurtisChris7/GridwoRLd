from abc import ABC, abstractmethod


class IEnvironment(ABC):
    """Interface for potential enviornments to be consumed by the reinforcement algorithms."""

    @abstractmethod
    def getStates(self) -> list:
        """
        Description
        ----------
        Returns the entire state space of the evironment

        Returns
        -------
        list
            A list containing all possible states
        """
        pass

    @abstractmethod
    def getAvailableActions(self, state) -> list:
        """
        Description
        ----------
        Gets all available actions from a given state

        Parameters
        ----------
        state : any
            The given state we want to get all actions from

        Returns
        -------
        list
            A list of legal actions for a given state
        """
        pass

    @abstractmethod
    def getActions(self) -> list:
        """
        Description
        ----------
        Gets all available actions

        Returns
        -------
        list
            A list of all legal actions
        """
        pass

    @abstractmethod
    def step(self, state, action):
        """
        Description
        ----------
        Gets the resulting state after applying a given action to a given state

        Parameters
        ----------
        state : any
            The given state we want to advance from

        action : any
            The given action we want to apply

        Returns
        -------
        any
            The resulting state
        """
        pass

    @abstractmethod
    def generateGreedyAction(self, state, π: dict, e: float):
        """
        Description
        ----------
        Gets an action from a given state in an e-greedy manner

        Parameters
        ----------
        state : any
            The given state we want to advance from

        π : dict
            The policy to be treated as optimal

        e : float
            Likelyhood of taking a random action

        Returns
        -------
        any
            The 'optimal' action or a random one
        """
        pass

    @abstractmethod
    def generateGreedyActionFromQValues(self, state, q: dict, e: float):
        """
        Description
        ----------
        Gets an action from a given state in an e-greedy manner

        Parameters
        ----------
        state : any
            The given state we want to advance from

        q : dict
            The dictionary mapping state action pairs to values

        e : float
            Likelyhood of taking a random action

        Returns
        -------
        any
            The 'optimal' action or a random one
        """
        pass

    @abstractmethod
    def getRewardFromAction(self, state, action) -> float:
        """
        Description
        ----------
        Gets the reward from applying a particular action at a given state

        Parameters
        ----------
        state : any
            The given state we want to advance from

        action : any
            The given action we want to apply

        Returns
        -------
        float
            The reward for taking a particular action in a given state
        """
        pass

    @abstractmethod
    def generateEpisode(self, π: dict, e: float) -> list:
        """
        Description
        ----------
        Gets the reward from applying a particular action at a given state

        Parameters
        ----------
        π : dict
            The policy to be treated as optimal

        e: float
            The likelyhood of taking a random action

        Returns
        -------
        list
            The reward for taking a particular action in a given state
        """
        pass

    @abstractmethod
    def goalTest(self, state) -> bool:
        """
        Description
        ----------
        Determines wether or not the provided state is a goal state

        Parameters
        ----------
        state : any
            The given state we want to check

        Returns
        -------
        bool
            The reward for taking a particular action in a given state
        """
        pass

    @abstractmethod
    def getStartState(self):
        """
        Description
        ----------
        Returns a start state

        Returns
        -------
        any
            A starting state
        """
        pass

    @abstractmethod
    def getGoalStates(self) -> list:
        """
        Description
        ----------
        Gets all the goal states

        Returns
        -------
        list
            A list containing all the goal states
        """
        pass

    @abstractmethod
    def displayEnvironment(self):
        """
        Description
        ----------
        Displays the environment
        """
        pass
