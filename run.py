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

def parse_data(data):
	return 0 #returns number of bars to be displayed, ie 0, 1, 2, 3, or 4

@app.route('/')
def index():
	data = get_data()
	_bars = parse_data(data)
	return render_template('index.html', bars=_bars)

if __name__ == '__main__':
	#app.run(host='0.0.0.0')
	app.run()
