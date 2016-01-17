from flask import *

app = Flask(__name__)

def get_data():
	pass

def parse_data(data):
	pass

@app.route('/')
def index():
	data = get_data()
	_bars = parse_data(data)
	return render_template('index.html', bars=_bars)

if __name__ == '__main__':
	#app.run(host='0.0.0.0')
	app.run()
