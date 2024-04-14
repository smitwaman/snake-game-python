# Use tiangolo/uwsgi-nginx-flask:python3.10 as base image
FROM tiangolo/uwsgi-nginx-flask:python3.10

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# Install project dependencies
# RUN pip install --no-cache-dir -r /app/requirements.txt  # Uncomment this line if you have a requirements.txt file

# Command to run the Python program
CMD ["python", "main.py"]
