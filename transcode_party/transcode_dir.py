__author__ = 'sullivan'

import os

directory = "/home/sullivan/Data/epic_ctc_analysis"

dirs = filter(lambda x: os.path.isdir(os.path.join(directory, x)), os.listdir(directory))

for dir in dirs:
    print dir
