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

#filepath 
path = '/home/taran/projects/AVIMA' 
rootdir = path
filepath = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.startswith('Meadows'):
            filepath.append(os.path.join(subdir, file))
for i in enumerate(filepath):
    fpath = filepath
for f in fpath:
    with open(f) as fhandle:
        data= json.load(fhandle)

#with open(fpath) as fhandle:
    #data = json.load(fhandle)
   
#inspect rdm stimuli labels 
stim = data['stimuli']

type(stim)
type(stim[0])
len(stim)
#stim is a list of 50 dict elements 

#contain all labels for y axis and x axis seperately  
y_names = []
for i in stim:
   y_names.append(i['name'])
   
x_names = []
for i in stim:
   x_names.append(i['name'])

#inspect rdm data   
data['rdm']
rdm_array = np.array(data['rdm'])
rdm_array.shape

#plt.plot(rdm_array.T)
#plt.show()

srdm = squareform(rdm_array)


#label x and y axis on rdm 

fig, ax = plt.subplots()
rdm = ax.imshow(srdm)

ax.set_xticks(np.arange(len(x_names)))
ax.set_yticks(np.arange(len(y_names)))

ax.set_xticklabels(x_names)
ax.set_yticklabels(y_names)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")
plt.plot(srdm)
plt.imshow(srdm)
plt.colorbar(mappable = None, cax = None, ax = None)

#plt.show()
plt.savefig(RDM)
