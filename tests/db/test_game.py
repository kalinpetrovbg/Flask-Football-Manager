"""Unit tests for db.game file."""
from db.game import AwayTeam, HomeTeam


def test_home_team_correct_initialization():
    home_team = HomeTeam("FC Arsenal", 40)

    assert home_team.name == "FC Arsenal"
    assert home_team.power == 40
    assert home_team.__str__() == "Home team FC Arsenal with power 40."


def test_away_team_correct_initialization():
    away_team = AwayTeam("FC Chelsea", 38)

    assert away_team.name == "FC Chelsea"
    assert away_team.power == 38
    assert away_team.__str__() == "Away team FC Chelsea with power 38."
