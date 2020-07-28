import requests
r = requests.get('http://ec2-52-214-38-72.eu-west-1.compute.amazonaws.com/health.html')
print(r)