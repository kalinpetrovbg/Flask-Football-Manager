"""Unit tests for Teams model."""


def test_if_teams_are_crated_correctly(app_with_team):
    team = app_with_team

    assert team.name == "Manchester United 2"
    assert team.league == "English Premier League"
    assert team.logo == "man"
    assert team.__repr__() == "Manchester United 2"


def test_if_default_team_stats_are_equal_to_zero(app_with_team):
    team = app_with_team

    assert team.attack == 0
    assert team.middle == 0
    assert team.defence == 0
    assert team.overall == 0
