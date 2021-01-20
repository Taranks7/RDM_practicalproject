import numpy as np
import matplotlib
import matplotlib.pyplot
import matplotlib.pyplot as plt
import scipy
import scipy.spatial
import scipy.spatial.distance as sd
from scipy.spatial.distance import squareform
import json
import matplotlib.pyplot as plt

def calc_dissim(fpath, output_filename):
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

    #assign x and y variables 
    for i in TP0:
        X = (i['x'])
        ax = abs(X)

    for i in TP0:
        Y = (i['y'])
        ay = abs(Y)

    #create y array 
    ly = []
    for i in TP0:
        Y = (abs(i['y']))
        ly.append(Y)
        arry = np.array(ly)

    #x array
    lx = []
    for i in TP0:
        X = (abs(i['x']))
        lx.append(X)
        arrx = np.array(lx)

	arrx = arrx.reshape((50,1))
    arry = arry.reshape((50,1))
    
    #scale of colourbar  
    arrx = arrx/25
    arry = arry/25
    
    #euclidean distance between arrx arry points 
    euc_dist = sd.cdist(arrx, arry, metric='euclidean') 
    
    #def calc_euc(arrx, arry):
        #return np.array([[np.linalg.norm(i-j) for j in arry] for i in arrx])
    #euc_dist = (calc_euc(arrx, arry))
    
    #plt.plot((euc_dist.reshape(2500,).T))
    
        #need to make euc_dist an array with (2500/2 - diagonal)  
    euc_dist = euc_dist + euc_dist.T - np.diag(np.diag(euc_dist))
    
    stim = data['stimuli']

    y_names = []
    for i in stim:
        y_names.append(i['name'])
    
    x_names = []
    for i in stim:
        x_names.append(i['name'])
    
    # label x and y axis on rdm
    fig, ax = plt.subplots()

    ax.set_xticks(np.arange(len(x_names)))
    ax.set_yticks(np.arange(len(y_names)))

    ax.set_xticklabels(x_names, fontsize = 5)
    ax.set_yticklabels(y_names, fontsize = 5)  
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right")
   
    plt.imshow(euc_dist)
    fig.suptitle('Representational Dissimilarity Matrix')
    plt.xlabel('Audio-visual stimuli')
    plt.ylabel('Audio-visial stimuli')
    plt.colorbar(mappable=None, cax=None, ax=None)
    fig.subplots_adjust(bottom=0.23)
    plt.savefig(output_filename, bbox_inches='tight')
