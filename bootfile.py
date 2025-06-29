# CHALLENGE: Create a new bucket + upload a file using Python

import boto3

s3 = boto3.client('s3', region_name='us-east-2')

bucket_name = 'addison-bucket-unique-name-12345'  # must be globally unique


# Upload file
s3.upload_file('secondfile.txt', bucket_name, 'secondfile.txt')

s3.upload_file('thirdfile.txt', bucket_name, 'thirdfile.txt')

print(f"✅ Uploaded 'secondfile.txt' and 'thirdfile.txt' to {bucket_name}")
