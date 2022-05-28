from flask import Blueprint, render_template
from flask_login import current_user

from .models import db, Users, Teams, Players

# Blueprint Configuration
app_bp = Blueprint(
    "app_bp", __name__,
)


@app_bp.route("/", methods=['GET'])
def index():
    """Homepage."""

    user = current_user
    # user_team = Teams.query.filter_by(id=user.team_id).first()

    # return render_template("index.html", user_team=user_team)
    return f"Hello {user}"
