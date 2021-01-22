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
def plot_rdm(fpath, output_filename):
    with open(fpath) as fhandle:
        data = json.load(fhandle)
        # inspect rdm stimuli labels

    stim = data['stimuli']

    # contain all labels for y axis and x axis seperately
    y_names = []
    for i in stim:
        y_names.append(i['name'])

    x_names = []
    for i in stim:
        x_names.append(i['name'])

    # create rdm array and squareform
    rdm_array = np.array(data['rdm'])
    srdm = squareform(rdm_array)

    # label x and y axis on rdm
    fig, ax = plt.subplots()

    ax.set_xticks(np.arange(len(x_names)))
    ax.set_yticks(np.arange(len(y_names)))

    ax.set_xticklabels(x_names, fontsize = 5)
    ax.set_yticklabels(y_names, fontsize = 5)  
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right")
   
    plt.imshow(srdm)
    plt.colorbar(mappable=None, cax=None, ax=None)
    fig.subplots_adjust(bottom=0.23)
    fig.suptitle('Representational Dissimilarity Matrix of pairs of audio-visual stimuli')
    plt.xlabel('Second element of audio-visual stimuli pair')
    plt.ylabel('First element of audio-visial stimuli pair')
    plt.savefig(output_filename, bbox_inches='tight')
    
    # create tables
def calc_dis(fpath, output_filename):
    with open(fpath) as fhandle:
        data = json.load(fhandle)

    stim = data['stimuli']
    rdm_array = np.array(data['rdm'])
    srdm = squareform(rdm_array)

    x_names = []
    for i in stim:
        x_names.append(i['name'])
    
    import pandas as pd
    DF = pd.DataFrame(srdm, columns = [x_names], index = [x_names])
    DF.to_csv(output_filename)
    
def calc_sim(fpath, output_filename):
    with open(fpath) as fhandle:
        data = json.load(fhandle)

    stim = data['stimuli']
    rdm_array = np.array(data['rdm'])
    srdm = squareform(rdm_array)

    x_names = []
    for i in stim:
        x_names.append(i['name'])
    
    import pandas as pd
    DF = pd.DataFrame(srdm, columns = [x_names], index = [x_names])
    
    #select columns from 0 to 0.01
    SDF = DF[(DF>-1) & (DF<0.01)]
    SDF.to_csv(output_filename)
        
    DF = pd.DataFrame(x_names)
    DF.to_csv("stimuli.csv")
        
def corr(fpath, output_filename):
    with open(fpath) as fhandle:
        data = json.load(fhandle)

    stim = data['stimuli']
    rdm_array = np.array(data['rdm'])
    srdm = squareform(rdm_array)

    x_names = []
    for i in stim:
        x_names.append(i['name'])
    
    import pandas as pd
    DF = pd.DataFrame(srdm, columns = [x_names], index = [x_names])
    CDF = DF.corr()
    CDF.to_csv(output_filename)      

def str_corr(fpath, output_filename):
    with open(fpath) as fhandle:
        data = json.load(fhandle)

    stim = data['stimuli']
    rdm_array = np.array(data['rdm'])
    srdm = squareform(rdm_array)

    x_names = []
    for i in stim:
        x_names.append(i['name'])
    
    import pandas as pd
    DF = pd.DataFrame(srdm, columns = [x_names], index = [x_names])
    CDF = DF.corr()
    STRDF = CDF[(CDF>=0.8) & (CDF>=-0.8)]
    
    STRDF.to_csv(output_filename)     
