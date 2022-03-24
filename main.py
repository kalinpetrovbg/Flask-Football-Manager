import random

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from fm.stadium.stadium import Stadium
from fm.weather.weather import WEATHER_TYPES

teams = ["Juventus", "Arsenal", "Manchester", "Liverpool", "Bayern", "Milan", "Inter", "Barcelona", "Real Madrid",
         "Lecce", "Man City", "Newcastle", "Paris", "Monaco", "Schalke", "Verona", "Lecce", "Borusia",
         ]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/settings")
def settings():
    return "Settings Page"


@app.route("/create")
def create():
    return "Create a New Team"


@app.route("/cup")
def cup():
    return "Play in a Cup"


@app.route("/select-team.html")
def select_team():
    from fm.db.teams import Teams
    teams = Teams.query.all()
    return render_template("select-team.html", teams=teams)


@app.route("/existing.html")
def existing():
    return render_template("existing.html")


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


if __name__ == '__main__':
    app.run(debug=True)
