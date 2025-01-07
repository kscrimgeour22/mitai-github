# Use a lightweight version of Python
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your application code to the container
COPY . .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app runs on
EXPOSE 8080

# Command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
