from ienivornment import IEnvironment
import random


def sarsa(env: IEnvironment, discount: float, alpha: float, e: float, episode_count: int, debug: int):
    """
    Description
    ----------
    Implementation of sarsa

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
        goals = env.getGoalStates()

        pairs = []

        while not state in goals and not new_state in goals:
            action = env.generateGreedyActionFromQValues(state, Q, e)

            if debug >= 2:
                print(state, action)

            pairs.append((state, action))
            new_state = env.step(state, action)

            if new_state in goals:
                break

            new_action = env.generateGreedyActionFromQValues(new_state, Q, e)

            Q[(state, action)] += alpha * (env.getRewardFromAction(state, action) + (discount *
                                                                                     Q[(new_state, new_action)]) - Q[(state, action)])
            state = new_state
            action = new_action
            pairs.append((state, action))

            if debug >= 2:
                print(new_state, new_action)

        if debug >= 1:
            print("Action Count: ", len(pairs))
            print("------------------------------------------------")

        i += 1

    return Q
