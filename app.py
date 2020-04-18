from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
#app.config['DATABASE_URL'] = "postgres://togcikqgjukane:38eb8b72b77222f835c9854ad7074a96736cc6f26aa68b8360405549e3aeb0f6@ec2-54-75-244-161.eu-west-1.compute.amazonaws.com:5432/de6j0v0fhdad84"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Crimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    severity = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.Integer, unique=False, nullable=False)
	date = db.Column(db.String(120), unique=False, nullable=False)
	time = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Integer version of string names 
    postnr = db.Column(db.Integer, unique=False, nullable=False)
    kommune = db.Column(db.Integer, unique=False, nullable=False)

    # Coordinates
    latitude = db.Column(db.Float, unique=False, nullable=False)
    longitude = db.Column(db.Float, unique=False, nullable=False)
    
    

    def __repr__(self):
        return '<User %r>' % self.username      

class MLresult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return '<User %r>' % self.id

#db.drop_all()
#db.create_all()
db.session.add(Crimes(username="Nibba", email="examples@example.com"))
db.session.commit()
#print(Crimes.query.all())

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()