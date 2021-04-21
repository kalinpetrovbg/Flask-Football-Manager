import random

from players.defender import Defender
from players.keeper import Keeper
from players.midfielder import Midfielder
from players.forward import Forward


class HomeTeam:
    def __init__(self, name, *players):
        self.name = name
        self.players = list(players)
        self.midfield = 38   # later to be calculated


Kalin = HomeTeam(
    "FC Kalin",
    Keeper("Yannic Banfi", 10, 10),
    Defender("Gasem Al-Marwani", 10, 10, 10),
    Midfielder("Jan Eger",10, 10, 10),
    Forward("Juraj Trška", 10, 10, 10)
)


HOME_TEAMS = random.choice([Kalin])
home_team = HOME_TEAMS.name
home_team_players = [player.name for player in HOME_TEAMS.players]

def home_team_lineup():
    home_team_players = [player.name for player in HOME_TEAMS.players]
    return ', '.join(home_team_players)