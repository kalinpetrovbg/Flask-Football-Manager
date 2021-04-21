import random

from players.defender import Defender
from players.keeper import Keeper
from players.midfielder import Midfielder
from players.forward import Forward


class AwayTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)
        self.midfield = 25  # later to be calculated
        self.tactic = "4-3-3"


Liverpool = AwayTeam(
    "Liverpool",
    Keeper("Alison Becker", 16, 9),
    Defender("Andrew Robertson", 13, 12, 14),
    Defender("Virgil van Dijk", 17, 11, 15),
    Defender("Joe Gomez", 15, 9, 14),
    Defender("Trent Alexander-Arnold", 12, 14, 16),
    Midfielder("Kai Havertz", 16, 14, 11),
    Midfielder("Fabinho", 14, 12, 15),
    Midfielder("Naby Keïta", 15, 14, 11),
    Forward("Sadio Mané", 15, 16, 12),
    Forward("Roberto Firmino", 15, 17, 13),
    Forward("Mohamed Salah", 15, 15, 10),
)


AWAY_TEAMS = random.choice([Liverpool])
away_team = AWAY_TEAMS.name
away_team_players = [player.name for player in AWAY_TEAMS.players]
print(', '.join(away_team_players))

