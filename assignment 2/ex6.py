# import necessary modules for file handling
import os
import glob


def get_hamsters(folderpath: str):
    # get files in folder and subfolders, stored as list
    found_files = glob.glob(os.path.join(folderpath, '**', '*.raw.seq'), recursive=True)
    # sort files in-place alphabetically
    found_files.sort()

    # loop through each file in found_files
    for file in found_files:
        # get rid of subfolders in filename
        filename = os.path.basename(file)
        # open file (original filepath is used!)
        with open(file, 'r') as f:
            # read current file, store it in file_content
            file_content = f.read()
        # return tuple:
        # 1.) base filename of current path
        # 2.) content of current filename as a string
        yield filename, file_content
