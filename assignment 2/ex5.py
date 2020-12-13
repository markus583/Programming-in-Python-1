"""
Author: Markus Frohmann
Matr.Nr.: K12005604
Exercise 5
"""

import re


def count_bases_and_subsequence(data_as_string: str, subsequence: str):
    # bases_all = []
    # set counter for bases
    A = 0
    T = 0
    C = 0
    G = 0

    # take subsequence and make it uppercase
    subsequence_upper = subsequence.upper()
    # make list out of subsequences
    subsequence_list = [x for x in subsequence_upper]

    # set subsequence_count to 0/initiate it
    subsequence_count = 0
    # set counter variable for proper length of subsequence to 0/initiate it
    i = 0

    for line in data_as_string.split('\n'):
        if line.startswith('#') or line.startswith('%') or line == '':
            # 1.) ignore empty lines (# and % just to make sure for both old/new formats) and lines that start with a %/# character.
            if line == '% End of data' or line == '# End of data':
                break
            else:
                # go into next iteration of loop (ignore line), and set counter variable for subsequence to 0
                i = 0
                continue

        elif line == '% End of data' or line == '# End of data':
            # exit loop if end of data is reached
            break
        else:
            # get proper base
            base = re.findall(';(.*);', line)
            if len(base) >= 1:
                base = base[0]
            base = base.upper()
            # get quality column
            columns = line.split(';')
            quality = float(columns[2])

            # check if bases are ACTG and if quality is > 0.08
            # only needed for debugging purposes, hence commented
            """
            if (base == 'A' or base == 'C' or base == 'T' or base == 'G') and quality > 0.08:
               bases_all.append(base)
            """
            # check if base == 'A/C/T/G' and quality is > 0.8
            # then increment A/T/C/G
            if base == 'A' and quality >= 0.08:
                A += 1
            elif base == 'T' and quality >= 0.08:
                T += 1
            if base == 'C' and quality >= 0.08:
                C += 1
            if base == 'G' and quality >= 0.08:
                G += 1

            # special case: if start of subsequence occurs several times in a row
            if subsequence_list[0] == base and i >= 1 and subsequence_list[1] != base:
                i = 0
            # check if 1st element of subsequence == current base AND quality >= 0.08
            if subsequence_list[i] == base and quality >= 0.08:
                # increment i, such that  next base is considered
                i += 1
                if i == len(subsequence_list):
                    # i has reached length(subsequence_list) --> entire subsequence has been achieved:
                    # reset i
                    i = 0
                    # increase count of subsequence_count
                    subsequence_count += 1
            else:
                # if next base is not correct, reset counter i
                i = 0

    # create list of bases, which store values of count of bases
    bases = [A, C, G, T]
    # create dict consisting of bases_vars and count of bases
    bases_vars = ['a', 'c', 'g', 't']
    bases_dict = dict(zip(bases_vars, bases))

    return subsequence_count, bases_dict


"""
# for testing purposes only:

filename = 'correct_7.seq.raw'  # This is the name or path of the file to read
with open(filename, 'r') as fh:
    file_content = fh.read()
# At this point file content will be the file content as string
# Your function should be callable like this:
subsequence_count, base_counts = count_bases_and_subsequence(data_as_string=
                                                             file_content, subsequence='AT')
print(subsequence_count)
print(base_counts)

"""
