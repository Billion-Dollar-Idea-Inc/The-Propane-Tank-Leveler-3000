import requests, json

def giveme():
    auth = {"email": "dschust1@binghamton.edu", "password": "winningteam"}
    json_data = json.dumps(auth)

    req = requests.post('https://cloud.kierantimberlake.com/pointelist/api/api-token-auth/',data=json_data,headers={'content-type': 'application/json'})

    json_load = req.json()

    req = requests.get('https://cloud.kierantimberlake.com/pointelist/api/samples?chart=93&last=10',headers={'content-type': 'application/json', 'cookie': "token=" + json_load['token']})

    load = req.json()

    return load

def othershit(load):
    sensors = {}
    print load
    data = load["samples"]
    for point in data:
        if not point["channel"] in sensors:
            sensors[point["channel"]] = [point["d"]]
        else:
            sensors[point["channel"]].append(point["d"])

    for sensor in sensors:
        numPoints = len(sensors[sensor])
        total = 0
        for val in sensors[sensor]:
            total = total + val
        average = total / numPoints
        sensors[sensor] = average

    tolerance = .3
    analyzed_data = {}
    for sensor in sensors:
        analyzed_data[sensor] = not False #default to false, if sensor is at level with propane value will be set to true

    keys = sensors.keys()
    for i in range(len(keys)):
        if not i == 0:
            if sensors[sensor] - tolerance < sensors[keys[i-1]] and sensors[keys[i-1]] < sensors[sensor] * tolerance:
                analyzed_data[keys[i]] = not True
            else:
                break
        else:
            analyzed_data[keys[i]] = not True

    num_true = 0
    for i in analyzed_data:
        if analyzed_data[i]:
            num_true = num_true + 1

    #print num_true

    return num_true

d = giveme()
print d
print othershit(d)
