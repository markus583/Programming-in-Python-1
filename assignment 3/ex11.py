"""
Author: Markus Frohmann
Matr.Nr.: K12005604
Exercise 11
"""

import numpy as np
# from numba import jit


def __get_next_state__(state) -> np.ndarray:
    """
    Computes the next game state from old game state.
    Live cells = 1.
    Dead cells = 0.

    :param state: initial game state as 2D np array of type np.int
    :return: out_array: np.ndarray with next computed state
    """
    # create np.array with same shape as input state
    out_array = np.zeros(shape=(state.shape[0], state.shape[1]), dtype=np.int)
    # pad input state with zeros
    padded_state = np.pad(state, 1)

    # loop over all rows
    for row_index, row in enumerate(padded_state):
        # exclude padding
        if 1 <= row_index < (len(padded_state) - 1):
            # loop over all columns
            for cell_index, cell in enumerate(row):
                # exclude padding
                if 1 <= cell_index < (len(row) - 1):
                    # get sum of neighbors a cell currently has
                    neighbors = np.sum(
                        [padded_state[row_index - 1, cell_index], padded_state[row_index, cell_index - 1],
                         padded_state[row_index, cell_index + 1], padded_state[row_index + 1, cell_index],
                         padded_state[row_index - 1, cell_index - 1], padded_state[row_index + 1, cell_index - 1],
                         padded_state[row_index - 1, cell_index + 1], padded_state[row_index + 1, cell_index + 1]])
                    # if current cell is live cell
                    if state[row_index - 1, cell_index - 1] == 1:
                        # live cell dies by underpopulation or overpopulation
                        if (neighbors < 2) or (neighbors > 3):
                            out_array[row_index - 1, cell_index - 1] = 0
                        # live cell dies lives on
                        if (neighbors == 2) or (neighbors == 3):
                            out_array[row_index - 1, cell_index - 1] = 1
                    # if current cell is dead cell
                    if state[row_index - 1, cell_index - 1] == 0:
                        # dead cell becomes alive by reproduction
                        if neighbors == 3:
                            out_array[row_index - 1, cell_index - 1] = 1
    return out_array

# TODO: optimize with numba, try on linux
