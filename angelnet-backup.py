import os
import boto3
from datetime import datetime

# Initialize the S3 client with secure credentials
s3_client = boto3.client('s3')

# Define the bucket name and backup directory
BUCKET_NAME = 'angelnet-enterprise-backup'
BACKUP_DIR = '/path/to/enterprise/data'

def upload_file_to_s3(file_path, bucket_name, object_name):
    """
    Upload a file to an S3 bucket
    """
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Uploaded {file_path} to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")

def backup_enterprise_data(backup_dir, bucket_name):
    """
    Backup all files in the specified directory to the S3 bucket
    """
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    for root, _, files in os.walk(backup_dir):
        for file in files:
            file_path = os.path.join(root, file)
            s3_object_name = f"{timestamp}/{file}"
            upload_file_to_s3(file_path, bucket_name, s3_object_name)

if __name__ == "__main__":
    backup_enterprise_data(BACKUP_DIR, BUCKET_NAME)
