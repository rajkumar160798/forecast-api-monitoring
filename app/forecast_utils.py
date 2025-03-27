# forecast_utils.py

import pandas as pd
from prophet import Prophet
import pickle
from datetime import datetime, timedelta

# Load model once
with open("model/prophet_model.pkl", "rb") as f:
    model = pickle.load(f)

def generate_forecast(start_date: str, periods: int) -> pd.DataFrame:
    # Convert string to datetime
    start_dt = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")

    # Create future dataframe
    future = pd.date_range(start=start_dt, periods=periods, freq="H")
    future_df = pd.DataFrame({"ds": future})

    # Predict
    forecast = model.predict(future_df)

    # Filter required fields
    return forecast[["ds", "yhat"]]
