"""Data models."""
from flask_login import UserMixin

from . import db


class Users(db.Model, UserMixin):
    """Default users database model."""

    __tablename__ = "fm_users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    team_id = db.Column(db.Integer, default=None)

    def __repr__(self):
        return f"User {self.username}"


class Teams(db.Model):
    """Build teams datatable model."""

    __tablename__ = "fm_teams"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    logo = db.Column(db.Text, default="no-logo")
    league = db.Column(db.String, nullable=False)
    overall = db.Column(db.Integer, default=0)
    attack = db.Column(db.Integer, default=0)
    middle = db.Column(db.Integer, default=0)
    defence = db.Column(db.Integer, default=0)

    def __repr__(self):
        return str(self.name)


class Players(db.Model):
    """Build all players' data model."""

    __tablename__ = "fm_players"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey(Teams.id), nullable=True)
    position = db.Column(db.String, default="NA")
    overall = db.Column(db.Integer, default=0)
    attack = db.Column(db.Integer, default=0)
    middle = db.Column(db.Integer, default=0)
    defence = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.first_name



# class AnonymousUser(AnonymousUserMixin):
#     """For non logged users."""
#
#     def __init__(self):
#         self.username = "Anonymous"
#         self.team_id = None

# login_manager.anonymous_user = AnonymousUser
