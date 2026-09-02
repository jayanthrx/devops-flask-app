variable "aws_region" {
  description = "The AWS region to deploy resources into"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "app_name" {
  description = "Application name for resource tagging"
  type        = string
  default     = "devops-flask-app"
}

variable "docker_image" {
  description = "Docker image to deploy on EC2"
  type        = string
  default     = "jayanthrx/devops-flask-app:latest"
}

variable "key_name" {
  description = "Name of an existing AWS KeyPair to enable SSH access"
  type        = string
  default     = ""
}
