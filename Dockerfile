# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app/ .

# Expose port Flask runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "main.py"]
