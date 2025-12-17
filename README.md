# 🚀 Serverless Data Processing Pipeline

## Architecture Overview
Designed a cloud-native, event-driven pipeline that automatically processes files uploaded to S3. Solution handles metadata extraction and storage without server management.

**Architecture**: S3 → Lambda → DynamoDB

## My Role: Solution Architect
- Designed system architecture and technical specifications
- Selected AWS services and integration patterns
- Established security controls and IAM policies
- Created infrastructure-as-code templates
- Defined operational procedures and monitoring

## Key Features
- **Serverless**: Zero infrastructure management
- **Event-Driven**: Automatic processing on file upload
- **Auto-Scaling**: Handles 1 to 10,000+ files
- **Cost-Optimized**: Pay-per-use pricing

## Quick Deployment
```bash
./deploy.sh
aws s3 cp test.txt s3://$(terraform output -raw bucket_name)/

🔗 Full Documentation & Demo
📚 Complete Project Documentation:[[Notion Page Link]](https://www.notion.so/Serverless-Data-Processing-Pipeline-2aeafa903f8a80cbbc7dc601c372eca9?source=copy_link)

🎥 Video Demonstration: [[Video Demo Link]](https://youtu.be/e5USaMiPLaQ)

💻 Source Code: [[GitHub Repository Link]](https://github.com/DOTWEB2020/Serverless-Data-Pipeline-with-AWS-Services)
