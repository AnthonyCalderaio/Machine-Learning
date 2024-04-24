 # EC2
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}

resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"

  # Associate with security group allowing SSH traffic
  # vpc_security_group_ids = [aws_security_group.allow_ssh.id]
  security_groups = ["allow_ssh"]

  tags = {
    Name = "ExampleInstance"
  }

  # Optionally include user_data to run scripts at launch
  # user_data = "${file("setup.sh")}"
}


resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH and SCP traffic"

  # Allow SSH (port 22) traffic
  #ingress {
    #description = "SSH"
    #from_port   = 22
    #to_port     = 22
    #protocol    = "tcp"
    #cidr_blocks = ["0.0.0.0/0"]
  #}

  # Allow SCP (port 22) traffic
  #ingress {
    #description = "SCP"
    #from_port   = 22
    #to_port     = 22
   #protocol    = "tcp"
  # cidr_blocks = ["0.0.0.0/0"]
 # }
#}




variable "AWS_ACCESS_KEY_ID" {}
variable "AWS_SECRET_ACCESS_KEY" {}


output "ec2_instance_ip" {
  value = aws_instance.example.public_ip
}