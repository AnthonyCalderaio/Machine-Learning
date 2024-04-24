 # EC2
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}



#resource "aws_key_pair" "my_key_pair" {
  #key_name   = "04_23_2024_key"  # Name of the existing key pair in the EC2 console
  #public_key = var.PC_SSH  # Path to the public key file
#}


resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"
  #key_name      = aws_key_pair.my_key_pair.key_name
  key_name      = "04_23_2024_2_key" 
  # Associate with security group allowing SSH traffic
  # vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  security_groups = ["allow_ssh"]

  tags = {
    Name = "ExampleInstance"
  }

  # Optionally include user_data to run scripts at launch
  # user_data = "${file("setup.sh")}"
}


resource "aws_vpc" "example" {
  cidr_block = "10.0.0.0/16"

  enable_dns_hostnames = true
  enable_dns_support   = true
}

variable "AWS_ACCESS_KEY_ID" {}
variable "AWS_SECRET_ACCESS_KEY" {}
variable "PC_SSH" {}


output "ec2_instance_ip" {
  value = aws_instance.example.public_ip
}