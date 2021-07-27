from ienivornment import IEnvironment
import random
import util


def dynaQ(env: IEnvironment, alpha: float, episode_count: int, n: int, epsilon: float, discount: float, debug: int):
    """

    """
    state_history = {}
    q = {}
    model = {}

    for s in env.getStates():
        for a in env.getActions():
            q[(s, a)] = random.uniform(0.0, 1.0)  # * 400 - 500
            model[(s, a)] = (0, None)

    for ep in range(episode_count):
        if debug >= 1:
            print("------------------------------------------------------------------")
            print("EPISODE:", ep)

        cntr = 0
        state = get_starting_state(env)
        goals = get_goal_states(env)

        while not state in goals:
            cntr += 1
            action = generate_greedy_action(
                state, q, env, epsilon=epsilon)

            if debug >= 3:
                print(state, action)

            if state in state_history:
                action_history = state_history[state]
                action_history.append(action)
                action_history = list(set(action_history))
                state_history[state] = action_history
            else:
                state_history[state] = [action]

            if debug >= 3:
                print("HISTORY:", state_history[state])

            new_state = env.step(state, action)
            r = 1 if new_state in goals else env.getRewardFromAction(
                state, action)

            q[(state, action)] += alpha * (r + discount *
                                           q[util.argmax(q, [(new_state, a) for a in env.getActions(new_state)])] - q[(state, action)])
            model[(state, action)] = (r, new_state)

            state = new_state

            for i in range(n):
                states = list(state_history.keys())
                # if debug >= 2:
                #    print("OBSERVED:", states)
                s = random.choice(states)
                a = random.choice(state_history[s])
                if debug >= 2:
                    print("UPDATING:", s, a)
                    print("OLD:", q[(s, a)])
                (r, new_state) = model[(s, a)]
                q[(s, a)] += alpha * (r + discount *
                                      q[util.argmax(q, [(new_state, a) for a in env.getActions(new_state)])] - q[(s, a)])
                if debug >= 2:
                    print("NEW:", q[(s, a)])

        if debug >= 1:
            print("EPISODE LENGTH:", cntr)
            print("------------------------------------------------------------------")

    return q
