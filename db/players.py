from fm.main import db
from fm.db.teams import Teams

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    overall = db.Column(db.Integer, default=0)
    attack = db.Column(db.Integer, default=0)
    middle = db.Column(db.Integer, default=0)
    defence = db.Column(db.Integer, default=0)

    def __init__(self, id, first_name, last_name, team_id, overall, attack, middle, defence):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.team_id = team_id
        self.overall = overall
        self.attack = attack
        self.middle = middle
        self.defence = defence



    def __repr__(self):
        return self.first_name


# db.create_all()
