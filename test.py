import requests, json

class Pls():
    def giveme(self):
        auth = {"email": "dschust1@binghamton.edu", "password": "winningteam"}
        json_data = json.dumps(auth)

        req = requests.post('https://cloud.kierantimberlake.com/pointelist/api/api-token-auth/',data=json_data,headers={'content-type': 'application/json'})

        json_load = req.json()

        req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/samples?chart=93&last=10',headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

        load = req.json()

        return load
