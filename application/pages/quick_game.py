import random
from collections import defaultdict

from flask import Blueprint, render_template, session, url_for, redirect, request
from flask_login import current_user

from application.misc.game import HomeTeam, AwayTeam
from application.misc.oponents import teams_data
from application.models import Teams
from application.stadium.stadium import Stadium
from application.weather.weather import Weather

quick_game = Blueprint("quick_game", __name__)


@quick_game.route("/quick-game.html")
def quick_games():
    """Renders Quick Game page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("quick-game.html", user_team=user_team)


@quick_game.route("/select-team.html")
def select_team():
    """Renders Select a Team page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("select-team.html", user_team=user_team)


@quick_game.route("/choose-opponent.html")
def choose_opponent():
    """Renders Choose Opponent page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("choose-opponent.html", user_team=user_team)


@quick_game.route("/lineup.html")
def lineup():
    """Renders Set Lineup page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()

    if session:
        opp_team = Teams.query.filter_by(id=session["opp_id"]).first()
    else:
        return render_template("lineup.html", user_team=user_team, opp_team=None)
    return render_template("lineup.html", user_team=user_team, opp_team=opp_team)


@quick_game.route("/play.html")
def play():
    """Renders Play page inside Quick Game menu."""

    user = current_user
    all_teams = len(Teams.query.all())

    matchday = defaultdict()

    matchday["weather"] = Weather.generate_weather()
    matchday["stadium"] = Stadium.generate_stadium()
    matchday["visitors"] = Stadium.generate_visitors(weather=matchday["weather"])
    matchday["message"] = Stadium.generate_message(weather=matchday["weather"])

    if user.team_id:
        user_team = Teams.query.filter_by(id=user.team_id).first()
    else:
        user_team = Teams.query.filter_by(id=random.randint(1, all_teams)).first()

    if session:
        opp_team = Teams.query.filter_by(id=session["opp_id"]).first()
    else:
        opp_team = Teams.query.filter_by(id=random.randint(1, all_teams)).first()

    game = defaultdict()

    game["home_team"] = HomeTeam(user_team.name, 23)
    game["away_team"] = AwayTeam(opp_team.name, 12)
    game["score"] = [0, 0]

    matchdata = defaultdict()

    time = 0
    while time <= 90:
        minute = random.randint(1, 15)
        time += minute

        if time >= 90:
            break

        goal = random.randint(0, 1)
        if goal == 0:
            continue

        team = random.choice(["Home", "Away"])
        event = random.choice(["Goal", "Miss"])

        if event == "Goal" and team == "Home":
            game["score"][0] += 1
            team = game["home_team"].name
        elif event == "Goal" and team == "Away":
            game["score"][1] += 1
            team = game["away_team"].name

        matchdata[time] = [team, event]

    return render_template(
        "play.html", game=game, matchdata=matchdata, matchday=matchday
    )


@quick_game.route("/opp-england.html", methods=["POST", "GET"])
def opp_england():
    """Renders English opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()

    # Todo add this to other opponent pages or remove it if not needed.
    if request.method == "POST":
        opp_id = request.form.get("team_id")
        session["opp_id"] = opp_id

        return redirect(url_for("lineup"))

    else:
        teams = Teams.query.filter_by(league="English Premier League").all()
        data = teams_data(teams)

        return render_template("opp-england.html", data=data, user_team=user_team)


@quick_game.route("/opp-spain.html")
def opp_spain():
    """Renders Spanish opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="Spain Primera Division").all()
    data = teams_data(teams)

    return render_template("opp-spain.html", data=data, user_team=user_team)


@quick_game.route("/opp-italy.html")
def opp_italy():
    """Renders Italian opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="Italian Serie A").all()
    data = teams_data(teams)

    return render_template("opp-italy.html", data=data, user_team=user_team)


@quick_game.route("/opp-germany.html")
def opp_germany():
    """Renders German opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="German Bundesliga").all()
    data = teams_data(teams)

    return render_template("opp-germany.html", data=data, user_team=user_team)


@quick_game.route("/opp-france.html")
def opp_france():
    """Renders French opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="French Ligue 1").all()
    data = teams_data(teams)

    return render_template("opp-france.html", data=data, user_team=user_team)


@quick_game.route("/opp-restofworld.html")
def opp_restofworld():
    """Renders Rest of World opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    # Todo league
    teams = Teams.query.filter_by(league="Rest of World").all()
    data = teams_data(teams)

    return render_template("opp-restofworld.html", data=data, user_team=user_team)
