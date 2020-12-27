def plot_rdm():
    with open(fpath) as fhandle:
        data = json.load(fhandle)
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

    plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    plt.plot(srdm)
    plt.imshow(srdm)
    plt.colorbar(mappable = None, cax = None, ax = None)
    fig.subplots_adjust(bottom=0.23)
#plt.show()

#save plot
    plt.savefig('rdm'+str(count)+'.png')

if __name__ == '__main__':
    plot_rdm()
