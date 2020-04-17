from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
app.config['DATABASE_URL'] = "postgres://fpgdtkivkpmedt:cd7f60ed50a88ef2bb2caf1a7e24f00ce37959decf2dddbb90ab1654df9d3816@ec2-54-247-78-30.eu-west-1.compute.amazonaws.com:5432/dlfqf6ig6k8vb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Crimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username      

class MLresult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#db.drop_all()
db.create_all()
db.session.add(User(username="Fast", email="examples@example.com"))
db.session.commit()


@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()