#!/bin/bash

# CD into project
cd ML_API

# Create and activate environment
python3 -m venv venv &&
source venv/bin/activate &&

# Install pip
sudo yum install -y python3-pip &&

# Install requirements
pip3 install -r requirements.txt &&

# Serve
gunicorn -b 0.0.0.0:8080 run:app