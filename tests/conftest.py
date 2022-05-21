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
def app_with_teams():
    """Fixture for adding Teams to the database."""

    team = Teams(name="Manchester United", league="English Premier League", logo="man")
    db.session.add(team)
    db.session.commit()

    yield team

    db.session.delete(team)
    db.session.commit()


@pytest.fixture()
def app_with_players():
    """Fixture for adding Players to the database."""

    player = Players(first_name="Cristiano",
                     last_name="Ronaldo",
                     team_id=1, position="ATT",
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
    user.team_id = 1

    db.session.add(user)
    db.session.commit()

    yield user

    db.session.delete(user)
    db.session.commit()
