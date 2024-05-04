# terraform import aws_key_pair.04_23_2024_key us-east-1

# Access Key
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}


resource "aws_security_group" "example_sg" {
  name        = "example-security-group"
  description = "Allow inbound traffic on port 5000"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow traffic from all IP addresses. Adjust as needed.
  }

  // Add more ingress rules as necessary
}


# Create the EC2 instance and associate it with the new security group
resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"
  key_name      = "04_23_2024_key"
  security_groups = ["allow_ssh","allow_outbound", "flask-api-security-group", "aws_security_group.example_sg.name"]

  tags = {
    Name = "AIBrary"
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