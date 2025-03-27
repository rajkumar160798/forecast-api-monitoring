# Forecast API Monitoring with Anomaly Detection

This project demonstrates how to **monitor predictions from a deployed Prophet model** and trigger alerts for anomalies using **Apache Airflow**.

>  Built as part of a blog series on AI-driven Smart Automation (Blog 4)

---

##  Features

- Trains a time-series model using [Facebook Prophet](https://facebook.github.io/prophet/)
- Saves the trained model as `prophet_model.pkl`
- Loads predictions from a deployed FastAPI forecast model (or mock data)
- Detects anomalies in forecasts using residual thresholds
- Sends **email alerts** if anomalies are detected
- Containerized with **Docker**
- Ready for integration with **GCP (BigQuery/GCS)** – coming soon!

---

##  Tech Stack

- Python 3.x  
- Facebook Prophet  
- FastAPI  
- Pandas  
- Uvicorn  
- Docker 

---

##  Project Structure
```
forecast-api-monitoring/ 
│ ├── dags/ │ └── forecast_monitoring_dag.py # Airflow DAG for monitoring 
│ ├── models/ 
│ └── prophet_model.pkl # Trained Prophet model 
│ ├── train_and_save_model.py # Script to train and save the model 
├── load_prophet_model.py # Quick test script to load and forecast 
├── Dockerfile # Airflow-ready Docker setup 
├── requirements.txt # Python dependencies 
└── README.md # You're here!
```
---

##  Quick Start (Local)

1.**Clone the repo**
   ```bash
   git clone https://github.com/rajkumar160798/forecast-api-monitoring.git
   cd forecast-api-monitoring
```

2.**Create and activate a virtual environment**

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3.**Train and save the model**

```
python train_and_save_model.py
```

4.**Run Airflow in Docker**

```
docker-compose up --build
```

5.**Access the Airflow UI at http://localhost:8080**

---
## Email Alerts

If a forecasted value deviates significantly from the actual value, Airflow sends an email alert using EmailOperator.

Note: Configure SMTP or use a dummy email setup for local testing in your airflow.cfg or use send_email.py.

---

---

## 👨‍💻 Author
**Raj Kumar Myakala**  
AI | Data | Automation | GCP | Python  
[LinkedIn ](https://www.linkedin.com/in/raj-kumar-myakala-927860264/)  
[GitHub ](https://github.com/rajkumar160798)

---

>  If you like this project, consider starring the repo and following my GitHub for more AI/ML innovations!
