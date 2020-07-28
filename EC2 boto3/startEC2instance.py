import boto3
from botocore.exceptions import ClientError

def start_instance(*args):
    ec2 = boto3.client('ec2', region_name='eu-west-2')
    lista = list(args)

    # Do a dryrun first to verify permissions
    try:
        ec2.start_instances(InstanceIds=args, DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=args, DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

start_instance('i-00afec9fc9f809b03')
