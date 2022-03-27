from fm.app import db


class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    logo = db.Column(db.Text, default="no-logo")
    league = db.Column(db.String, nullable=False)
    overall = db.Column(db.Integer, default=0)
    attack = db.Column(db.Integer, default=0)
    middle = db.Column(db.Integer, default=0)
    defence = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.name


"""Generate the database with teams."""
teams = [Teams(name="Manchester United", league="English Premier League", logo="man"),
         Teams(name="Arsenal", league="English Premier League", logo="ars"),
         Teams(name="FC Kalin", league="Hattrick"),
         Teams(name="Barcelona", league="Spain Primera Division", logo="bar"),
         Teams(name="Juventus", league="Italian Serie A", logo="juv"),
         Teams(name="Roma", league="Italian Serie A", logo="rom"),
         Teams(name="Real Madrid", league="Spain Primera Division", logo="rea"),
         ]


# db.create_all()
#
# for team in teams:
#     db.session.add(team)
#
# db.session.commit()
