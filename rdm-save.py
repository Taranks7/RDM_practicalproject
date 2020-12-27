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

# define fpath 
count=0 # count default
#i.e. fpath[0] will be the first filepath... 

path = '/home/taran/projects/AVIMA' 
rootdir = path
filepath = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.startswith('Meadows'):
            filepath.append(os.path.join(subdir, file))
            fpath = filepath[count]
            import plot-rdm
            #exec(open('plot-rdm.py').read())
            count +=1
            
#p = Path(path)
#for file in p.glob('**/*'):
    #if file.startswith('Meadows'):
        #fpath= filepath[count]
        
