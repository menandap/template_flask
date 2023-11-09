# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory for following COPY and CMD instructions
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt requirements.txt

# Install the required Python packages
RUN pip3 install -r requirements.txt

# Copy the entire content of the local flask_file directory to the container
COPY framework_files/ .

# Set the working directory to the flask_file directory
WORKDIR /app/framework_files

# Run app.py when the container launches
CMD ["python3", "app.py"]