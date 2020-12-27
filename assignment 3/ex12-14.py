from pathlib import Path
import subprocess

import os


class GameOfLife(object):
    # Here you should modify the __init__ method (ex12)
    def __init__(self, configpath: str, outputfile: str):
        # provide attributes from method
        self.n_iterations, self.dead_symbol, self.live_symbol, self.state = self.read_config_file(configpath)
        self.current_iteration = 0  # set initial iteration
        # get directory and write file
        self.outputfile = os.path.join(outputfile)
        with open(self.outputfile, 'w') as f:
            pass  # file is empty
        # get and make directory for plots
        plot_dir_child = Path(self.outputfile)
        plot_dir = plot_dir_child.parent
        os.makedirs(os.path.join(plot_dir, 'plots'), exist_ok=True)

    # Here you should modify the __write_state__ method (ex13)
    def __write_state__(self):
        # open file in append mode
        with open(self.outputfile, 'a') as f:
            for line in self.state:  # loop over lines
                for symbol in line:  # loop over symbols
                    if symbol == 0:
                        f.write(self.dead_symbol)
                    else:
                        f.write(self.live_symbol)
                else:
                    f.write('\n')  # entering next line
            else:
                f.write('\n')  # newline at end of file

    # Here you should modify the make_video method (ex14)
    def make_video(self, video_filename: str):
        # BEFORE RUNNING, ENSURE THAT video_filename DOES NOT EXIST!!!
        # get proper path of images
        image_dir_child = Path(self.outputfile)
        image_dir_above = image_dir_child.parent
        image_dir = os.path.join(image_dir_above, 'plots', '*.png')
        # get proper path to save video to
        video_pathname = os.path.join(image_dir_above, video_filename)

        # create video with ffmpeg (fewer arguments for better compatibility)
        p = subprocess.Popen(
            ['ffmpeg', '-framerate', '10', '-pattern_type', 'glob', '-i', image_dir, '-c:v', 'libx264',
             '-pix_fmt', 'yuv420p', video_pathname])

        # make sure that unittest waits for video to be created
        _ = p.wait(timeout=15)