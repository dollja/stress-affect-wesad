
# WEarable Stress and Affect Detection States

## Project Goal and Background

The goal of this project is to experiment with the WESAD multimodal dataset to become famliar with Python for deep learning.
The project uses different ML models to predict when an individual reaches a state of stress or increased stress.

[WESAD, a multimodal WEarable Stress and Affect Detection dataset](/references), is a collection of physiological signal data recorded from 12 subjects in which the experimenters induced a stressful state using the TSST (Tier Social Stress Test). Multiple physiological parameters in addition to acceleration information were captured during the experiments. They attached two diferent devices to each individual; one wrist worn and one chest worn and collected multiple modalities for each.

This project considers the chest worn device with a subset of the total number
of modalities.

## Data

WESAD dataset ~17 GB of raw data. Download link is [here](https://uni-siegen.sciebo.de/s/pYjSgfOVs6Ntahr/download).

Download and extract WESAD data set so that each subject has a folder (SX, where X = subject ID). Each subject folder contains the following files:

- SX_readme.txt: contains information about the subject (SX) and information about data collection and data quality (if applicable)
- SX_quest.csv: contains all relevant information to obtain ground truth, including the protocol schedule for SX and answers to the self-report questionnaires
- SX_respiban.txt: contains data from the RespiBAN device
- SX_E4_Data.zip: contains data from the Empatica E4 device
- SX.pkl: contains synchronised data and labels
- 17 subjects participated in the study. However, due to a sensor malfunction, data from two subjects (S1 and S12) had to be discarded.

## Model Descriptions

- [WESAD_all_models.ipynb](https://github.com/dollja/stress-affect-wesad/blob/main/WESAD_all_models.ipynb) contains all visualization techniques applied to the dataset
- [WESAD_visualizationa.ipynb](https://github.com/dollja/stress-affect-wesad/blob/main/WESAD_visualization.ipynb) consists of preprocessing along with different ML models such as LDA, QDA, Decision Trees, KNN along with techniques such as k-Fold Cross Validation along with   their analysis and optimization strategies employed.

# Implementation

## Environment

#### Install the required python libraries

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

## Directions

To run the notebooks and the python module:

- (1) Set a path to the git project ```module = os.path.abspath('C:/github/stress-affect-wesad/src/main')```
- (2) Set a path to the WESAD dataset  ```ROOT_PATH = 'C:/Users/dollj/OneDrive/Desktop/datasets/WESAD'```
- (3) Make sure to point DataManager.py and the Notebooks to the data source. See below example.
- (4) Run Demo.py to prepare, create, and evaluate an LSTM NN with one epoch and also load and evalute an LSTM NN with 5 epochs.

### File Structure

File Structure
/

demo.sh - driver that sets up, builds, trains, and tests model
readme.md
references/ - WESAD dataset and paper information
src/
src/main - Python3 modules
DataManager.py
Demo.py
src/notebooks - jupyter ipython notebooks
exploring-the-dataset.ipynb
feature-exploration.ipynb
feature-exploration-continued.ipynb
model-training.ipynb
demo
src/models - Directory for Keras model data files

### Development Process Notes

## Results
Performance using the LSTM based network architecture with one hidden layer
has performed with an accuracy of ~ 97.4% on the validation set using 5 epochs.

With just one epoch, the model has results between ~80% and ~92% for accuracy
on the validation data. Each epoch of training takes approximately 70 seconds
without GPU acceleration. At 5 epochs, the model outperforms the WESAD results for both accuracy and F1 using less modalities and less features.

<img src="https://github.com/dollja/stress_affect_wesad/blob/master/images/results_model-2022-12-1218_56_51_epochs5_learning_rate0_05.PNG">

## Future Work

Some future work items to complete may include: adding optimization strategies to improve performance i.e. feature selection techinques, adding different ML models QDA, Decision Trees, KNN, etc., and adding visualizations to the dataset.

- [ ] Add encoder-decoder attention layer 
- [ ] Add notebook with more model results for LDA, QDA, Decision Trees, KNN, SVM, PCA, and k-fold cross validation
- [ ] Update directions in README.md with notes on development process and performance using Windows


## References

Also, many thanks to the below mentioned authors for their past work:

-> <https://github.com/BradySheehan/wesad_experiments>

-> <https://github.com/WJMatthew/WESAD>
