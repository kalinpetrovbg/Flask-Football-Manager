from sqlalchemy import func

from app import db
from db.players import Players
from db.teams import teams

for team in teams:
    total_attack = db.session.query(func.avg(Players.attack)).filter(Players.team_id == team.id).scalar()
    team.attack = round(total_attack)
    total_middle = db.session.query(func.avg(Players.middle)).filter(Players.team_id == team.id).scalar()
    team.middle = round(total_middle)
    total_defence = db.session.query(func.avg(Players.defence)).filter(Players.team_id == team.id).scalar()
    team.defence = round(total_defence)

    db.session.add(team)

db.session.commit()
