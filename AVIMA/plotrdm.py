def plot_rdm(fpath):
    import numpy as np
    import matplotlib
    import matplotlib.pyplot
    import matplotlib.pyplot as plt
    import scipy
    import scipy.spatial
    import scipy.spatial.distance as sd
    from scipy.spatial.distance import squareform
    import json 
    
    with open(fpath) as fhandle:
        data = json.load(fhandle)
	 #inspect rdm stimuli labels 
    stim = data['stimuli']

	#contain all labels for y axis and x axis seperately  
    y_names = []
    for i in stim:
        y_names.append(i['name'])

    x_names = []
    for i in stim:
        x_names.append(i['name'])

	#create rdm array and squareform 
    rdm_array = np.array(data['rdm'])
    srdm = squareform(rdm_array)

	#label x and y axis on rdm 
    fig, ax = plt.subplots()
    rdm = ax.imshow(srdm)

    ax.set_xticks(np.arange(len(x_names)))
    ax.set_yticks(np.arange(len(y_names)))

    ax.set_xticklabels(x_names)
    ax.set_yticklabels(y_names)
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    plt.plot(srdm)
    plt.imshow(srdm)
    plt.colorbar(mappable = None, cax = None, ax = None)
    fig.subplots_adjust(bottom=0.23)
import matplotlib.pyplot as plt
plt.savefig('rdm.png')
