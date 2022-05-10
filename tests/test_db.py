"""Unit tests for db folder."""

from db.game import HomeTeam, AwayTeam
from db.names import spanish_f_names
from db.players import Players
from db.teams import Teams
from db.update import update_teams
from db.users import Users, AnonymousUser


def test_player_if_correctly_created():
    new_player = Players(first_name="Cristiano", last_name="Ronaldo", team_id=1, position="ATT", overall=50, attack=91,
                         middle=36, defence=22)

    assert new_player.overall == 50
    assert new_player.position == "ATT"
    assert new_player.first_name == "Cristiano"
    assert new_player.last_name == "Ronaldo"
    assert new_player.__repr__() == "Cristiano"


def test_teams_if_correctly_created():
    new_team = Teams(name="Manchester United", league="English Premier League", logo="man")

    assert new_team.league == "English Premier League"
    assert new_team.__repr__() == "Manchester United"


def test_home_team_initialization():
    home_team = HomeTeam("FC Arsenal", 40)

    assert home_team.__str__() == "Home team FC Arsenal with power 40."


def test_away_team_initialization():
    home_team = AwayTeam("FC Chelsea", 38)

    assert home_team.__str__() == "Away team FC Chelsea with power 38."


def test_users_are_created_correctly():
    new_user = Users()
    new_user.username = "Kalin"
    new_user.password = "f15s@"
    new_user.team_id = 1

    assert new_user.username == "Kalin"
    assert new_user.password == "f15s@"
    assert new_user.team_id == 1


def test_annonymouse_user_if_it_has_no_team():
    new_guest_user = AnonymousUser()

    assert new_guest_user.team_id is None


def test_update_teams_functionality():
    team1 = Teams(name="Manchester United", league="English Premier League", logo="man")
    team2 = Teams(name="Newcastle", league="English Premier League", logo="man")

    # Todo finish this.


def test_spanish_names():

    names = spanish_f_names

    assert "Santiago" in names
