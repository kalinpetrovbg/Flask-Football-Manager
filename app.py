from flask_sqlalchemy import SQLAlchemy

from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "secret"

db = SQLAlchemy(app)