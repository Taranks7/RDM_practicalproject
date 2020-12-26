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
import pathlib
from pathlib import Path


def paths_files_from_args(paths_args, fn_match_test):
     class oSet(OrderedDict):
        def add(self, k):
            self.__setitem__(k, None)

        paths_files = oSet()

        for test_path in paths_args:
            test_path = Path(test_path).expanduser().resolve()
    
        if fn_match_test(test_path):
                paths_files.add(test_path)
                continue  # next test_path

        # walk the directory structure
        for path_dir_root, sub_directories, names_files in os.walk(test_path):
            for filename in names_files:
                if fn_match_test(filename):
                    paths_files.add(pathlib.Path(path_dir_root, filename))
            return list(paths_files)
paths_files_from_args('/home/taran/projects/AVIMA', lambda x: x.endswith(".json")))
    
    
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

#save plot
count=1 # count default

fpath = './home/taran/projects/AVIMA' 
p = Path(fpath)

#loop through all files in AVIMA folder
for file in p.glob('**/*'):
    if file.endswith('.json'):
        plt.savefig('img'+str(count)+'.png')
        count +=1
