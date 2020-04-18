from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# SQLite for development
# PostgreSQL for production

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
#app.config['DATABASE_URL'] = "postgres://togcikqgjukane:38eb8b72b77222f835c9854ad7074a96736cc6f26aa68b8360405549e3aeb0f6@ec2-54-75-244-161.eu-west-1.compute.amazonaws.com:5432/de6j0v0fhdad84"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'b44d6ac664507abd8fa897caf1080041'

db = SQLAlchemy(app)

from app import routes