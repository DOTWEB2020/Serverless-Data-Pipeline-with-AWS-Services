# lambda_function.py
import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get bucket and file details from S3 event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        print(f"Processing file: {file_key} from bucket: {bucket_name}")
        
        # Get the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        
        # Process the data (example: count lines and words)
        lines = file_content.split('\n')
        word_count = sum(len(line.split()) for line in lines if line.strip())
        
        # Prepare data for DynamoDB
        table_name = 'ProcessedData'
        table = dynamodb.Table(table_name)
        file_id = str(uuid.uuid4())
        
        item = {
            'file_id': file_id,
            'file_name': file_key,
            'processed_at': datetime.utcnow().isoformat(),
            'line_count': len(lines),
            'word_count': word_count,
            'file_size': response['ContentLength'],
            'status': 'PROCESSED'
        }
        
        # Store in DynamoDB
        table.put_item(Item=item)
        
        print(f"Successfully processed and stored data for file: {file_key}")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'File processed successfully',
                'file_id': file_id,
                'file_name': file_key
            })
        }
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
