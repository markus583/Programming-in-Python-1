"""
Author: Markus Frohmann
Matr.Nr.: K12005604
Exercise 9
"""

# import relevant modules
import os
import argparse
import subprocess
import sys
from plot_csv import plot_csv

# add command line argument
parser = argparse.ArgumentParser()
parser.add_argument('output_folder', help='some foldername', type=str)

# get & store command line argument
args = parser.parse_args()
output_folder = args.output_folder

# create folder 200 in folder output_folder
# in this folder, hamstergenegen.py will generate data
input_folder = os.path.join(output_folder, '200')
os.makedirs(input_folder, exist_ok=True)

# create filename in output_folder where output of ex8.py will be stored
file = os.path.join(output_folder, 'patterns_analysis.csv')

# call hamstergenegen.py with argument input_folder (output_folder/200)
# generates 4000 files of hamster sequences
subprocess.call([sys.executable, 'hamstergenegen.py', input_folder])

# call ex8.py with arguments:
# input_folder (output_folder/200)
# file (output_folder/patterns_analysis.csv)
# subsequence 'ctag'

subprocess.call([sys.executable, 'ex8.py', input_folder, file, 'ctag'])

# # create filename in output_folder where output of plot_csv will be stored
plot_file = os.path.join(output_folder, 'patterns_analysis.png')

# finally, use plot_csv to create .png image
# inputfilename: file (output_folder/patterns_analysis.csv)
# outputfilename: plot_file (output_folder, 'patterns_analysis.png')
plot_csv(file, plot_file)
