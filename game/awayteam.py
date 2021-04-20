import random

from players.defender import Defender
from players.keeper import Keeper
from players.midfielder import Midfielder
from players.winger import Winger
from players.forward import Forward

class AwayTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)
        self.midfield = 25   # later to be calculated


Liverpool = AwayTeam("Liverpool", Keeper("Player 1"), Defender("Player 2"), Midfielder("Player 3"),
                     Winger("Player 4"), Forward("Player 5"))
RealMadrid = AwayTeam("Real Madrid", Keeper("Player 1"), Defender("Player 2"), Midfielder("Player 3"),
                     Winger("Player 4"), Forward("Player 5"))
BayernMunich = AwayTeam("Bayern Munich", Keeper("Player 1"), Defender("Player 2"), Midfielder("Player 3"),
                     Winger("Player 4"), Forward("Player 5"))
Juventus = AwayTeam("FC Juventus", Keeper("Player 1"), Defender("Player 2"), Midfielder("Player 3"),
                     Winger("Player 4"), Forward("Player 5"))

AWAY_TEAMS = random.choice([Liverpool, RealMadrid, BayernMunich, Juventus])
away_team = AWAY_TEAMS.name
