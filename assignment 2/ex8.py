# import functions from previous exercises and relevant modules
from ex5 import count_bases_and_subsequence
from ex6 import get_hamsters
from ex7 import get_file_metadata
import numpy as np
import pandas as pd
import argparse

# add command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('input_folder', help='some foldername', type=str)
parser.add_argument('output_folder', help='some foldername', type=str)
parser.add_argument('subsequence', type=str)

# get & store command line arguments
args = parser.parse_args()
input_folder = args.input_folder
output_folder = args.output_folder
subsequence = args.subsequence

# get generator for reading files
generator = get_hamsters(input_folder)

"""
initialize np-array with zeros where:
each row corresponds to a date
column 1 to given subsequence; column 2,3,4,5 to base a,c,g,t
datatype is float64
"""
array = np.zeros(shape=(200, 5), dtype=np.float64)

# loop over all the files with our generator
for file_name, file_content in generator:
    # store date (_, which would be the ID and columns, are not needed here)
    _, date, _ = get_file_metadata(file_content)

    # get count of subsequences as int and number of bases as dict
    subsequence_count, bases_dict = count_bases_and_subsequence(file_content, subsequence)

    # update array in row date with current counts
    array[date, :] += subsequence_count, bases_dict['a'], bases_dict['c'], bases_dict['g'], bases_dict['t']

# for debugging purposes:
# np.set_printoptions(suppress=True)

# finally, divide everything by 20 to get average counts for each date
array[:] /= 20

# create Pandas dataframe to make outputfile
out_basefile = pd.DataFrame(array)

# rename columns to (separated by space):
# subsequence a c g t
out = out_basefile.rename(columns={0: 'subsequence', 1: 'a', 2: 'c', 3: 'g', 4: 't'})

# save pd.Dataframe to given output_folder
# without row index
# separator is space (' ')
out.to_csv(output_folder, index=False, sep=' ')
