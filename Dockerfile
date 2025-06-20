# Use a slim Python image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy app code into container
COPY app/ .

# Install dependencies
RUN pip install flask requests

# Expose Flask app on port 5000
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
