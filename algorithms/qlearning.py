from ienivornment import IEnvironment
import random
import util


def qLearning(env: IEnvironment, discount: float, alpha: float, e: float, episode_count: int, debug: int):
    """
    Description
    ----------
    Implementation of qLearning

    Parameters
    ----------
    env : IEnvironment
        Representation of the environment, doesn't actually need to be of any particular type, but
        in this example the girdworld we use is of this type.

    episode_count : int
        The amount of episodes to be run when used in training

    discount : float
        Discount factor

    alpha : float
        Step factor

    e : float
        Sigma value used in e-greedy exploration
        (likelyhood of taking exploratory action in episode generation)

    debug_level : int, optional
        Determines the level of granularity that should be used when debugging during training with 0
        being no messages one representing just some metadata on a per episode basis and two being
        the updates occuring within the steps of each episode

    Returns
    -------
    dict
        a dictionary of state-action pairs to values
    """
    Q = {}  # Maps state action pairs to values
    for s in env.getStates():
        for a in env.getActions():
            # All are initialized randomly
            Q[(s, a)] = random.uniform(0.0, 1.0)

    i = 0
    while (i < episode_count):
        if debug >= 1:
            print("------------------------------------------------")
            print("EPISODE:", i)

        state = env.getStartState()
        new_state = state

        if debug >= 2:
            print(state, new_state)

        pairs = []

        while not env.goalTest(state):
            action = env.generateGreedyActionFromQValues(state, Q, e)

            if debug >= 2:
                print(state, action)

            pairs.append((state, action))
            newState = env.step(state, action)

            if env.goalTest(newState):
                break

            Q[(state, action)] += alpha * (env.getRewardFromAction(state, action) + (discount *
                                                                                     Q[util.argmax(Q, [(newState, a) for a in env.getAvailableActions(newState)])] - Q[(state, action)]))
            state = newState

        if debug >= 1:
            print("Action Count: ", len(pairs))
            print("------------------------------------------------")

        i += 1

    return Q
