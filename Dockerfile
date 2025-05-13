# Use the official Python image from the Docker Hub
FROM python:3.12-alpine

# Set image name label
LABEL name="bot_polling"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the application
CMD ["python", "src/script.py"]
