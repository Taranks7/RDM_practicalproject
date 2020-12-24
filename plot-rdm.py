import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 
import scipy
import scipy.spatial
import scipy.spatial.distance as sd

import json 

fpath = '/home/taran/projects/AVIMA/1/Meadows_avima-image-version1_v_v2_better-hound_2_tree.json'

with open(fpath) as fhandle:
   ...:    data = json.load(fhandle)
   
#inspect rdm stimuli labels 
data['stimuli']

#contain all labels for y axis and x axis seperately  
y_names = []
for i in stim:
   y_names = (i['name'])
   
x_names = []
for i in stim:
   x_names = (i['name'])

#inspect rdm data   
data['rdm']
rdm_array = np.array(data['rdm'])
rdm_array.shape

plt.plot(rdm_array.T)
#plt.show()

from scipy.spatial.distance import squareform
srdm = squareform(rdm_array)
plt.plot(srdm)
plt.imshow(srdm)
plt.colorbar(mappable = None, cax = None, ax = None)

#label x and y axis on rdm 

fig, ax = plt.subplots()
rdm = ax.imshow(srdm)

ax.set_xticks(np.arange(len(x_names)))
ax.set_yticks(np.arange(len(y_names)))

ax.set_xticklabels(x_names)
ax.set_yticklabels(y_names)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

for i in range(len(x_names)):
    for j in range(len(y_names)):
        text = ax.text(j, i, srdm[i, j])

plt.show()



