"""
Author: Markus Frohmann
Matr.Nr.: K12005604
Exercise 10
"""

import re
import os
import numpy as np


def read_config_file(configpath: str):
    """
    Extracts number of iterations, symbol for dead cells, symbol for live cells, and initial state seed from inputfile.

    :param configpath: path of config file that should be parsed.
    :return: n. of iterations: int
    :return: symbol for live cells: str
    :return: symbol for dead cells: str
    :return: initial state seed: np.array
    """

    # initialize variables
    dead = 0
    live = 0
    n_iterations = 0
    # open and store file
    with open(configpath, 'r') as f:
        text = f.read()

    # loop over all lines in configfile
    for line in text.split('\n'):
        # try to get number of iterations
        if line.startswith('n_iterations:'):
            pattern_niter = "n_iterations: *(.*)"
            niter_match = re.search(pattern_niter, line)
            n_iterations = niter_match.group(1)

        # try to get dead symbol
        if line.startswith('dead_symbol:'):
            try:
                dead_symbol = 'dead_symbol: *(.*)"(.)"'
                dead_match = re.search(dead_symbol, line)
                dead = dead_match.group(2)
            except:
                raise AttributeError('Dead symbol does not match specification!')

        # try to get live symbol
        if line.startswith('live_symbol:'):
            try:
                live_symbol = 'live_symbol: *(.*)"(.)"'
                live_match = re.search(live_symbol, line)
                live = live_match.group(2)
            except:
                raise AttributeError('Live symbol does not match specification!')
    # raise error if n_iterations is missing or not an int
    if not n_iterations:
        raise AttributeError('Number of iterations missing!')
    try:
        n_iterations = int(n_iterations)
    except ValueError:
        raise AttributeError('Cannot convert number of iterations to integer!')

    # Raise Error if dead/live symbol is not there or contains more than one character
    if len(str(dead)) > 1 or not dead:
        raise AttributeError('Wrong or no dead symbol!')
    if len(str(live)) > 1 or not live:
        raise AttributeError('Wrong or no live symbol!')

    # get initial state seed
    try:
        seed_pattern = 'init_state:( *)\\n\"\\n((.|\n)*)\\n\"'
        seed_match = re.search(seed_pattern, text)
        seed = seed_match.group(2)
    except:
        raise AttributeError('Initial state not given!')

    # define helper function for splitting strings into lists
    def split(word):
        return [char for char in word]

    # transform initial state seed into numpy array consisting of 1's and 0's
    seed_list = [char for char in (line for line in seed.splitlines()) if char]
    new_list = [split(line) for line in seed_list]
    array = np.asarray(new_list)
    # replace dead and live symbols with 0's and then 1's
    dead_array = np.where(array == dead, 0, array)
    out_array = np.where(dead_array == live, 1, dead_array)

    # Check if all lines of seed string have same length
    iteration_seed = iter(out_array)
    length_seed = len(next(iteration_seed))
    if not all(len(row) == length_seed for row in iteration_seed):
        raise ValueError('Not all lists have same length!')

    # Check if seed contains no symbols other than dead or live
    for row in out_array:
        for elem in row:
            if elem != '1' and elem != '0':
                raise ValueError('Seed contains symbols other than dead or live!')

    return n_iterations, dead, live, out_array.astype(int)


# for testing purposes only
if __name__ == '__main__':
    configpath = os.path.join(r'valid_00.config')
    n_iterations, dead, live, array = read_config_file(configpath)
    print(n_iterations, dead, live, array)
