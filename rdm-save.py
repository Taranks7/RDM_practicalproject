import os
from pathlib import Path
import matplotlib 
import matplotlib.pyplot as plt 

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
            
p = Path(path)
for file in p.glob('**/*'):
    if file.endswith('.json'):
        fpath= filepath[count]
        exec(open('plot-rdm.py').read())
        #plt.savefig('img'+str(count)+'.png')
        count +=1
