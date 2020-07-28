import boto3
import json

# Create IAM client
iam = boto3.client('iam')
policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"AWS": "arn:aws:s3:::kati-bucket"},
            "Action": "s3:*"
        }
    ]
})
# Create role
response = iam.create_role(RoleName='kati-boto3-role', AssumeRolePolicyDocument=policy)