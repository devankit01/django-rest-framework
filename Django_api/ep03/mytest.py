import requests
import json

URL = 'http://127.0.0.1:8000/ep3/stu_api/'

def get_data(id = None):
    data = {}

    if id is not None:
        data = {'id' : id}
        
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

# During test remove comment
# get_data()

def post_data():
    data = {'name':'ravi',
    'roll':103,
    'city':'Kolkata'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)

# During test remove comment
# post_data()

def update_data():
    data = {
    'id' : 3,
    'city':'Delhi',
    'name':'Ankit',
    'roll':107
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)

# During test remove comment
# update_data()

def delete_data():
    data = {
    'id' : 1
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)

delete_data()