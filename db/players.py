"""Generate players database table."""
from app import db
from db.teams import Teams


class Players(db.Model):
    """Build all players' data model."""

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

# """Manchester United players"""
# db.create_all()
#
# player1 = Players(
#     first_name="David", last_name="De Gea", team_id=1, position="GK", overall=31, attack=4, middle=3, defence=87)
# player2 = Players(
#     first_name="Alex", last_name="Telles", team_id=1, position="DEF", overall=42, attack=14, middle=31, defence=81)
# player3 = Players(
#     first_name="Harry", last_name="Maguire", team_id=1, position="DEF", overall=48, attack=27, middle=33, defence=83)
# player4 = Players(
#     first_name="Raphaël", last_name="Varane", team_id=1, position="DEF", overall=49, attack=23, middle=37, defence=87)
# player5 = Players(
#     first_name="Diogo", last_name="Dalot", team_id=1, position="DEF", overall=43, attack=21, middle=29, defence=78)
# player6 = Players(
#     first_name="Scott", last_name="McTominay", team_id=1,
#     position="MID", overall=44, attack=12, middle=82, defence=38)
# player7 = Players(
#     first_name="Paul", last_name="Pogba", team_id=1, position="MID", overall=49, attack=33, middle=86, defence=27)
# player8 = Players(
#     first_name="Bruno", last_name="Fernandes", team_id=1,
#     position="MID", overall=48, attack=35, middle=87, defence=22)
# player9 = Players(
#     first_name="Jadon", last_name="Sancho", team_id=1, position="ATT", overall=42, attack=85, middle=26, defence=15)
# player10 = Players(
#     first_name="Marcus", last_name="Rashford", team_id=1,
#     position="ATT", overall=40, attack=83, middle=24, defence=13)
# player11 = Players(
#     first_name="Cristiano", last_name="Ronaldo", team_id=1,
#     position="ATT", overall=50, attack=91, middle=36, defence=22)
#
# for p in players:
#     db.session.add(p)
# db.session.commit()
#
# """Arsenal players"""
# player1 = Players(
#     first_name="Aaron",
#     last_name="Ramsdale",
#     team_id=2,
#     position="GK",
#     overall=29,
#     attack=2,
#     middle=3,
#     defence=81,
# )
# player2 = Players(
#     first_name="Kieran",
#     last_name="Tierney",
#     team_id=2,
#     position="DEF",
#     overall=41,
#     attack=20,
#     middle=22,
#     defence=81,
# )
# player3 = Players(
#     first_name="Gabriel",
#     last_name="Magalhães",
#     team_id=2,
#     position="DEF",
#     overall=45,
#     attack=22,
#     middle=31,
#     defence=81,
# )
# player4 = Players(
#     first_name="Benjamin",
#     last_name="White",
#     team_id=2,
#     position="DEF",
#     overall=43,
#     attack=21,
#     middle=29,
#     defence=80,
# )
# player5 = Players(
#     first_name="T",
#     last_name="Tomiyasu",
#     team_id=2,
#     position="DEF",
#     overall=42,
#     attack=23,
#     middle=26,
#     defence=78,
# )
# player6 = Players(
#     first_name="Gabriel",
#     last_name="Silva",
#     team_id=2,
#     position="MID",
#     overall=39,
#     attack=20,
#     middle=79,
#     defence=18,
# )
# player7 = Players(
#     first_name="Granit",
#     last_name="Xhaka",
#     team_id=2,
#     position="MID",
#     overall=44,
#     attack=19,
#     middle=79,
#     defence=33,
# )
# player8 = Players(
#     first_name="Thomas",
#     last_name="Partey",
#     team_id=2,
#     position="MID",
#     overall=48,
#     attack=23,
#     middle=84,
#     defence=37,
# )
# player9 = Players(
#     first_name="Bukayo",
#     last_name="Saka",
#     team_id=2,
#     position="MID",
#     overall=43,
#     attack=27,
#     middle=83,
#     defence=18,
# )
# player10 = Players(
#     first_name="Martin",
#     last_name="Ødegaard",
#     team_id=2,
#     position="ATT",
#     overall=41,
#     attack=83,
#     middle=24,
#     defence=16,
# )
# player11 = Players(
#     first_name="Alexandre",
#     last_name="Lacazette",
#     team_id=2,
#     position="ATT",
#     overall=38,
#     attack=82,
#     middle=20,
#     defence=11,
# )
#
# for p in players:
#     db.session.add(p)
# db.session.commit()
