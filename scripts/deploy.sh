#!/bin/bash

echo "Starting deployment of Serverless Data Pipeline..."

# Create lambda_function.zip
echo "Step 1: Zipping Lambda function..."
zip lambda_function.zip lambda_function.py

# Navigate to terraform directory
echo "Step 2: Initializing Terraform..."
cd terraform
terraform init

echo "Step 3: Deploying infrastructure..."
terraform apply -auto-approve

echo "Deployment completed successfully!"
echo "S3 Bucket: $(terraform output bucket_name)"
echo "DynamoDB Table: $(terraform output dynamodb_table)"
