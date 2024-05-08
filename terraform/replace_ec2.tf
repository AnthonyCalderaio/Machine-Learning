# terraform import aws_key_pair.04_23_2024_key us-east-1

# Access Key
provider "aws" {
  region     = "us-east-1"
  access_key = var.AWS_ACCESS_KEY_ID
  secret_key = var.AWS_SECRET_ACCESS_KEY
}


 resource "aws_security_group" "Flask_Inbound" {
   name        = "Flask_Inbound"
   description = "Allow inbound traffic on port 5000"

  ingress {
    from_port   = 8080
    to_port     = 8080
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
  security_groups = ["allow_ssh","allow_outbound", "flask-api-security-group", "allow-outbound-1", "aws_security_group.Flask_Inbound.name"]

  tags = {
    Name = "AIBrary"
  }


  # Associate the Elastic IP with the instance
  #associate_public_ip_address = false # Ensure this is set to false
  #eip                          = aws_eip.example.id # 

  # Optionally include user_data to run scripts at launch
  # user_data = "${file("setup.sh")}"
}

# Allocate Elastic IP: 18.213.211.119
# resource "aws_eip" "ML_IP" {
  # vpc = true # Specify if you are using a VPC or not
  # instance = aws_instance.example.id
# }

data "aws_eip" "ML_IP" {
  # Configuration to fetch the Elastic IP information
  filter {
    name   = "tag:Name"
    values = ["ML_IP"]
  }
}

resource "aws_eip_association" "ML_IP" {
  instance_id   = aws_instance.example.id
  allocation_id = data.aws_eip.ML_IP.id
}

variable "AWS_ACCESS_KEY_ID" {}
variable "AWS_SECRET_ACCESS_KEY" {}
variable "EC2_SSH" {}

#output "ec2_instance_ip" {
  #value = aws_instance.example.public_ip
#}

output "ec2_instance_ip" {
  value = data.aws_eip.ML_IP.public_ip
}
