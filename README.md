# Representational similarity analysis (RSA) of pairs of visual stimuli. Master's Practical Project 2020-21: Project Overview #
- RSA characterizes the representation of stimuli in an individual's brain or a computational model 
- Created a representational dissimilarity matrix (RDM) from 0 to 0.05 for participants using pairs of visual stimuli, reflecting percieved similairy between the stimuli
- Calculated the Pearson's correlation coefficient between pairs of stimuli to quantify the level of dissimilarity 

![rdm_plot](https://user-images.githubusercontent.com/74196907/105768107-ce1f1580-5f53-11eb-84d7-8567bfd7fcb6.png)

Figure 1. RDM for participant 1; 0 represents most similar pairs of stimuli and 0.05 represents least similar pairs. 
## Set up ## 
**Setting up the environment:**

```
cd RDM_researchproject/AVIMA
# CREATE VIRTUAL ENVIRONMENT
# virtualenv venv -p python3
source venv/bin/activate
```
- The data are presumed to be at ~/RDM_researchproject/AVIMA/
- Install dependencies: pip install -r requirements.txt

**Run plots**
```
python3 rdmsave.py
python3 disrdmsave.py
```
