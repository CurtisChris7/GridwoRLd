import argparse
from simulation_constants import EPISODE_COUNT, E
import algorithms.mc as mc

#import racetrack
#import demo_constants.demo_racetrack_data as data

from windy_gridworld import WindyGridworld
import demo_constants.demo_windy_gridworld_data as data

# Script arguments
run_demo_test = False
train = False
display_policy = False
display_track = True
output_filename = "output.py"
episode_count = 5 * EPISODE_COUNT
debug_level = 1

"""
env = racetrack.Racetrack(data.DEMO_RACETRACK_SCHEMA,
                          data.MAX_VELOCITY, data.ACTIONS, data.REWARD, data.FAIL_REWARD)
"""
env = WindyGridworld(data.GRIDWORLD_SCHEMA, data.ACTIONS,
                     data.REWARD, data.COL_TO_WIND)


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


def run_demo():
    """
    Description
    ----------
    Runs a demo of the policy stored in demo_policy.py
    """
    #from demo_policies.racetrack.demo_racetrack_policy import POLICY
    from output import POLICY

    episode = env.generateEpisode(POLICY, 0)[0]
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
    # Training takes place here
    result = mc.off_policy(
        env, episode_count, data.DISCOUNT, E, debug_level)

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
