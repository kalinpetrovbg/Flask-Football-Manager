import pytest

from application import create_app, db
from application.models import Players
from application.models import Teams
from application.models import Users
from application.weather.weather import weathers


@pytest.fixture()
def app():
    """Main flask app fixture."""
    app = create_app()
    app.config.update({"TESTING": True})

    with app.app_context():
        yield app


@pytest.fixture()
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture()
def app_with_team(app, client):
    """Fixture for adding a Team to the database."""

    team = Teams(id=1000,
                 name="Manchester United 2",
                 logo="man",
                 league="English Premier League"
                 )
    db.session.add(team)
    db.session.commit()

    yield team

    db.session.delete(team)
    db.session.commit()


@pytest.fixture()
def app_with_two_teams(app):
    """Fixture for adding two Teams to the database."""

    team1 = Teams(id=1000,
                  name="Manchester United 2",
                  logo="man",
                  league="English Premier League",
                  overall=50,
                  attack=60,
                  middle=50,
                  defence=40
                  )
    team2 = Teams(id=1001,
                  name="Arsenal 2",
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
def app_with_player(app):
    """Fixture for adding Players to the database."""

    player = Players(id=1000,
                     first_name="Cristiano",
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
def app_with_user(app):
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


@pytest.fixture(params=weathers)
def weather_type(request):
    """Params type of fixure with all wather types."""
    current_weather = request.param

    return current_weather
