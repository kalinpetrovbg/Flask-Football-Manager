from flask import Blueprint, render_template
from flask_login import current_user

from application.models import Teams

play_cup = Blueprint("play_cup", __name__)


@play_cup.route("/cup.html")
def cup():
    """Renders Play Cup page"""
    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("cup.html", user_team=user_team)


@play_cup.route("/cup-champions.html")
def cup_champions():
    """Renders Champions Cup page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("cup-champions.html", user_team=user_team)
