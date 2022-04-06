import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")
response_text = json.loads(response.text)

print('\nThe ISS current location:')
for i in response_text['iss_position']:
    print('\t' + i + ': ' + response_text['iss_position'][i])

response = requests.get('http://api.open-notify.org/astros.json')
response_text = json.loads(response.text)
print('\nCurrent astronauts on the ISS:')
for i in response_text['people']:
    print('\t' + i['name'])
