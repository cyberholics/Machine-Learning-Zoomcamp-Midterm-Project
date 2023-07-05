#import libraries
import pickle
import pandas as pd
import xgboost as xgb
from flask import Flask
from flask import request
from flask import jsonify

print("libraries imported")
# declear parameters  

model_file= 'xgb_model.bin'
threshold=0.5

#open the saved model
print("opening the saved model")
with open (model_file,'rb') as f_in:
    model=pickle.load(f_in)

# prediction service
print("creating prediction service")
def predict_fraud_transaction(transaction_details):
    #convert json to pandas dataframe and then Dmatrix
    transaction_series = pd.Series(transaction_details)
    transaction_dmatrix = xgb.DMatrix(pd.DataFrame(transaction_series).T)

    # prediction using the transaction_dmatrix and model
    prediction = model.predict(transaction_dmatrix)
    fraud=(prediction >= threshold)
    return fraud, prediction
    


app= Flask('Fraud')

@app.route('/predict', methods=['POST'])
def predict():
    transaction_details= request.get_json()
    fraud, prediction =predict_fraud_transaction(transaction_details)
    
    if fraud:
        description = "Transaction is Fraudulent, please stop this transaction"
    else:
        description = "This is not a fraudulent transaction"
        
    result = {'fraud_probability': float(prediction),
            'fraud': bool(fraud),
            'description': description
            }
    
    return jsonify(result)



if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0', port=9696)

