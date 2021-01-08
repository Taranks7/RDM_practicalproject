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
    ax.set_yticklabels(y_names[::-1], fontsize = 5)  
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right")
   
    plt.imshow(srdm)
    plt.colorbar(mappable=None, cax=None, ax=None)
    fig.subplots_adjust(bottom=0.23)
    fig.suptitle('Representational Dissimilarity Matrix')
    plt.xlabel('Audio-visual stimuli')
    plt.ylabel('Audio-visial stimuli')
    plt.savefig(output_filename, bbox_inches='tight')
