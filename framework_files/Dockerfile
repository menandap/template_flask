# Use an official Python runtime as the base image
FROM python:3.8-slim-buster
# Set the working directory for following COPY and CMD instructions
WORKDIR /framework_files
# Copy the requirements.txt file to the container
COPY requirements.txt .
# Install the required Python packages
RUN pip3 install -r requirements.txt
# Copy the entire content of the local app_files directory to the container
COPY app_files /framework_files/app_files
# Set the working directory to the app_files directory
WORKDIR /framework_files/app_files
# Run app.py when the container launches
CMD ["python3", "app.py"]
