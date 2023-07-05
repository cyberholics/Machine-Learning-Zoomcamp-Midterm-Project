#This script sends request to web service which accepts transaction details and returns the prediction whether transaction is fraudulent or not
import numpy as np
import pandas as pd 
import requests

transaction = {
  "distance_from_home": 1.9808574511514092,
  "distance_from_last_transaction": 5.04247186357492,
  "ratio_to_median_purchase_price": 0.5889080718859896,
  "repeat_retailer": 1.0,
  "used_chip": 0.0,
  "used_pin_number": 0.0,
  "online_order": 0.0
}



url = 'http://localhost:9696/predict'
response = requests.post(url, json=transaction).json()
print(response)
