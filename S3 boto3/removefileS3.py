import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.resource("s3")

def remove_file(bucket, file_name):
    try:
        obj = s3.Object(bucket, file_name)
        obj.delete()
    except ClientError as e:
        logging.error(e)
        return False
    return True

print(remove_file('kati-boto3-bucket', 'puppy.jpg'))






