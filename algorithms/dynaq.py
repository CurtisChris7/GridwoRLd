def dyna_q(gridworld, alpha=0.1, episode_count=25, debug=0, n=50, epsilon=0.1, discount=0.95):
    state_history = {}
    q = {}
    model = {}

    for s in get_states(ROWS+1, COLS+1):
        for a in ACTIONS:
            q[(s, a)] = random.uniform(0.0, 1.0)  # * 400 - 500
            model[(s, a)] = (0, None)

    for ep in range(episode_count):
        if debug >= 1:
            print("------------------------------------------------------------------")
            print("EPISODE:", ep)

        cntr = 0
        state = get_starting_state(gridworld)
        goals = get_goal_states(gridworld)

        while not state in goals:
            cntr += 1
            action = generate_greedy_action(
                state, q, gridworld, epsilon=epsilon)

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

            new_state = step(state, action, gridworld)
            r = 1 if new_state in goals else REWARD

            q[(state, action)] += alpha * (r + discount *
                                           q[argmax(q, [(new_state, a) for a in ACTIONS])] - q[(state, action)])
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
                                      q[argmax(q, [(new_state, a) for a in ACTIONS])] - q[(s, a)])
                if debug >= 2:
                    print("NEW:", q[(s, a)])

        if debug >= 1:
            print("EPISODE LENGTH:", cntr)
            print("------------------------------------------------------------------")

    return q
