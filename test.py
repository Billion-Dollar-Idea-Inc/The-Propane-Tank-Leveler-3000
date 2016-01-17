import requests, json



auth = {"email": "dschust1@binghamton.edu", "password": "winningteam"}
json_data = json.dumps(auth)
print json_data

req = requests.post('https://cloud.kierantimberlake.com/pointelist/api/api-token-auth/',
    data=json_data,
    headers={'content-type': 'application/json'})

print req

json_load = req.json()
print json_load
print json_load['token']

req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/samples?chart=93&last=10',
    headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

print req.text
