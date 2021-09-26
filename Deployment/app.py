# 1. Library Imports
import uvicorn
from fastapi import FastAPI
from Customers import Customer
import numpy as np
import pandas as pd
import pickle

app = FastAPI()
churn_model = open('TCC-RF-clf.pkl', 'rb')
model = pickle.load(churn_model)


@app.get('/')
async def index():
    return {"message": "Hello API Masters"}


@app.get('/{name}')
async def get_name(name: str):
    return {'message': f'Hello, {name}'}


@app.post('/predict')
async def predict(data: Customer):
    data = data.dict()
    AccountWeeks = data['AccountWeeks']
    ContractRenewal = data['ContractRenewal']
    DataPlan = data['DataPlan']
    DataUsage = data['DataUsage']
    CustServCalls = data['CustServCalls']
    DayMins = data['DayMins']
    DayCalls = data['DayCalls']
    MonthlyCharge = data['MonthlyCharge']
    OverageFee = data['OverageFee']
    RoamMins = data['RoamMins']
    customer_feature = [[AccountWeeks, ContractRenewal, DataPlan, DataUsage, CustServCalls,
                         DayMins, DayCalls, MonthlyCharge, OverageFee, RoamMins]]
    prediction = model.predict(customer_feature)
    if prediction[0] == 0:
        prediction = "Will Not Churn"
    else:
        prediction = "Will Churn"
    return prediction


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
