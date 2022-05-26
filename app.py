# """Build general Flask settings."""
#
# from flask import Flask
# from flask_login import LoginManager
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# db = SQLAlchemy(app)
#
# login_manager = LoginManager()
# login_manager.init_app(app)
