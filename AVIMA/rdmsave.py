#import libraries
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 
import scipy
import scipy.spatial
import scipy.spatial.distance as sd
from scipy.spatial.distance import squareform
import os
import json 
from subprocess import * 
import time

# define fpath 
#i.e. fpath[0] will be the first filepath... 

path = '/home/taran/projects/AVIMA' 
rootdir = path
filepath = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.startswith('Meadows'):
            count=0 # count default
            filepath.append(os.path.join(subdir, file))
            fpath = filepath[count]
            Popen('plotrdm.py')
            time.sleep(1)
            count +=1      