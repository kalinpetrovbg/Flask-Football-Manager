from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "A05sj32fd@09234/;#d492"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)



