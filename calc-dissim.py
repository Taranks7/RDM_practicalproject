import numpy as np
import matplotlib 
import matplotlib.pyplot as plt 
import scipy
import scipy.spatial
import scipy.spatial.distance as sd

import json 

fpath = '/home/taran/projects/AVIMA/1/Meadows_avima-image-version1_v_v2_better-hound_2_tree.json'

with open(fpath) as fhandle:
    data = json.load(fhandle)

DT = data['trials']

print(len(DT))
#there are 133 trials 
#the first will be T0 
#the last will be T132
#each trial has 50 items, each with x and y coordinates 

T0 = data['trials'][0]
dir(T0)
type(T0)
T0.keys()

#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list. 

TP0 = T0['positions']
type(T0['positions'])

#first PO abs(x-y) value
P0 = TP0[0]
P0.keys()
x0 = P0['x']
y0 = P0['y']
abs(x0-y0)

#assign x and y variables 
for i in TP0:
     X = (i['x'])
     ax = abs(X)
     
for i in TP0:
     Y = (i['y'])
     ay = abs(Y)
     
#there will be 50 x,y coordinates

#dissimilarity  
for i in TP0:
     answer = (i['x']-i['y'])
     D = (abs(answer))

#create zeros matrix
arr = np.zeros([50, 50])


#create y array 
ly = []
for i in TP0:
    Y = (abs(i['y']))
    ly.append(Y)
arry = np.array(ly)

#check
type(arry)

#x array with 50 variables
lx = []
for i in TP0:
    X = (abs(i['x']))
    lx.append(X)
arrx = np.array(lx)

#50x1
arrx.reshape((25,2))
arry.reshape((25,2))

arrx = abs(arrx)
arry = abs(arry)

#euclidean distance between arrx arry points 
def calc_euc(arrx, arry):
    return np.array([[np.linalg.norm(i-j) for j in arry] for i in arrx])
euc_dist = (calc_euc(arrx, arry))
plt.plot((euc_dist.reshape(2500,).T))

#need to make euc_dist an array with (2500/2 - diagonal)  
euc_dist = euc_dist + euc_dist.T - np.diag(np.diag(euc_dist))
img = plt.imshow(euc_dist)


#loop through 133 trials  -dont need to, only first trial
#t = {}
#for i in range(len(DT)):
    #t = data['trials'][i]
