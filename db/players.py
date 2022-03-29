from fm.app import db
from fm.db.teams import Teams


class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey(Teams.id), nullable=True)
    position = db.Column(db.String, default="NA")
    overall = db.Column(db.Integer, default=0)
    attack = db.Column(db.Integer, default=0)
    middle = db.Column(db.Integer, default=0)
    defence = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.first_name


"""Generate the database with players."""


# db.create_all()
#
# player = Players(first_name="Kalin", last_name="Petrov",
#                  team_id=1, position="GK", overall=60, attack=80, middle=60, defence=40)
#
# db.session.add(player)
# db.session.commit()


# Todo for some reason the script is creating two players instead of only one.
