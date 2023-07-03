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
print("The data has been read ")

#Splitting data as Full Train (80%), Test (20%) 
data_full_train, data_test = train_test_split(data,test_size=0.2,random_state=1)
data_full_train = data_full_train.reset_index(drop=True)
y_train=data_full_train.fraud
print("The data has been splitted")
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
print("The data is getting fitted")
print("Hold on the model is been trained, this might take some time ")
final_model = xgb.train(xgb_params, dtrain, num_boost_round=175)
print("trained succesfully")
# saving the final model
print("saving the model")
model_output_file = f'xgb_model.bin'
with open(model_output_file, 'wb') as f_out:
    pickle.dump((final_model),f_out)

print("model saved ")
    
