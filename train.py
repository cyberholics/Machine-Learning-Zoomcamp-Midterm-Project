#import libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
import pickle

#read and load the data

data=pd.read_csv("/Users/victoroshimua/Downloads/card_transdata.csv")

#Splitting data as Full Train (80%), Test (20%) 
data_full_train, data_test = train_test_split(data,test_size=0.2,random_state=1)
data_full_train = data_full_train.reset_index(drop=True)
y_train=data_full_train.fraud

# training the model
dtrain=xgb.DMatrix(data_full_train, label= y_train)
xgb_params={
    'eta': 0.1, 
    'max_depth': 3,
    'min_child_weight': 1,

    'objective': 'binary:logistic',
    'eval_metric': 'auc',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1,
}

final_model = xgb.train(xgb_params, dtrain, num_boost_round=175)

# saving the final model

model_output_file = f'xgb_model.bin'
with open(model_output_file, 'wb') as f_out:
    pickle.dump((final_model),f_out)