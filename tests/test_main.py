"""Unit tests for main.py file."""

from app import app
from db.teams import Teams
from db.users import Users


def test_login_page():
    client = app.test_client()
    url = "/"
    response = client.get(url)

    # Todo - add db.

    team = Teams()

    user = Users()
    user.username = "kalin_petrov"
    user.password = "0Ury@gaj82"
    user.team_id = 1
    user_team = "Manchester United"


    assert user.username == "kalin_petrov"
    assert user_team == "Manchester United"

