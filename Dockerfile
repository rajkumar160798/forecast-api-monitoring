# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code and model
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (for FastAPI)
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
