from sqlalchemy import func

from fm.app import db
from fm.db.players import Players
from fm.db.teams import Teams

teams = Teams.query.all()

for team in teams:

    try:
        total_attack = db.session.query(func.avg(Players.attack)).filter(Players.team_id == team.id).scalar()
        team.attack = round(total_attack)
        total_middle = db.session.query(func.avg(Players.middle)).filter(Players.team_id == team.id).scalar()
        team.middle = round(total_middle)
        total_defence = db.session.query(func.avg(Players.defence)).filter(Players.team_id == team.id).scalar()
        team.defence = round(total_defence)
        team_overall = (team.attack + team.middle + team.defence) // 3
        team.overall = team_overall

    except TypeError:
        team.attack = 0
        team.middle = 0
        team.defence = 0
        team.overall = 0

    db.session.commit()
