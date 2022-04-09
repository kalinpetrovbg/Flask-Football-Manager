from app import db, login_manager
from flask_login import UserMixin, AnonymousUserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    team_id = db.Column(db.Integer, default=None)


class AnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.team_id = None

login_manager.anonymous_user = AnonymousUser



# db.create_all()
