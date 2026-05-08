from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Global Temperature Predictor")

model = joblib.load("models/LinearRegression.joblib")

class Features(BaseModel):
    year: int
    month: int
    temp_lag1: float
    temp_lag2: float
    temp_lag12: float

@app.post("/predict")
def predict(features: Features):
    X = np.array([[
        features.year, features.month,
        features.temp_lag1, features.temp_lag2, features.temp_lag12
    ]])
    pred = model.predict(X)[0]
    return {"predicted_temperature": round(pred, 4)}