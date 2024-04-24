 # EC2
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}

resource "aws_instance" "example" {
  ami           = "ami-04e5276ebb8451442"
  instance_type = "t2.micro"

  # Allow SSH Traffic
  ingress {
    description = "SSH"
    from_port   = 0
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "ExampleInstance"
  }

  # Optionally include user_data to run scripts at launch
  # user_data = "${file("setup.sh")}"

  
}





variable "AWS_ACCESS_KEY_ID" {}
variable "AWS_SECRET_ACCESS_KEY" {}


output "ec2_instance_ip" {
  value = aws_instance.example.public_ip
}