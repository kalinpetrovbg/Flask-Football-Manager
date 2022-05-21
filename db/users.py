"""Generate users database table."""
from flask_login import AnonymousUserMixin, UserMixin

from app import db, login_manager


class Users(db.Model, UserMixin):
    """Default users database model."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    team_id = db.Column(db.Integer, default=None)


class AnonymousUser(AnonymousUserMixin):
    """For non logged users."""

    def __init__(self):
        self.team_id = None


login_manager.anonymous_user = AnonymousUser

db.create_all()
