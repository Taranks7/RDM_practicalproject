# Representational similarity analysis (RSA) (Master's Research Project 2020-21): Project Overview #
- create representational dissimilarity matrix (RDM) for participants using pairs of visual stimuli, reflecting Euclidean distances between the stimuli
-  rsa characterizes the representation of stimuli in an individual's brain or a computational model 
[rdm_1.pdf](https://github.com/Taranks7/RDM_researchproject/files/5869747/rdm_1.pdf)

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
