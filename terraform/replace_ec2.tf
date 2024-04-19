output "ec2_instance_ip" {
  value = aws_instance.your_instance.public_ip
  description = "The public IP address of the EC2 instance."
}

provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}

resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleInstance"
  }

  # Optionally include user_data to run scripts at launch
  # user_data = "${file("setup.sh")}"
}

variable "AWS_ACCESS_KEY_ID" {}
variable "AWS_SECRET_ACCESS_KEY" {}
