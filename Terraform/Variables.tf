# variables.tf
variable "aws_region" {
  description = "AWS region where resources will be deployed"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name of the project for resource naming"
  type        = string
  default     = "serverless-pipeline"
}

variable "environment" {
  description = "Deployment environment (dev, staging, prod)"
  type        = string
  default     = "demo"
}

variable "lambda_runtime" {
  description = "Python runtime for Lambda function"
  type        = string
  default     = "python3.9"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table for processed data"
  type        = string
  default     = "ProcessedData"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "DataProcessor"
}
