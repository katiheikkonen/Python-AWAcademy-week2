import boto3
import json

iam = boto3.resource('iam')
policy = iam.Policy('arn')

def create_policy(resource):
    # Create a policy
    kati_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": f"{resource}:*"
            }]
        }
    response = iam.create_policy(
      PolicyName='kati-boto3-policy',
      PolicyDocument=json.dumps(kati_policy)
    )
    print(response)

create_policy('arn:aws:s3:::kati-bucket')
