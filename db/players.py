from fm.main import db
from fm.db.teams import Teams

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=True, nullable=True)
    last_name = db.Column(db.String, unique=True, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

db.create_all()


p = Players(first_name="Gerard", last_name="Pique", team_id=1)


db.session.add(p)
db.session.add(p)
db.session.commit()