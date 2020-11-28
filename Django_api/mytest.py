import requests
import json

URL = "http://127.0.0.1:8000/ep2/stu_create/"

data = {
    'name' : 'Sonam',
    'roll' : 101,
    'city' : 'LKO'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)