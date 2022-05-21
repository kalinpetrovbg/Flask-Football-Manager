import pytest
from sqlalchemy import delete

from app import app
from app import db
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
    ctx = test_app.test_request_context()
    ctx.push()

    yield client
    ctx.pop()


@pytest.fixture(scope="session")
def app_with_db(flask_app):
    """Fixture for conntecting to the database."""
    db.create_all()

    yield flask_app
    db.session.commit()
    db.drop_all()


@pytest.fixture(scope="session")
def app_with_data(app_with_db):
    """Instert some data in the database."""
    user = Users()
    user.username = "kalin_petrov"
    user.password = "0Ury@gaj82"
    user.team_id = 1

    db.session.add(user)
    db.session.commit()

    yield app_with_db

    db.session.execute(delete(Users))
    db.session.commit()
