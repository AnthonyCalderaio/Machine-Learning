# terraform import aws_key_pair.04_23_2024_key us-east-1

# Access Key
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}




# Create the EC2 instance and associate it with the new security group
resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"
  key_name      = "04_23_2024_key"
  security_groups = ["allow_ssh","allow_outbound", "allow_inbound", "flask-api-security-group"]

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