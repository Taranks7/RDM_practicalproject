def calc_dissim(fpath, output_filename):
    import json
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

    #dissimilarity  
    for i in TP0:
        answer = (i['x']-i['y'])
        D = (abs(answer))
        
    import numpy as np
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

    #50x1
    arrx.reshape((1,-1))
    arry.reshape((1,-1))

    #euclidean distance between arrx arry points 
    def calc_euc(arrx, arry):
        return np.array([[np.linalg.norm(i-j) for j in arry] for i in arrx])
    
    euc_dist = (calc_euc(arrx, arry))
    #plt.plot((euc_dist.reshape(2500,).T))
    
    import matplotlib.pyplot as plt
        #need to make euc_dist an array with (2500/2 - diagonal)  
    euc_dist = euc_dist + euc_dist.T - np.diag(np.diag(euc_dist))
    
    stim = data['stimuli']

    y_names = []
    for i in stim:
        y_names.append(i['name'])
    
    x_names = []
    for i in stim:
        x_names.append(i['name'])
    
    import numpy as np
    
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(len(x_names)))
    ax.set_yticks(np.arange(len(y_names)))
    ax.set_xticklabels(x_names, fontsize = 5)
    ax.set_yticklabels(y_names[::-1], fontsize = 5)  
    plt.setp(ax.get_xticklabels(), rotation=90, ha="right")
    plt.imshow(euc_dist)
    plt.clim(0, 1)
    plt.colorbar(mappable=None, cax=None, ax=None)
    fig.subplots_adjust(bottom=0.23)
    
    plt.savefig(output_filename, bbox_inches='tight')
