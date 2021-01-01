#import libraries
import numpy as np
import matplotlib
import matplotlib.pyplot
import matplotlib.pyplot as plt
import scipy
import scipy.spatial
import scipy.spatial.distance as sd
from scipy.spatial.distance import squareform
import os
import json 

# define fpath 
#i.e. fpath[0] will be the first filepath... 

path = '/home/taran/RDM_researchproject/AVIMA' 
rootdir = path
filepath = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.startswith('Meadows'):
            count=0 # count default
            filepath.append(os.path.join(subdir, file))
            fpath = filepath[count]
            os.system("/home/taran/RDM_researchproject/AVIMA/plotrdm.py")
            count +=1  
