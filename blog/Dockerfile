# start with linux kernal
FROM python:3.11-slim-bullseye

#linux : python
ENV PYTHONUNBUFFERED=1

# update & install
RUN apt-get update && apt-get -y install gcc libpq-dev

# create folder : docker
WORKDIR /app

# copy requirements 
COPY requirements.txt /pp/requirements.txt

# install req
RUN pip install -r /pp/requirements.txt

# copy all project files
COPY . /app/
  
