import boto3

def iam_role_to_EC2(instance_id, arn, name):
    client = boto3.client('ec2', region_name='eu-west-2')
    response = client.associate_iam_instance_profile(
        IamInstanceProfile={
            'Arn': arn,
            'Name': name
        },
        InstanceId=instance_id
    )

iam_role_to_EC2('i-01d9aa604bb09416a', 'arn:aws:iam::821383200340:instance-profile/Kati-EC2-S3-full-access', 'Kati-EC2-S3-full-access')