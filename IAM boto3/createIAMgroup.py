import boto3

iam = boto3.resource('iam')
group = iam.Group('kati-boto3-group')

response = iam.create_group(
    GroupName='kati-boto3-group')

print(response)