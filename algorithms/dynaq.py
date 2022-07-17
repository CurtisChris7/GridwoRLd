from ienivornment import IEnvironment
import random
import util


def dynaQ(env: IEnvironment, alpha: float, episodeCount: int, n: int, epsilon: float, discount: float, debug: int = 0) -> dict:
    """

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
        goals = env.getGoalStates()

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

            for i in range(n):
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
