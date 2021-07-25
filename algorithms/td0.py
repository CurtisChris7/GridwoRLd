def td0(gridworld, policy, discount=1.0, episode_count=500000, alpha=0.05, epsilon=0.1):
    v = {}
    states = get_states(ROWS + 1, COLS + 1)
    goals = get_goal_states(gridworld)
    for s in states:
        v[s] = random.uniform(0.0, 1.0)

    for ep in range(episode_count):
        print("----------------------------------------------")
        print("EPISODE:", ep)
        state = get_starting_state(gridworld)
        while not state in goals:
            action = generate_greedy_action(state, policy, epsilon=0.1)
            new_state = step(state, action)
            v[state] += alpha * (REWARD + (discount * v[new_state]) - v[state])
            state = new_state
        print("----------------------------------------------")
    return v
