from flask import render_template
from app import app
from app.models import Crimes, Cities, MLresult


@app.route('/')
def hello_world():
    return render_template('index.html')