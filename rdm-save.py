import os
count=0 # count default
f_path = './home/taran/projects/AVIMA' # set path
#loop 
while os.path.isdir(f_path):
    for file in os.listdir(f_path): # loop through the folder
        print(file)   # print text to keep track the process
        if file.endswith('.json'):
            count+=1
            print('+1')


fpath = '/home/taran/projects/AVIMA/1/Meadows_avima-image-version1_v_v2_better-hound_2_tree.json'


#plt.plot(euc_dist)
img = plt.imshow(euc_dist)
#save figures 
img_num = 1
for _ in range(len(participants)):
    plt.savefig('img'+str(img_num)+'.png')
    img_num += 1

plt.show()
