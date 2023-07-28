# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

# Copy the project files into the container
COPY . /app

RUN pip install -r requirements.txt

# Expose the port the application runs on
EXPOSE 8000

ENTRYPOINT cd /app && \
	python3 manage.py makemigrations && \
	python3 manage.py migrate && \
	python3 manage.py runserver 0.0.0.0:8000
# Run the Django development server
