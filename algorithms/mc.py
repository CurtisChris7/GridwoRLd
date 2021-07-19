import random
from ienivornment import IEnvironment
import util


def off_policy(env: IEnvironment, episode_count: int, discount: float, e: float, debug_level: int = 0) -> dict:
    """
    Description
    ----------
    Performs a simplified off-policy monte carlo control method and generates a policy to be used. 
    The methods for getting all the states in this example as well as generating episodes
    all live in the associated utility file for simplicity but can be delegated to whatever
    suits a consumer of this method better in the future.

    The algorithm is additionally simplified by the following assumptions:
        - Reward is constant and fixed for failures
        - Cost is constant (zero)
        - The entire state and actions space can be stored

    These first two can also be modified easily enough. The latter can be handled, but with 
    more difficulty. There are various strategies on how to do this, and I would reccomend consulting
    a few different sources on making this change inorder to find the best one for the implementer's
    particular needs if they were in need of doing so.

    Parameters
    ----------
    env : IEnvironment
        Representation of the environment, doesn't actually need to be of any particular type, but 
        in this example the girdworld we use is of this type.

    episode_count : int
        The amount of episodes to be run when used in training

    discount: float
        Discount factor

    e : float
        Sigma value used in e-greedy exploration 
        (likelyhood of taking exploratory action in episode generation)

    debug_level : int, optional
        Determines the level of granularity that should be used when debugging during training with 0
        being no messages to three representing every action taken.

    Returns
    -------
    dict
        a dictionary of state-action pairs to values
    """
    states = env.getStates()  # Total state space
    actions = env.getActions()  # All possible actions
    q = {}  # Stores values for all state action pairs
    c = {}  # Stores the cost of all actions
    π = {}  # Stores the best action for all states

    # Initialization step
    for s in states:
        for a in actions:
            k = (s, a)  # state-action pair
            # We set a random value to initialize the map
            q[k] = random.uniform(0, 1) * 400 - 500
            c[k] = 0  # We set the cost

        # The best action is chosen and mapped
        π[s] = util.argmax(q, [(s, a) for a in actions])[1]

    # We perform the desired amount of episodes for training
    for i in range(episode_count):
        if debug_level >= 1:
            print("--------------------------------------------")
            print("Generating Episode", i)

        # Generate an episode
        episode, policy_probs = env.generateEpisode(π, e)

        G = 0
        W = 1

        if debug_level >= 1:
            print("Episode", i, "Length", len(episode))

        cntr = 0  # Used for keeping track of how long until the episode terminates

        # We process the episode in reverse
        for i in range(len(episode)-1, -1, -1):
            cntr += 1

            t = episode[i]  # We grab the state-action pair at that moment
            s = t[0]  # State
            a = t[1]  # Action

            # We perform the necesary updates to the weights
            G = (discount * G) + env.getRewardFromAction(s, a)
            c[(s, a)] += W
            q[(s, a)] += ((W / c[(s, a)]) * (G - q[(s, a)]))

            # We find and store the best available action as determined by q
            actions = env.getAvailableActions(s)
            best_action = util.argmax(q, [(s, action)
                                          for action in actions])[1]
            π[s] = best_action

            if debug_level >= 2:
                print("t:", t, "c[(s, a)]:", c[(s, a)], "q[(s, a)]:",
                      q[(s, a)], "π[s]", π[s])
                print([((s, action), q[(s, action)]) for action in actions])

            # If the best action was not taken we break early
            if a != π[s]:
                if debug_level >= 1:
                    print("BREAK", cntr)
                    print("--------------------------------------------")
                break

            # Updates weight
            W /= policy_probs[(a, s)]
            if debug_level >= 2:
                print("W", W)
                print("--------------------------------------------")

    return π
