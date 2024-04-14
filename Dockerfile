# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./* /app
RUN apt-get update
RUN apt-get install -y python3 python3-pip
# Install any needed packages specified in requirements.txt (if you have one)
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python program
CMD ["python", "main.py"]
