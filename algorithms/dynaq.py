from ienivornment import IEnvironment
import random
import util


def dynaQ(env: IEnvironment, alpha: float, episodeCount: int, n: int, epsilon: float, discount: float, debug: int = 0) -> dict:
    """
    Description
    ----------
    Implementation of dynaQ

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

    epsilon : float
        Sigma value used in e-greedy exploration 
        (likelyhood of taking exploratory action in episode generation)

    n : int
        The number of times to resample from history every action

    debug_level : int, optional
        Determines the level of granularity that should be used when debugging during training with 0
        being no messages one representing just some metadata on a per episode basis and two being
        the updates occuring within the steps of each episode

    Returns
    -------
    dict
        a dictionary of state-action pairs to values
    """
    stateHistory = {}
    q = {}
    model = {}

    for s in env.getStates():
        for a in env.getActions():
            q[(s, a)] = random.uniform(0.0, 1.0)
            model[(s, a)] = (0, None)

    for ep in range(episodeCount):
        if debug >= 1:
            print("------------------------------------------------------------------")
            print("EPISODE:", ep)

        cntr = 0
        state = env.getStartState()

        while not env.goalTest(state):
            cntr += 1
            action = env.generateGreedyActionFromQValues(state, q, epsilon)

            if debug >= 3:
                print(state, action)

            if state in stateHistory:
                actionHistory = stateHistory[state]
                actionHistory.append(action)
                actionHistory = list(set(actionHistory))
                stateHistory[state] = actionHistory
            else:
                stateHistory[state] = [action]

            if debug >= 3:
                print("HISTORY:", stateHistory[state])

            newState = env.step(state, action)
            r = env.getRewardFromAction(state, action)

            q[(state, action)] += alpha * (r + discount *
                                           q[util.argmax(q, [(newState, a) for a in env.getActions(newState)])] - q[(state, action)])
            model[(state, action)] = (r, newState)

            state = newState

            for _ in range(n):
                states = list(stateHistory.keys())
                if debug >= 3:
                    print("OBSERVED:", states)
                s = random.choice(states)
                a = random.choice(stateHistory[s])
                if debug >= 2:
                    print("UPDATING:", s, a)
                    print("OLD:", q[(s, a)])
                (r, newState) = model[(s, a)]
                q[(s, a)] += alpha * (r + discount *
                                      q[util.argmax(q, [(newState, a) for a in env.getActions(newState)])] - q[(s, a)])
                if debug >= 2:
                    print("NEW:", q[(s, a)])

        if debug >= 1:
            print("EPISODE LENGTH:", cntr)
            print("------------------------------------------------------------------")

    return q
