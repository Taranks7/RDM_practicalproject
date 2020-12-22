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
   
data['stimuli']
   
data['rdm']
rdm_array = np.array(data['rdm'])
rdm_array.shape

plt.plot(rdm_array.T)

plt.show()

from scipy.spatial.distance import squareform
srdm = squareform(rdm_array)
plt.plot(srdm)
plt.imshow(srdm)
plt.show()

#add axes and olourbar 
#colorbar()
#plt.show.colorbar()
#img = plt.imshow(srdm)
#colorbar(img)
#img = (plt.imshow(srdm)) colorbar()
#img.colorbar
#img.colorbar.show()
#plt.colorbar
#plt.colorbar(heatmap)
#plt.colorbar(cMap)