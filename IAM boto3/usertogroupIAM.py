#  Tee funktio, joka liittää parametrina annetun käyttäjän, toisena parametrina annettuun ryhmään.

import boto3



#adding user to group
def add_user_to_group(user_name, group):
    iam = boto3.client('iam')
    response = iam.add_user_to_group(UserName=user_name, GroupName=group)

    print(response)

    #  iam_resource = boto3.resource('iam') #resource representing IAM
    #  group = iam_resource.Group('group1') # Name of group
    #  response = group.add_user(
    #  UserName='user2_g1' #name of user

add_user_to_group('kati-boto3-user', 'kati-boto3-group')
