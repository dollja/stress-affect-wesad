
# Classification of Wearable Stress and Affect Detection States

## Data

WESAD dataset: https://uni-siegen.sciebo.de/s/pYjSgfOVs6Ntahr/download

~17 GB of raw data. Download and extract WESAD data set so that each subject has a folder (SX, where X = subject ID). Each subject folder contains the following files:

SX_readme.txt: contains information about the subject (SX) and information about data collection and data quality (if applicable)
SX_quest.csv: contains all relevant information to obtain ground truth, including the protocol schedule for SX and answers to the self-report questionnaires
SX_respiban.txt: contains data from the RespiBAN device
SX_E4_Data.zip: contains data from the Empatica E4 device
SX.pkl: contains synchronised data and labels
17 subjects participated in the study. However, due to a sensor malfunction, data from two subjects (S1 and S12) had to be discarded.

## Models
- [WESAD_all_models.ipynb](https://github.com/dollja/stress-affect-wesad/blob/main/WESAD_all_models.ipynb) contains all visualization techniques applied to the dataset
- [WESAD_visualizationa.ipynb](https://github.com/dollja/stress-affect-wesad/blob/main/WESAD_visualization.ipynb) consists of preprocessing along with different ML models such as LDA, QDA, Decision Trees, KNN along with techniques such as k-Fold Cross Validation along with   their analysis and optimization strategies employed.


## References
Also, many thanks to the below mentioned authors for their past work:

-> https://github.com/BradySheehan/wesad_experiments

-> https://github.com/WJMatthew/WESAD
