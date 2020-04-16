from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fpgdtkivkpmedt:cd7f60ed50a88ef2bb2caf1a7e24f00ce37959decf2dddbb90ab1654df9d3816@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/dlfqf6ig6k8vb'

db = SQLAlchemy(app)

from models import User

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/add/')
def webhook():
    name = "ram"
    email = "ram@ram.com"
    u = User(id = id, nickname = name, email = email)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"

'''
@app.route('/delete/')
def delete():
    u = User.query.get(i)
    db.session.delete(u)
    db.session.commit()
    return "user deleted"
'''

if __name__ == '__main__':
    app.run()