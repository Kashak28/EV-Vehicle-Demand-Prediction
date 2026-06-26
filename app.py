from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="EV Forecast API")

# Load trained model
model = joblib.load("forecasting_ev_model.pkl")

# Input schema
class EVInput(BaseModel):
    months_since_start: int
    county_encoded: int
    ev_total_lag1: float
    ev_total_lag2: float
    ev_total_lag3: float
    ev_total_roll_mean_3: float
    ev_total_pct_change_1: float
    ev_total_pct_change_3: float
    ev_growth_slope: float

# Home endpoint
@app.get("/")
def home():
    return {"message": "EV Forecast API is running"}

# Prediction endpoint
@app.post("/predict")
def predict(data: EVInput):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)[0]

    return {
        "predicted_ev_count": float(prediction)
    }