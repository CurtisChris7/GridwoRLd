from ienivornment import IEnvironment
import random


def nStepTD(env: IEnvironment, policy, discount: float, episode_count: int, alpha: float = 0.05, n: int = 1, epsilon: float = 0.1, use_td_sum=False):
    """

    """
    v = {}
    states = get_states(ROWS + 1, COLS + 1)
    goals = get_goal_states(env)
    for s in states:
        v[s] = random.uniform(0.0, 1.0)

    for ep in range(episode_count):
        print("----------------------------------------------")
        print("EPISODE:", ep)
        episode = generate_episode(
            env, policy, epsilon=epsilon, include_terminal=True)
        print("EPISODE LENGTH:", len(episode))
        T = float('inf')
        t = 0
        tau = 0

        while(tau != T - 1):
            if t < T:
                if episode[t+1][0] in goals:
                    T = t + 1

            tau = t - n + 1

            if tau >= 0:
                G = 0
                if use_td_sum:
                    i = tau
                    while(i <= min(tau + n, T)):
                        G += (REWARD + (discount * v[episode[tau + 1][0]]) -
                              v[episode[tau][0]]) * pow(discount, i - tau - 1)
                        i += 1

                else:
                    i = tau + 1
                    while(i <= min(tau + n, T)):
                        G += REWARD * pow(discount, i - tau - 1)
                        i += 1

                    if tau + n < T:
                        G += pow(discount, n) * v[episode[tau + n][0]]

                    v[episode[tau][0]] += alpha * (G - v[episode[tau][0]])
            t += 1
        print("----------------------------------------------")

    return v
