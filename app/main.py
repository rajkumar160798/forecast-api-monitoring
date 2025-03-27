# main.py (with Prometheus metrics)

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from .forecast_utils import generate_forecast

app = FastAPI()

# Define Prometheus metrics
REQUEST_COUNT = Counter("api_requests_total", "Total API Requests")
FAILURE_RISK_COUNT = Counter("failure_risks_total", "Total High Failure Risk Predictions")

# Input schema
class ForecastRequest(BaseModel):
    start_date: str
    periods: int

# Output schema
class ForecastPoint(BaseModel):
    ds: str
    yhat: float
    failure_risk: bool

class ForecastResponse(BaseModel):
    forecast: List[ForecastPoint]

@app.post("/predict", response_model=ForecastResponse)
def predict(request: ForecastRequest):
    REQUEST_COUNT.inc()
    try:
        forecast_df = generate_forecast(request.start_date, request.periods)
        response = []
        for row in forecast_df.itertuples():
            risk = row.yhat > 78
            if risk:
                FAILURE_RISK_COUNT.inc()
            response.append(ForecastPoint(
                ds=row.ds.strftime("%Y-%m-%d %H:%M:%S"),
                yhat=round(row.yhat, 2),
                failure_risk=risk
            ))
        return {"forecast": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)