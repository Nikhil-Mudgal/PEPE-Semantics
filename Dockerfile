# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim-buster
#FROM gcr.io/deeplearning-platform-release/base-cpu

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
#COPY . ./
COPY pepe_semantics/ ./pepe_semantics
COPY main.py ./main.py
COPY requirements.txt ./requirements.txt

# Install production dependencies.
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app