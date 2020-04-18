from flask import render_template, json
from app import app
from app.models import Crimes, Cities, MLresult


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/<name>')
def api_get_name(name):
	return json.jsonify({
		'name': name
		})