import bentoml
from bentoml.io import JSON
import xgboost as xgb
import pandas as pd

model_ref = bentoml.xgboost.get("fraud_detection:latest")
model_runner = model_ref.to_runner()

svc = bentoml.Service("fraud_detection", runners=[model_runner])

@svc.api(input=JSON(), output=JSON())
def classify(fraud_details):
    df = pd.DataFrame(fraud_details, index=[0])
    prediction = model_runner.predict.run(df)
    result = prediction[0]
    print('Prediction:', result)
    if result > 0.5:
        return {'Transaction': 'Fraud'}
    else:
        return {'Transaction': 'Not Fraud'}
