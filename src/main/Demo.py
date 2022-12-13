# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:32:39 2019

@author: Brady Sheehan
"""

import os
import sys
# module = os.path.abspath('/home/learner/DLA_project/src/main')
module = os.path.abspath('C:/github/stress-affect-wesad/src/main')
if module not in sys.path:
    sys.path.append(module)
from DataManager import DataManager

class Demo:
    
    manager = DataManager()
        
    print("Preparing data for model creation..")
    manager.load_all()
    print("Considering baseline experiment data:")
    manager.compute_features()
    print("Considering stress experiment data:")
    manager.compute_features_stress()
    
    batch_size = 4
    epochs = 5
    print("===============================================================")
    
    print("Creating the LSTM network with", epochs, "epochs.")
    # compute for one epoch
    (model, X_train, X_test, y_train, y_test) = \
        manager.create_network(epochs, batch_size)
        
    print("===============================================================")
    
    print("Evaluating LSTM network with", epochs, "epochs.")
    manager.get_model_results(model, X_train, X_test, y_train, y_test, batch_size)
    
    
    print("===============================================================")
    
    print("Loading and evaluating LSTM network from 5 epochs")
    # then load a previously computed 5 epoch model and display the results
   # model_5_epochs = manager.load_model('model-2022-12-0520_39_14.h5')
    model_5_epochs = manager.load_model('model-2022-12-1218_56_51.h5')
    manager.get_model_results(model_5_epochs, X_train, X_test, y_train, y_test )

