import boto3
import logging
from botocore.exceptions import ClientError

s3 = boto3.resource("s3")

def remove_bucket(bucket_name):

    try:
        bucket = s3.Bucket(bucket_name)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
    except ClientError as e:
        logging.error(e)
        return False
    return True

print(remove_bucket('kati-boto3-bucket'))
