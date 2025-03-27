from prophet import Prophet
import pandas as pd
import pickle

# Sample DataFrame
df = pd.DataFrame({
    'ds': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'y': range(365)
})

# Train the model
model = Prophet()
model.fit(df)

# Save the model as a pickle
with open('model/prophet_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")
