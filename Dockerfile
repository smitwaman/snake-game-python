# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./* /app
RUN apt install python3 -y

# Install any needed packages specified in requirements.txt (if you have one)
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python program
CMD ["python3", "main.py"]
