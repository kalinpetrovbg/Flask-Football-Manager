import random

from flask import render_template, request, flash, redirect, url_for
from sqlalchemy import func

from app import app
from app import db
from fm.db.players import Players
from fm.db.teams import Teams
from fm.stadium.stadium import Stadium
from fm.weather.weather import WEATHER_TYPES

teams = ["Juventus", "Arsenal", "Manchester", "Liverpool", "Bayern", "Milan", "Inter", "Barcelona", "Real Madrid",
         "Lecce", "Man City", "Newcastle", "Paris", "Monaco", "Schalke", "Verona", "Lecce", "Borusia",
         ]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/settings")
def settings():
    return "Settings Page"


@app.route("/create")
def create():
    return "Create a New Team"


@app.route("/cup.html")
def cup():
    return render_template("cup.html")


@app.route("/select-team.html")
def select_team():
    return render_template("select-team.html")


@app.route("/team/<team_id>.html")
def team(team_id):
    team = Teams.query.filter_by(id=team_id).first()
    return render_template("team.html", team=team)


@app.route("/existing.html")
def existing():
    all_teams = Teams.query.all()

    data = {}
    for team in all_teams:
        players = Players.query.filter_by(team_id=team.id).all()
        stats = {'name': team.name, 'logo': team.logo,
                 'league': team.league, 'id': team.id,
                 'ovr': team.overall, 'att': team.attack,
                 'mid': team.middle, 'def': team.defence,
                 'count': len(players),
                 }
        data[team] = stats
    return render_template("existing.html", data=data)


@app.route("/build-team.html", methods=['GET', 'POST'])
def build_team():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['league']:
            flash('Please enter all the fields.', 'error')
        else:
            team = Teams(name=request.form['name'], league=request.form['league'])
            db.session.add(team)
            db.session.commit()

            team_id = team.id
            return redirect(url_for('add_players', team_id=team_id))

    return render_template("build-team.html")


@app.route("/add-players/<team_id>.html", methods=['GET', 'POST'])
def add_players(team_id):
    team = Teams.query.filter_by(id=team_id).first()

    if request.method == 'POST':
        if not request.form['first_name'] or not request.form['last_name']:
            flash('Please enter all the fields.', 'error')
        else:
            player = Players(first_name=request.form['first_name'],
                             last_name=request.form['last_name'],
                             team_id=4,
                             attack=random.randint(50, 85),
                             middle=random.randint(50, 85),
                             defence=random.randint(50, 85),
                             )

            db.session.add(player)
            db.session.commit()

            # Todo
            attack = db.session.query(func.sum(Players.attack).filter_by(id=team_id)).first()
            middle = db.session.query(func.sum(Players.middle)).first()
            defence = db.session.query(func.sum(Players.defence)).first()
            overall = db.session.query(func.sum(Players.overall)).first()

            # db.session.merge(team)

            db.session.commit()
            flash('Your player has been created.')

            return render_template("/add-players.html", team_id=team_id, team=team)

    return render_template("add-players.html", team_id=team_id, team=team)

    # from fm.db.teams import Teams
    # from fm.db.players import Players
    #
    # def add_player(self):
    #     team = Teams.query.filter_by(id=self.team_id).first()
    #
    #     team.overall += self.overall
    #     team.attack += self.attack
    #     team.middle += self.middle
    #     team.defence += self.defence
    #
    # def remove_player(self):
    #     team = Teams.query.filter_by(id=self.team_id).first()
    #
    #     team.overall -= self.overall
    #     team.attack -= self.attack
    #     team.middle -= self.middle
    #     team.defence -= self.defence

    # p = Players(id=10, first_name="Kalin", last_name="Petrov", team_id=2, overall=20, attack=30, middle=10, defence=30)
    # p.remove_player()


@app.route("/choose-opponent.html")
def choose_opponent():
    return render_template("choose-opponent.html")


@app.route("/lineup.html")
def lineup():
    return render_template("lineup.html")


@app.route("/play.html")
def play():
    class Game:
        pass

        @staticmethod
        def start():
            content = "Game is starting..."
            return content

    class HomeTeam:
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def __str__(self):
            return f"Home team {self.name} with power {self.power}."

    class AwayTeam:
        def __init__(self, name, power):
            self.name = name
            self.power = power

        def __str__(self):
            return f"Away team {self.name} with power {self.power}."

    home_team = HomeTeam(random.choice(teams), 23)
    away_team = AwayTeam(random.choice(teams), 12)

    score = {home_team.name: 0, away_team.name: 0}
    scorers = {}

    time = 0

    weather = random.choice(WEATHER_TYPES)

    stadium = Stadium()
    stadium.generate_stadium()

    visitors = stadium.generate_visitors(weather=weather)
    welcome = stadium.print_message(weather=weather)

    while time <= 90:

        minute = random.randint(1, 15)
        time += minute

        if time >= 90:
            break

        goal = random.randint(0, 1)
        if goal == 0:
            continue

        random_side = random.choice([home_team.name, away_team.name])

        scorers[time] = random_side

        score[random_side] += goal

    return render_template("play.html", content=Game.start(), home=home_team, away=away_team, score=score,
                           scorers=scorers, stadium=stadium, visitors=visitors, welcome=welcome, weather=weather)


@app.route("/multiplayer.html")
def multiplayer():
    return render_template("multiplayer.html")


if __name__ == '__main__':
    app.run(debug=True)
