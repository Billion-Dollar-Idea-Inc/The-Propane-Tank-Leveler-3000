import requests, json

#prepare dictionary
auth = {"email": "myemail@email.com", "password": "mypassword"}

#convert dictionary to json
json_data = json.dumps(auth)

#make post request for authorization
#if successful, req will be authorization token
req = requests.post('https://cloud.kierantimberlake.com/pointelist/api/api-token-auth/',
        data=json_data,
        headers={'content-type': 'application/json'})

#convert from json to dictionary
json_load = req.json()

#make request for data
#this specific request would take the last ten results from chart 93
req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/samples?chart=93&last=10',
        headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

#convert from json
load = req.json()
