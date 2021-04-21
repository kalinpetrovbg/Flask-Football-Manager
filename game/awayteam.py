import random

from players.defender import Defender
from players.keeper import Keeper
from players.midfielder import Midfielder
from players.forward import Forward


class AwayTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)
        self.midfield = 0
        self.tactic = "4-3-3"

    @property
    def midfield(self):
        return self._midfield

    @midfield.setter
    def midfield(self, value):
        value = calculate_midfield_points(AWAY_TEAM)
        self._midfield = value

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


AWAY_TEAM = random.choice([Liverpool])
away_team = AWAY_TEAM.name
away_team_players = [player.name for player in AWAY_TEAM.players]
# print(', '.join(away_team_players))

def calculate_midfield_points(AWAY_TEAM):
    points = sum([player.playmaking for player in AWAY_TEAM.players if player.__class__.__name__ == "Midfielder"])
    return points

def calculate_attacking_points(AWAY_TEAM):
    points = sum([player.scoring for player in AWAY_TEAM.players if player.__class__.__name__ == "Forward"])
    return points

def calculate_defending_points(AWAY_TEAM):
    points = sum([player.defending for player in AWAY_TEAM.players if player.__class__.__name__ == "Defender"])
    return points

def calculate_goalkeeping_points(AWAY_TEAM):
    points = sum([player.goalkeeping for player in AWAY_TEAM.players if player.__class__.__name__ == "Keeper"])
    return points


mid = calculate_midfield_points(AWAY_TEAM)
forew = calculate_attacking_points(AWAY_TEAM)
defend = calculate_defending_points(AWAY_TEAM)
keep = calculate_goalkeeping_points(AWAY_TEAM)