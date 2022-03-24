from fm.main import db

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    # logo = db.Column(db.Text, unique=True, nullable=False)
    country = db.Column(db.String, nullable=False)

    def __repr__(self):
        return self.name


# teams = [Teams(name="Manchester United", country="UK"),
# Teams(name="Arsenal", country="UK"),
#      ]
#
#
# for t in teams:
#     db.session.add(t)
#     db.session.add(t)
# db.session.commit()
