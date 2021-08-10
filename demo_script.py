"""

"""
import argparse
from simulation_constants import *

from algorithms.sarsa import sarsa
from algorithms.mc import off_policy
from algorithms.qlearning import qLearning
from algorithms.dynaq import dynaQ

"""
from racetrack import Racetrack
import demo_constants.demo_racetrack_data as data

from windy_gridworld import WindyGridworld
import demo_constants.demo_windy_gridworld_data as data

from maze_gridworld import MazeGridWorld
import demo_constants.demo_maze_data as data

from complex_gridworld import ComplexGirdworld
import demo_constants.demo_complex_gridworld_data as data

from blackjack import Blackjack
import demo_constants.demo_blackjack_data as data
"""

# Script arguments
run_demo_test = False
train = False
display_policy = False
display_track = True
output_filename = "output.py"
episode_count = EPISODE_COUNT
debug_level = 1
algorithm_option = 0
enviornment_option = 0

data = None
env = None

# Environment Enumeration Constants
RACETRACK_OPTION = 1
WINDYGRIDWORLD_OPTION = 2
WALLEDGRIDWORLD_OPTION = 3
COMPEX_GRIDWORLD_OPTION = 4
BLACKJACK_OPTION = 5

# Algorithm Enumeration Constants
MC_OPTION = 1
SARSA_OPTION = 2
QLEARNING_OPTION = 3
DYNAQ_OPTION = 4

"""
env = WindyGridworld(data.GRIDWORLD_SCHEMA, data.ACTIONS,
                     data.REWARD, data.COL_TO_WIND)
env = racetrack.Racetrack(data.DEMO_RACETRACK_SCHEMA,
                          data.MAX_VELOCITY, data.ACTIONS, data.REWARD, data.FAIL_REWARD)
"""


def parse_args():
    """
    Description
    ----------
    Handles the argument parsing of the script
    """
    parser = argparse.ArgumentParser(
        description='A script used to run an off-policy monte carlo control method for a specific gridworld problem. It can test and create policies.')
    parser.add_argument(
        '-d', '--display_policy', help='Determines whether or not to display the policy after training', required=False, action='store_true')
    parser.add_argument(
        '-t', '--train', help='Determines whether or not to run a training session', required=False, action='store_true')
    parser.add_argument(
        '-o', '--output', help='The output file use for storing the generated policy', required=False)
    parser.add_argument(
        '-r', '--run_demo', help='Toggles on running the policy stored in demo_policy.py', required=False, action='store_true')
    parser.add_argument(
        '-n', '--no_track_display', help='Toggles off a display of the track', required=False, action='store_false')
    parser.add_argument(
        '-e', '--episode_count', help='The amount of episodes to train on', required=False)
    parser.add_argument(
        '-i', '--info_level', help='Determines the level of information to be shown when running (0-3)', required=False)
    parser.add_argument('-a', '--algorithm',
                        help='Determines which algorithim to use')
    parser.add_argument('-v', '--enviornment',
                        help='Determines which which environment to use')

    args = parser.parse_args()

    if args.display_policy:
        global display_policy
        display_policy = True

    if args.train:
        global train
        train = True

    if args.no_track_display:
        global display_track
        display_track = args.no_track_display

    if args.run_demo:
        global run_demo_test
        run_demo_test = True

    if args.output:
        global output_filename
        output_filename = args.output

    if args.episode_count:
        global episode_count
        episode_count = args.episode_count

    if args.info_level:
        global debug_level
        debug_level = args.info_level

    if args.algorithm:
        global algorithm_option
        algorithm_option = args.algorithm

    if args.enviornment:
        global enviornment_option
        enviornment_option = args.enviornment


def run_demo():
    """
    Description
    ----------
    Runs a demo of the policy stored in demo_policy.py
    """
    #from demo_policies.demo_racetrack_policy import POLICY
    #from demo_policies.windy_gridworld.demo_windy_gridworld_qvalue_policy import POLICY
    #from output import POLICY

    episode = None

    # We find the corresponding policy we need
    if enviornment_option == RACETRACK_OPTION:
        if algorithm_option == MC_OPTION:
            from demo_policies.racetrack.mc_policy import POLICY
        elif algorithm_option == SARSA_OPTION:
            from demo_policies.racetrack.sarsa_policy import POLICY

    elif enviornment_option == WINDYGRIDWORLD_OPTION:
        if algorithm_option == MC_OPTION:
            from demo_policies.windy_gridworld.mc_policy import POLICY
        elif algorithm_option == SARSA_OPTION:
            from demo_policies.windy_gridworld.sarsa_policy import POLICY

    # elif enviornment_option == WALLEDGRIDWORLD_OPTION:

    episode = env.generateEpisodeFromQValues(POLICY, 0)
    for pair in episode:
        print(pair)
    print("EPISODE LENGTH:", len(episode))
    return


def train_policy():
    """
    Description
    ----------
    Handles the actual learning for the policy
    """
    result = None

    # Training takes place here
    if algorithm_option == MC_OPTION:
        result = off_policy(env, episode_count, DISCOUNT, E, debug_level)
    elif algorithm_option == SARSA_OPTION:
        result = sarsa(env, DISCOUNT, ALPHA, E, episode_count, debug_level)
    elif algorithm_option == QLEARNING_OPTION:
        result = qLearning(env, )
    """

    elif algorithm_option == DYNAQ_OPTION:
    """

    if display_policy:
        print(result)

    if output_filename:
        with open(output_filename, 'w') as f:
            f.write("POLICY = " + str(result) + "\n")
            f.close()


def main():
    """
    Description
    ----------
    Main control flow of the script
    """
    parse_args()

    if display_track:
        env.displayEnvironment()

    if train:
        train_policy()

    if run_demo_test:
        run_demo()


if __name__ == "__main__":
    main()
