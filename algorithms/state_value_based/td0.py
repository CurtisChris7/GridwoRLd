from ienivornment import IEnvironment
import random


def td0(env: IEnvironment, policy, discount=1.0, episode_count=500000, alpha=0.05, epsilon=0.1):
    """

    """
    v = {}
    states = env.getStates()
    goals = env.getGoalStates()
    for s in states:
        v[s] = random.uniform(0.0, 1.0)

    for ep in range(episode_count):
        print("----------------------------------------------")
        print("EPISODE:", ep)
        state = env.getStartState()
        while not state in goals:
            action = env.generateGreedyAction(state, policy, epsilon)
            new_state = env.step(state, action)
            v[state] += alpha * (env.getRewardFromAction(state,
                                                         action) + (discount * v[new_state]) - v[state])
            state = new_state
        print("----------------------------------------------")
    return v
