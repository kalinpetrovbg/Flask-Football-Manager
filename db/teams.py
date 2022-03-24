from fm.main import db


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    # logo = db.Column(db.Text, unique=True, nullable=False)
    country = db.Column(db.String, nullable=False)
    overall = db.Column(db.Integer, default=0)
    attack = db.Column(db.Integer, default=0)
    middle = db.Column(db.Integer, default=0)
    defence = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.name

# db.create_all()

# teams = [Teams(name="Manchester United", country="UK"),
#          Teams(name="Arsenal", country="UK"),
#          ]
#
# for t in teams:
#     db.session.add(t)
#     db.session.add(t)
# db.session.commit()
