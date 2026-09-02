output "instance_public_ip" {
  description = "Public IP address of the deployed EC2 instance"
  value       = aws_instance.flask_server.public_ip
}

output "application_url" {
  description = "Direct URL to the Flask application"
  value       = "http://${aws_instance.flask_server.public_ip}:5000"
}

output "health_endpoint" {
  description = "Application health check URL"
  value       = "http://${aws_instance.flask_server.public_ip}:5000/health"
}

output "metrics_endpoint" {
  description = "Prometheus metrics URL"
  value       = "http://${aws_instance.flask_server.public_ip}:5000/metrics"
}
