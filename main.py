# """Main file rendering all website pages."""
#
# import logging
# import random
# from collections import defaultdict
#
# from flask import flash, redirect, render_template, request, session, url_for
# from flask_login import current_user, login_required, login_user, logout_user
# from sqlalchemy import func
# from werkzeug.security import check_password_hash, generate_password_hash
#
# # from app import app, db, login_manager
# from application.db.game import AwayTeam, HomeTeam
# from application.db.names import spanish_f_names, spanish_l_names
# from application.db import Players
# from application.db.teams import Teams
# from application.db.users import Users
# from application.misc.oponents import teams_data
# from application.stadium import Stadium
# from application.weather.weather import Weather

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('main.log')
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)


@login_manager.user_loader
def load_user(user_id):
    """Flask-login user loader."""
    # Todo - place it somewhere else

    return Users.query.get(int(user_id))





@app.route("/settings.html")
def settings():
    """Renders Settings page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("settings.html", user_team=user_team)


@app.route("/cup.html")
def cup():
    """Renders Play Cup page"""
    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("cup.html", user_team=user_team)


@app.route("/cup-champions.html")
def cup_champions():
    """Renders Champions Cup page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("cup-champions.html", user_team=user_team)


@app.route("/select-team.html")
def select_team():
    """Renders Select a Team page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("select-team.html", user_team=user_team)


@app.route("/team/<team_id>.html")
def team_page(team_id):
    """Renders a page for each team."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    team = Teams.query.filter_by(id=team_id).first()
    players = Players.query.filter_by(team_id=team.id).all()
    return render_template("team.html", team=team, players=players, user_team=user_team)


@app.route("/existing.html", methods=["POST", "GET"])
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


@app.route("/build-team.html", methods=["GET", "POST"])
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


@app.route("/add-players/<team_id>.html", methods=["GET", "POST"])
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
                    .filter(Players.team_id == team_id)
                    .scalar()
            )
            team.attack = round(total_attack)
            total_middle = (
                db.session.query(func.avg(Players.middle))
                    .filter(Players.team_id == team_id)
                    .scalar()
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


@app.route("/choose-opponent.html")
def choose_opponent():
    """Renders Choose Opponent page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("choose-opponent.html", user_team=user_team)


@app.route("/lineup.html")
def lineup():
    """Renders Set Lineup page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()

    if session:
        opp_team = Teams.query.filter_by(id=session["opp_id"]).first()
    else:
        return render_template("lineup.html", user_team=user_team, opp_team=None)
    return render_template("lineup.html", user_team=user_team, opp_team=opp_team)


@app.route("/play.html")
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


@app.route("/quick-game.html")
def quick_game():
    """Renders Quick Game page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("quick-game.html", user_team=user_team)


@app.route("/multiplayer.html")
def multiplayer():
    """Renders Multiplayer page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    return render_template("multiplayer.html", user_team=user_team)


@app.route("/opp-england.html", methods=["POST", "GET"])
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


@app.route("/opp-spain.html")
def opp_spain():
    """Renders Spanish opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="Spain Primera Division").all()
    data = teams_data(teams)

    return render_template("opp-spain.html", data=data, user_team=user_team)


@app.route("/opp-italy.html")
def opp_italy():
    """Renders Italian opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="Italian Serie A").all()
    data = teams_data(teams)

    return render_template("opp-italy.html", data=data, user_team=user_team)


@app.route("/opp-germany.html")
def opp_germany():
    """Renders German opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="German Bundesliga").all()
    data = teams_data(teams)

    return render_template("opp-germany.html", data=data, user_team=user_team)


@app.route("/opp-france.html")
def opp_france():
    """Renders French opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    teams = Teams.query.filter_by(league="French Ligue 1").all()
    data = teams_data(teams)

    return render_template("opp-france.html", data=data, user_team=user_team)


@app.route("/opp-restofworld.html")
def opp_restofworld():
    """Renders Rest of World opponents page."""

    user = current_user
    user_team = Teams.query.filter_by(id=user.team_id).first()
    # Todo league
    teams = Teams.query.filter_by(league="Rest of World").all()
    data = teams_data(teams)

    return render_template("opp-restofworld.html", data=data, user_team=user_team)


@app.route("/login.html", methods=["GET", "POST"])
def login():
    """Renders Login page."""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = Users.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return render_template("login.html")

        login_user(user, remember=remember)
        return redirect("/profile.html")  # Todo

    elif request.method == "GET":
        return render_template("login.html")


@app.route("/logout.html")
@login_required
def logout():
    """Renders Logout page."""

    logout_user()
    return redirect("/")


@app.route("/signup.html", methods=["GET", "POST"])
def signup():
    """Renders Signup page."""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        existing_user = Users.query.filter_by(username=username).first()

        if existing_user:
            flash("There is already an user with this username.")
            return redirect("/signup.html")

        user = Users(
            username=username,
            password=generate_password_hash(password, method="sha256"),
        )

        db.session.add(user)
        db.session.commit()

        return render_template("index.html")
    else:
        return render_template("signup.html")


@app.route("/profile.html")
def profile():
    """Renders Profile page."""

    user = current_user
    if not current_user.is_authenticated:
        return redirect(url_for("nologin"))

    user_team = Teams.query.filter_by(id=user.team_id).first()

    try:
        opp_team = Teams.query.filter_by(id=session["opp_id"]).first()
    except KeyError:
        return render_template(
            "profile.html", user=user, user_team=user_team, opp_team=None
        )

    return render_template(
        "profile.html", user=user, user_team=user_team, opp_team=opp_team
    )


@app.route("/no-login.html")
def nologin():
    """Error page for unauthorized users."""

    return render_template("no-login.html")


if __name__ == "__main__":
    app.run(debug=True)
