import requests
import json

response = requests.get("https://randomuser.me/api/?inc=gender,name,location,email,dob,phone,cell")

print(json.dumps(response.json(), indent=4))
