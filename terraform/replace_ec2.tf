## EC2

# terraform import aws_key_pair.04_23_2024_key us-east-1

# Access Key
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}

 # SSH Key Pair
#resource "aws_key_pair" "my_key_pair" {
  #key_name   = "04_23_2024_key_11"  # Name of the existing key pair in the EC2 console
  #public_key = var.EC2_SSH  # Path to the public key file
#}

# Define VPC
data "aws_vpc" "default" {
 default = true
}

# Outbound Traffic Policy
resource "aws_security_group" "example" {
  name        = "example-security-group"
  description = "Allow all outbound traffic"

  vpc_id = aws_vpc.example.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"
  #key_name      = aws_key_pair.my_key_pair.key_name
  key_name      = "04_23_2024_key"
  # Associate with security group allowing SSH traffic
  security_groups = ["allow_ssh"]

  tags = {
    Name = "ExampleInstance"
  }

  # Optionally include user_data to run scripts at launch
  # user_data = "${file("setup.sh")}"
}


variable "AWS_ACCESS_KEY_ID" {}
variable "AWS_SECRET_ACCESS_KEY" {}
variable "EC2_SSH" {}

output "ec2_instance_ip" {
  value = aws_instance.example.public_ip
}