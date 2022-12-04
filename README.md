
# WEarable Stress and Affect Detection States

## Project Goal and Background

The goal of this project is to experiment with the WESAD multimodal dataset to become famliar with Python for deep learning.
The project development files include Jupyter notebooks and a python module with code for preprocessing and different ML models to predict when an individual reaches a state of stress or increased stress.


[WESAD, a multimodal WEarable Stress and Affect Detection dataset](/references), is a collection of physiological signal data recorded from 12 subjects in which the experimenters induced a stressful state using the TSST (Tier Social Stress Test). Multiple physiological parameters in addition to acceleration information were captured during the experiments. They attached two diferent devices to each individual; one wrist worn and one chest worn and collected multiple modalities for each.

This project considers the chest worn device with a subset of the total number
of modalities.

## Data and Project Structure

WESAD dataset ~17 GB of raw data. Download link is [here](https://uni-siegen.sciebo.de/s/pYjSgfOVs6Ntahr/download).


Download and extract WESAD data set so that each subject has a folder (SX, where X = subject ID). Each subject folder contains the following files:

- SX_readme.txt: contains information about the subject (SX) and information about data collection and data quality (if applicable)
- SX_quest.csv: contains all relevant information to obtain ground truth, including the protocol schedule for SX and answers to the self-report questionnaires
- SX_respiban.txt: contains data from the RespiBAN device
- SX_E4_Data.zip: contains data from the Empatica E4 device
- SX.pkl: contains synchronised data and labels
17 subjects participated in the study. However, due to a sensor malfunction, data from two subjects (S1 and S12) had to be discarded.

### Set up the environment
To run the notebooks and the python module:
- set a path to the git project
- set a path to the WESAD dataset. (ROOT_PATH = '\Users\dollj\Desktop\datasets\WESAD\'

####  Dependencies
- Python3 
- pandas
- matplotlib
- numpy
- sklearn
- graphviz
- seaborn
- xgboost
- statsmodel.api
- pickle
- ipython and jupyter for jupyter notebook


#### Directions
 1. Download and extract WESAD data set so that each subject has a folder (SX, where X = subject ID). 
 2. Point the DataManager.py and Notebooks to the data source.
 3. Run Demo.py to prepare, create, and evaluate an LSTM NN. The demo prints the results.


## Models
- [WESAD_all_models.ipynb](https://github.com/dollja/stress-affect-wesad/blob/main/WESAD_all_models.ipynb) contains all visualization techniques applied to the dataset
- [WESAD_visualizationa.ipynb](https://github.com/dollja/stress-affect-wesad/blob/main/WESAD_visualization.ipynb) consists of preprocessing along with different ML models such as LDA, QDA, Decision Trees, KNN along with techniques such as k-Fold Cross Validation along with   their analysis and optimization strategies employed.


## References
Also, many thanks to the below mentioned authors for their past work:

-> https://github.com/BradySheehan/wesad_experiments

-> https://github.com/WJMatthew/WESAD
