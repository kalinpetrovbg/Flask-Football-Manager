"""File that should be run to update newly created teams."""
from sqlalchemy import func

from application import db
from application.models import Teams, Players


def update_teams():
    """Updates team's statistics once team has been created."""

    teams = Teams.query.all()

    for team in teams:

        try:
            total_attack = (
                db.session.query(func.avg(Players.attack))
                    .filter(Players.team_id == team.id)
                    .scalar()
            )
            team.attack = round(total_attack)
            total_middle = (
                db.session.query(func.avg(Players.middle))
                    .filter(Players.team_id == team.id)
                    .scalar()
            )
            team.middle = round(total_middle)
            total_defence = (
                db.session.query(func.avg(Players.defence))
                    .filter(Players.team_id == team.id)
                    .scalar()
            )
            team.defence = round(total_defence)
            team_overall = round((team.attack + team.middle + team.defence) / 3)
            team.overall = team_overall

        except TypeError:
            team.attack = 0
            team.middle = 0
            team.defence = 0
            team.overall = 0

        db.session.commit()


def update_player(player_id):
    """Updates player's statistics."""
    try:
        player = Players.query.filter_by(id=player_id).first()
        new_overall = round(player.attack + player.middle + player.defence) / 3
        Players.query.filter_by(id=player_id).update(dict(overall=round(new_overall)))
        db.session.commit()
        print(f"Player {player} has just updated his overall stats. His new overal score is {round(player.overall)}")

    except AttributeError:
        raise AttributeError("No player to update.")


update_teams()
