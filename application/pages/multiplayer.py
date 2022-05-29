from flask import Blueprint, render_template
from flask_login import current_user

from application.models import Teams

multiplayer = Blueprint("multiplayer", __name__)


@multiplayer.route("/multiplayer.html")
def multiplayers():
    """Renders Multiplayer page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("multiplayer.html", user_team=user_team)
