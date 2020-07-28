import boto3


def create_instance(image_id, type):
    ec2 = boto3.resource('ec2', region_name= 'eu-west-2')
    ec2.create_instances(ImageId=image_id, InstanceType=type, MinCount=1, MaxCount=1)

create_instance('ami-04122be15033aa7ec', 't2.micro')