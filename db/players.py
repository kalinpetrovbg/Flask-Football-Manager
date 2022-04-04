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

    def __add__(self, other):
        return [self, other]

"""Generate the database with players."""


db.create_all()

player1 = Players(
    first_name="David", last_name="De Gea", team_id=1, position="GK", overall=31, attack=4, middle=3, defence=87)
player2 = Players(
    first_name="Alex", last_name="Telles", team_id=1, position="DEF", overall=42, attack=14, middle=31, defence=81)
player3 = Players(
    first_name="Harry", last_name="Maguire", team_id=1, position="DEF", overall=48, attack=27, middle=33, defence=83)
player4 = Players(
    first_name="Raphaël", last_name="Varane", team_id=1, position="DEF", overall=49, attack=23, middle=37, defence=87)
player5 = Players(
    first_name="Diogo", last_name="Dalot", team_id=1, position="DEF", overall=43, attack=21, middle=29, defence=78)
player6 = Players(
    first_name="Scott", last_name="McTominay", team_id=1, position="DEF", overall=44, attack=12, middle=38, defence=82)
player7 = Players(
    first_name="Paul", last_name="Pogba", team_id=1, position="MID", overall=49, attack=33, middle=86, defence=27)
player8 = Players(
    first_name="Bruno", last_name="Fernandes", team_id=1, position="MID", overall=48, attack=35, middle=87, defence=22)
player9 = Players(
    first_name="Jadon", last_name="Sancho", team_id=1, position="ATT", overall=42, attack=85, middle=26, defence=15)
player10 = Players(
    first_name="Marcus", last_name="Rashford", team_id=1, position="ATT", overall=40, attack=83, middle=24, defence=13)
player11 = Players(
    first_name="Cristiano", last_name="Ronaldo", team_id=1, position="ATT", overall=50, attack=91, middle=36, defence=22)


# players = (player1 + player2) + (player3 + player4) + (player5 + player6) + (player7 + player8) + (player9 + player10)
# players.append(player11)
#
# for p in players:
#     db.session.add(p)
# db.session.commit()


# Todo for some reason the script is creating two players instead of only one.
