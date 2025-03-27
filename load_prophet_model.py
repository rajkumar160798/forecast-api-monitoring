import pickle
import matplotlib.pyplot as plt
from prophet.plot import plot_plotly

# Load the model
with open('model/prophet_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Optional: make a future DataFrame and predict
future = model.make_future_dataframe(periods=10)
forecast = model.predict(future)

# Print forecast
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())


plot_plotly(model, forecast)