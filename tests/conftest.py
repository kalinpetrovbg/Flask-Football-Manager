import pytest

from app import app
from app import db
from db.players import Players
from db.teams import Teams
from db.users import Users
from weather.weather import weathers


@pytest.fixture(params=weathers)
def weather_type(request):
    """Params type of fixure with all wather types."""
    current_weather = request.param

    return current_weather


@pytest.fixture(scope="session")
def flask_app():
    """Main flask app fixture."""
    test_app = app
    client = test_app.test_client()

    yield client


@pytest.fixture()
def app_with_team():
    """Fixture for adding a Team to the database."""

    team = Teams(id=1000,
                 name="Manchester United",
                 logo="man",
                 league="English Premier League"
                 )
    db.session.add(team)
    db.session.commit()

    yield team

    db.session.delete(team)
    db.session.commit()


@pytest.fixture()
def app_with_two_teams():
    """Fixture for adding two Teams to the database."""

    team1 = Teams(id=1000,
                  name="Manchester United",
                  logo="man",
                  league="English Premier League",
                  overall=50,
                  attack=60,
                  middle=50,
                  defence=40
                  )
    team2 = Teams(id=1001,
                  name="Arsenal",
                  logo="ars",
                  league="English Premier League",
                  overall=100,
                  attack=120,
                  middle=100,
                  defence=80
                  )

    db.session.add(team1)
    db.session.add(team2)
    db.session.commit()

    yield team1, team2

    db.session.delete(team1)
    db.session.delete(team2)
    db.session.commit()


@pytest.fixture()
def app_with_player():
    """Fixture for adding Players to the database."""

    player = Players(first_name="Cristiano",
                     last_name="Ronaldo",
                     team_id=1000, position="ATT",
                     overall=50, attack=91,
                     middle=36, defence=22)

    db.session.add(player)
    db.session.commit()

    yield player

    db.session.delete(player)
    db.session.commit()


@pytest.fixture()
def app_with_user():
    """Instert a user data in the database."""

    user = Users()
    user.username = "kalin_petrov"
    user.password = "0Ury@gaj82"
    user.team_id = 1000

    db.session.add(user)
    db.session.commit()

    yield user

    db.session.delete(user)
    db.session.commit()
