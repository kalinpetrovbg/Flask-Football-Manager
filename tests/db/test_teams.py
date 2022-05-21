"""Unit tests for Teams model."""


def test_if_teams_are_crated_correctly(app_with_teams):
    team = app_with_teams

    assert team.name == "Manchester United"
    assert team.league == "English Premier League"
    assert team.logo == "man"
