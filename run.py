from flask import *
from test import Pls

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
    p = Pls()
    return p.giveme()

def parse_data(load):
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

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route('/<id>/', methods=['GET', 'POST'])
def tank(id):
    #check to make sure is valid tank but
    #we're gonna skip that for now
    valid = True
    if valid:
        dic_pic = {
            '0': '../static/images/propaneEmpty.png',
            '1': '../static/images/propaneRed.png',
            '2': '../static/images/propaneOrange.png',
            '3': '../static/images/propaneYellow.png',
            '4': '../static/images/propaneGreen.png'
        }
        data = get_data()
        return render_template('id.html', image = dic_pic[str(parse_data(data))])
        #return render_template('id.html', image = dic_pic[str(1)])

@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	#app.run(host='0.0.0.0')
	app.run()
