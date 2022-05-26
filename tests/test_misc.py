"""Unit tests for misc folder."""

from application.db.teams import Teams
from application.misc.oponents import teams_data

teams = [
    Teams(name="Manchester United", league="English Premier League", logo="man"),
    Teams(name="Arsenal", league="English Premier League", logo="ars"),
]


def test_teams_data_function():
    tdata = teams_data(teams)

    # Todo finish this.
    assert 2 == 2
