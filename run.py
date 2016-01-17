from flask import *

app = Flask(__name__)

'''
this is how the data will be returned in get_data()

returned = {
    "samples": [
        {
            "id":1773,
            "channel":1,
            "d":25.25
        },
        {
            "id":1773,
            "channel":1,
            "d":25.25
        }
    ]
}
'''

def get_data():
	pass

def parse_data(raw_data):
    sensors = {}

    print raw_data

    data = raw_data["samples"]
    for point in data:
        if not point["channel"] in sensors:
            sensors[point["channel"]] = [point["d"]]
        else:
            sensors[point["channel"]].append(point["d"])

    for sensor in sensors:
        numPoints = len(sensor)
        total = 0
        for val in sensor:
            total = total + val
        average = total / numPoints
        sensors[sensor] = average

    tolerance = .05
    analyzed_data = {}
    for sensor in sensors:
        analyzed_data[sensor] = false #default to false, if sensor is at level with propane value will be set to true

    keys = sensors.keys()
    for i in range(len(keys)):
        if not i == 0:
            if sensors[sensor] - sensors[sensor] * tolerance < sensors[keys[i-1]] and sensors[keys[i-1]] < sensors[sensor] + sensors[sensor] * tolerance:
                analyzed_data[keys[i]] = true
            else:
                break;
        else:
            analyzed_data[keys[i]] = true

    num_true = 0
    for i in analyzed_data:
        if analyzed_data[i]:
            num_true = num_true + 1

    fill = num_true/len(sensors)
    fill = fill*4
    fill = int(fill)

    return fill

@app.route('/')
@app.route('/index/')
def index():
	#data = get_data()
	#_bars = parse_data(data)

    dic_pic = {
        '0': 'static/images/propaneEmpty.png',
        '1': 'static/images/propaneRed.png',
        '2': 'static/images/propaneOrange.png',
        '3': 'static/images/propaneYellow.png',
        '4': 'static/images/propaneGreen.png'
    }

    return render_template('index.html', image = dic_pic[str(1)])

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	#app.run(host='0.0.0.0')
	app.run()
