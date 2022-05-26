from flask import Blueprint
from flask import current_app as app
from .models import db, Users, Teams, Players

# Blueprint Configuration
app_bp = Blueprint(
    "app_bp", __name__,
)


@app_bp.route("/", methods=['GET'])
def index():
    """Homepage."""

    user = Users()
    user.username = "Kalin"
    user.password = "ooo"

    team = Teams(name="Manchester United", league="English Premier League", logo="man")
    player = Players(first_name="David", last_name="De Gea", team_id=1, position="GK",
                    overall=31, attack=4, middle=3, defence=87)

    db.session.add(user)
    db.session.add(team)
    db.session.add(player)

    db.session.commit()



    return "Hello 2"




#     user = current_user
#     user_team = Teams.query.filter_by(id=user.team_id).first()
#     return render_template("index.html", user_team=user_team)
