import random

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user
from sqlalchemy import func

from application import db, login_manager
from application.misc.names import spanish_l_names, spanish_f_names
from application.misc.oponents import teams_data
from application.models import Teams, Players, Users

main = Blueprint("main", __name__)

@login_manager.user_loader
def load_user(user_id):
    """Get user function."""
    return Users.get(user_id)

@main.route("/", methods=['GET'])
def index():
    """Homepage."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()

    return render_template("index.html", user_team=user_team)


@main.route("/settings.html")
def settings():
    """Renders Settings page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("settings.html", user_team=user_team)


@main.route("/team/<team_id>.html")
def team_page(team_id):
    """Renders a page for each team."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    team = Teams.query.filter_by(id=team_id).first()
    players = Players.query.filter_by(team_id=team.id).all()
    return render_template("team.html", team=team, players=players, user_team=user_team)


@main.route("/existing.html", methods=["POST", "GET"])
def existing_teams():
    """Renders Select your team page."""

    user = current_user

    if request.method == "POST":
        user_team = request.form.get("team_id")
        user.team_id = user_team
        db.session.commit()

        return redirect(url_for("profile"))

    else:
        user_team = Teams.query.filter_by(id=user.team_id).first()
        teams = Teams.query.all()
        data = teams_data(teams)

        return render_template("existing.html", data=data, user_team=user_team)


@main.route("/build-team.html", methods=["GET", "POST"])
def build_team():
    """Renders build your team page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    if request.method == "POST":
        if not request.form["name"] or not request.form["league"]:
            flash("Please enter all the fields.", "error")
        else:
            team = Teams(name=request.form["name"], league=request.form["league"])
            db.session.add(team)
            db.session.commit()

            team_id = team.id
            user.team_id = team.id
            db.session.commit()

            return redirect(url_for("add_players", team_id=team_id))

    return render_template("build-team.html", user_team=user_team)


@main.route("/add-players/<team_id>.html", methods=["GET", "POST"])
def add_players(team_id):
    """Renders the page for adding new players to a team."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()

    if request.method == "POST":
        team = Teams.query.filter_by(id=team_id).first()
        players = Players.query.filter_by(team_id=team.id).all()
        player = ""
        position = request.form["position"]

        if not position:
            flash("Please enter all the fields.", "error")

        else:
            if position == "GK":
                player = Players(
                    first_name=random.choice(spanish_f_names),
                    last_name=random.choice(spanish_l_names),
                    position="GK",
                    team_id=team_id,
                    attack=random.randint(1, 5),
                    middle=random.randint(1, 10),
                    defence=random.randint(60, 85),
                )
            elif position == "DEF":
                player = Players(
                    first_name=random.choice(spanish_f_names),
                    last_name=random.choice(spanish_l_names),
                    position="DEF",
                    team_id=team_id,
                    attack=random.randint(10, 30),
                    middle=random.randint(20, 40),
                    defence=random.randint(60, 85),
                )

            elif position == "MID":
                player = Players(
                    first_name=random.choice(spanish_f_names),
                    last_name=random.choice(spanish_l_names),
                    position="MID",
                    team_id=team_id,
                    attack=random.randint(15, 35),
                    middle=random.randint(60, 85),
                    defence=random.randint(15, 35),
                )

            elif position == "ATT":
                player = Players(
                    first_name=random.choice(spanish_f_names),
                    last_name=random.choice(spanish_l_names),
                    position="ATT",
                    team_id=team_id,
                    attack=random.randint(60, 85),
                    middle=random.randint(20, 40),
                    defence=random.randint(10, 30),
                )

            player.overall = round((player.attack + player.middle + player.defence) / 3)

            db.session.add(player)
            db.session.commit()

            total_attack = (
                db.session.query(func.avg(Players.attack))
                    .filter(Players.team_id == team_id).scalar()
            )
            team.attack = round(total_attack)
            total_middle = (
                db.session.query(func.avg(Players.middle))
                    .filter(Players.team_id == team_id).scalar()
            )
            team.middle = round(total_middle)
            total_defence = (
                db.session.query(func.avg(Players.defence))
                    .filter(Players.team_id == team_id)
                    .scalar()
            )
            team.defence = round(total_defence)

            team_overall = round((team.attack + team.middle + team.defence) / 3)
            team.overall = team_overall

            db.session.merge(team)
            db.session.commit()

            flash("Your player has been created.")
            players.append(player)

            return render_template(
                "add-players.html",
                team_id=team_id,
                team=team,
                players=players,
                user_team=user_team,
            )
    else:
        team = Teams.query.filter_by(id=team_id).first()
        players = Players.query.filter_by(team_id=team.id).all()

        return render_template(
            "add-players.html",
            team_id=team_id,
            team=team,
            players=players,
            user_team=user_team,
        )
