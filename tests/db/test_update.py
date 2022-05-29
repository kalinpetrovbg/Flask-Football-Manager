"""Unit tests for update_teams function in db.update."""
import pytest

from app import db
from application.db import Players
from application.db.teams import Teams
from application.misc.update import update_teams, update_player


def test_if_update_function_gets_all_teams_from_db(app_with_two_teams):
    team1, team2 = app_with_two_teams

    assert team1.overall == 50
    assert team2.overall == 100

    teams = Teams.query.all()   # Todo
    teams = [str(t) for t in teams]

    assert teams == ['Manchester United', 'Arsenal']


def test_if_update_function_gives_correct_values(app_with_team, app_with_player):
    team = app_with_team

    """Team 1 Stats before the update."""
    assert team.attack == 0
    assert team.middle == 0
    assert team.defence == 0
    assert team.overall == 0

    teams_players = db.session.query(Players).filter(Players.team_id == 1000).all()

    assert len(teams_players) == 1

    update_teams()

    """Team 1 Stats after the update."""
    assert team.attack == 91
    assert team.middle == 36
    assert team.defence == 22
    assert team.overall == 50


def test_if_adding_second_player_gives_correct_values(app_with_team, app_with_player):
    team = app_with_team

    teams_players = db.session.query(Players).filter(Players.team_id == 1000).all()

    assert len(teams_players) == 1

    update_teams()

    """Stats when only 1 player is in the team."""
    assert team.attack == 91
    assert team.middle == 36
    assert team.defence == 22
    assert team.overall == 50

    """Adding new player to Team 1."""
    new_player = Players(first_name="Michael",
                         last_name="Owen",
                         team_id=1000, position="ATT",
                         overall=40, attack=80,
                         middle=30, defence=10)

    db.session.add(new_player)
    db.session.commit()

    teams_players = db.session.query(Players).filter(Players.team_id == 1000).all()

    assert len(teams_players) == 2

    update_teams()

    """Team 1 Stats after the update. It has now the updated stats."""
    assert team.attack == 86  # round (91 + 80 / 2)
    assert team.middle == 33  # round (36 + 30 / 2)
    assert team.defence == 16  # round (22 + 10 / 2)
    assert team.overall == 45  # round (50 + 40 / 2)

    db.session.delete(new_player)
    db.session.commit()


def test_update_team_if_there_are_no_players(app_with_team):
    team = app_with_team

    assert team.attack == 0
    assert team.middle == 0
    assert team.defence == 0
    assert team.overall == 0

    update_teams()

    assert team.attack == 0
    assert team.middle == 0
    assert team.defence == 0
    assert team.overall == 0


def test_update_player_overall_stats(app_with_player):

    player = Players.query.filter_by(id=1000).first()

    assert player.attack == 91
    assert player.overall == 50

    Players.query.filter_by(id=1000).update(dict(attack=94))
    db.session.commit()

    assert player.attack == 94
    assert player.overall == 50

    update_player(1000)

    assert player.overall == 51


def test_raises_exception_when_player_id_doesnt_exist(app_with_player):
    with pytest.raises(AttributeError):
        update_player(2000)

