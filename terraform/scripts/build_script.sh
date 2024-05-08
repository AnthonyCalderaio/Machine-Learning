####################################
### When EC2 instance is created

# python3 -m venv venv
# source venv/bin/activate

### Install pip
# sudo yum install python3-pip

### Install requirements
# pip3 install -r requirements.txt

####################################

### SSH into EC2
# ssh -i Security/AWS/EC2/04_23_2024_key/04_23_2024_key.pem ec2-user@54.167.120.254


# Create and activate environment
python3 -m venv venv &&
source venv/bin/activate &&

# Install pip
sudo yum install -y python3-pip &&

# Install requirements
pip3 install -r requirements.txt &&

# Serve
gunicorn -b 0.0.0.0:8080 run:app