#  Hae JSON-dataa osoitteesta https://api.github.com/search/repositories?q=language:python
from pprint import pprint
import requests

r = requests.get('https://api.github.com/search/repositories?q=language:python')
data = r.json()

#  print(data)
#  print(data['items'][0]['forks'])

#  Tulosta data rivi kerrallaan, seuraavassa muodossa:{forks}. {name}: {description}

for items in data['items']:
    pprint(f"{items['forks']}.{items['name']}: {items['description']}")

# pprint(data['items'][0]['forks'])


for d in sorted(data['items'], key=lambda x: x['forks'], reverse=True):
    pprint(f"{items['forks']}.{items['name']}: {items['description']}")