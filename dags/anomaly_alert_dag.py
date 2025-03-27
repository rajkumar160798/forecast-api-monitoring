from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pickle
import pandas as pd
from email_alert import send_anomaly_email
from prophet.diagnostics import cross_validation

MODEL_PATH = '/opt/airflow/models/prophet_model.pkl'

def detect_anomalies():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    future = model.make_future_dataframe(periods=7)
    forecast = model.predict(future)

    forecast['uncertainty'] = forecast['yhat_upper'] - forecast['yhat_lower']
    anomalies = forecast[forecast['uncertainty'] > 0.01]

    if not anomalies.empty:
        send_anomaly_email(
            subject="🚨 Anomaly Detected in Forecast",
            message=anomalies[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_string(),
            recipient="test@example.com"
        )

with DAG(
    dag_id='anomaly_email_alert_dag',
    default_args={'owner': 'raj', 'retries': 1, 'retry_delay': timedelta(minutes=2)},
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['forecast', 'alert']
) as dag:

    task_check_and_alert = PythonOperator(
        task_id='check_for_anomalies',
        python_callable=detect_anomalies
    )

    task_check_and_alert