import os
from pathlib import Path
import matplotlib 
import matplotlib.pyplot as plt 

#starting path 
fpath = './home/taran/projects/AVIMA' 
p = Path(fpath)
count=1 # count default

#create loop through all files in AVIMA folder

for file in p.glob('**/*'):
    if file.endswith('.json'):
        execfile('calc-dissim.py')
        plt.savefig('img'+str(count)+'.png')
        count +=1



#while os.path.isdir(fpath):
    #for file in os.listdir(fpath): # loop through the folder
        #print(file)   # print text to keep track the process
        #if file.endswith('.json'):
            #count+=1
            #print(file+'+1')

#from subprocess import call 

#class CallPy(file):
    
    #def __init__(self, path = fpath)
       #self.path = path 
    
    #def call_python_file(self):
        
        
        
        
        #call(["Python3", "{}".format(self.path)])


#for each each .json file, run calc-dissim.py 
#each rdm is img = imshow(euc_dist)



#File = namedtuple('File')

#empty list 
#files = []





            #call calc-dissim.py 
            #subprocess.run(['open', calc-dissim], check=True)


#fpath = '/home/taran/projects/AVIMA/1/Meadows_avima-image-version1_v_v2_better-hound_2_tree.json'


