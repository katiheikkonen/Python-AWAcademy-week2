import boto3

s3 = boto3.client('s3')
s3.download_file('kati-boto3-bucket', 'puppy.jpg', 'puppy2.jpg')
